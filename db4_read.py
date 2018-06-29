import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","root","root101","mydb" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM student"
try:
	# Execute the SQL command
	cursor.execute(sql)
	# Fetch all the rows in a list of lists.
	results = cursor.fetchall()
	for row in results:
		roll = row[0]
		name = row[1]
		marks = row[2]
		# Now print fetched result
		print "%-3d%-10s%-5.3f" % (roll, name, marks)
except:
	print "Error: unable to fetch data"

# disconnect from server
db.close()
