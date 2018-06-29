import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root101","i2it" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

name = raw_input("enter name: ")
roll = input("enter roll: ")
marks = input("enter marks: ")
# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO students VALUES ('%s',%d, %d)" %(name, roll, marks)
try:
	# Execute the SQL command
	cursor.execute(sql)
	# Commit your changes in the database
	db.commit()
except:
	# Rollback in case there is any error
	print "Error"
	db.rollback()
# disconnect from server
db.close()
