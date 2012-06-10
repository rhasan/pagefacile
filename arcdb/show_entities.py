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
import sys
con = None

entity_type_url = "http://schema.org/Person"

try:

    con = mdb.connect('localhost', 'testuser', 
        'test623', 'pagefacile');

    cur = con.cursor(mdb.cursors.DictCursor)
    
    #get the entity type
    cur.execute("select * from entity_type where url=%s", entity_type_url)
    entity_type = cur.fetchone()

    #rows = cur.fetchall()

    #for row in rows:
    #    print "%s %s %s" % (row["id"], row["label"], row["url"])

    #print con.open


    entity_properties = list()
    #get entity schema
    cur.execute("select * from property_in_entity where entity_type_id=%s", entity_type["id"])

    properties_of_entity = cur.fetchall()
    for eprop in properties_of_entity:
        #print "property id: %s" % (eprop["property_id"])

        #get the label of the current property
        cur.execute("select * from property where id=%s", eprop["property_id"])
        prop = cur.fetchone()
        #print "property label: %s" % (prop["label"])
        entity_properties.append(prop)


    #for tp in entity_properties:
    #    print tp
    #get entity data
    cur.execute("select * from entity_data where entity_type_id=%s", entity_type["id"])
    entity_data = cur.fetchall()

    entities = list()
    for entity_instance in entity_data:
        
        entity = dict(entity_instance)
        entity['eitity_type_url'] = entity_type['url']
        #print entity
        for entity_prop in entity_properties:
            prop_data_table_name = "prop_"+entity_prop["label"]+"_data"
            #print prop_data_table_name
            prop_data_query = "select * from %s where entity_data_id=%s" % (prop_data_table_name, entity_instance["id"])
            #print prop_data_query
            cur.execute(prop_data_query)
            entity_prop_value = cur.fetchone()
            entity[entity_prop["label"]] = entity_prop_value['value']
        entities.append(entity)

    #print entities

    for te in entities:
        for k, v in te.items():
            print k, ':', v
        print '############################################'

except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
    
    if con:    
        con.close()
    
