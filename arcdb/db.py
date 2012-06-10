# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#######################################################################
import MySQLdb as mdb
import dbutil
import config as conf

class ArcDB:
	entity_types_list = list()
	entity_types_dict_key_url = dict()
	entity_types_dict_key_id = dict()
	entity_properties_dict_key_id = dict()
	
	property_in_entity_list = list()
	property_in_entity_key_eid = dict()

	etype_props_dict = dict()

	def load_entity_types(self):
		try:
			con = dbutil.connect()
			cur = con.cursor(mdb.cursors.DictCursor)

			#get the entity type
			cur.execute('select * from entity_type')
			self.entity_types_list = list(cur.fetchall())
			#print self.entity_types_list
			for entity_type in self.entity_types_list:
				self.entity_types_dict_key_id[entity_type.get('id')] = entity_type
				self.entity_types_dict_key_url[entity_type.get('url')] = entity_type
			#print self.entity_types_dict_url
			#print self.entity_types_dict_id
			
		except:
			raise
		finally:
			if con:    
				con.close()
	def load_property_in_entity(self):

		try:
			con = dbutil.connect()
			cur = con.cursor(mdb.cursors.DictCursor)

			cur.execute('select * from property_in_entity')
			self.property_in_entity_list = list(cur.fetchall())
			#print self.property_in_entity_list
			
			for etype in self.entity_types_list:
				#self.property_in_entity_key_eid[property_in_entity.get('entity_type_id')] = property_in_entity
				prop_id_list = list()
				prop_list = list()
				for tpe in self.property_in_entity_list:
					if etype.get('id') == tpe.get('entity_type_id'):
						prop_id_list.append(tpe.get('property_id'))
						cur.execute("select * from property where id=%s", tpe.get('property_id'))
						prop = cur.fetchone()
						prop_list.append(prop)
				
				self.etype_props_dict[etype.get('id')] = prop_list
				self.property_in_entity_key_eid[etype.get('id')] = prop_id_list


			#print self.property_in_entity_key_eid
			print self.etype_props_dict
				
		except:
			raise
		finally:
			if con:    
				con.close()

	def __init__(self):
		print "in init"
		try:
			self.load_entity_types()
			self.load_property_in_entity()

		except:
			raise

	def get_entities_by_type(self, entity_type_url):
		try:
			con = dbutil.connect()
			cur = con.cursor(mdb.cursors.DictCursor)

			#get the entity type
			entity_type = self.entity_types_dict_key_url.get(entity_type_url)
			print entity_type

			#get entity data
			cur.execute("select * from entity_data where entity_type_id=%s", entity_type["id"])
			entity_data = cur.fetchall()

			entities = list()
			print '############################################'
			for entity_instance in entity_data:
				entity = dict(entity_instance)
				entity['entity_type_url'] = entity_type.get('url')
				#print entity
				for entity_prop in self.etype_props_dict.get(entity_type.get('id')):
					prop_data_table_name = "prop_"+entity_prop["label"]+"_data"
					#print prop_data_table_name
					prop_data_query = "select * from %s where entity_data_id=%s" % (prop_data_table_name, entity_instance["id"])
					#print prop_data_query
					cur.execute(prop_data_query)
					entity_prop_value = cur.fetchone()
					entity[entity_prop["label"]] = entity_prop_value['value']
				entities.append(entity)


			for te in entities:
				for k, v in te.items():
					print k, ':', v
				print '############################################'

			
		except mdb.Error, e:

			raise

		finally:    

			if con:
				con.close()

