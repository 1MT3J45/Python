
import MySQLdb
# sudo apt-get install python-mysqldb
# Open database connection

db = MySQLdb.connect("localhost","root","root101","iot")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : ", data
# disconnect from server

db.close()
