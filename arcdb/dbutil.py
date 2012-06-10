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
import config as conf



def hello():
	print "hello:", host
	print "hello user", user

def connect():
	try:
		con = mdb.connect(conf.mysql_config.get('host'), conf.mysql_config.get('user'), conf.mysql_config.get('password'), conf.mysql_config.get('database'))
	except mdb.Error, e:
		#print "Error %d: %s" % (e.args[0],e.args[1])
		raise
	else:
		return con
