import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","root","root101","mydb")
# prepare a cursor object using cursor() method

cursor = db.cursor()
marks = int(raw_input("Enter updated Marks: "))
# Prepare SQL query to UPDATE required records
sql = "UPDATE student SET marks = %d" %(marks)
try:
	# Execute the SQL command
	cursor.execute(sql)
	# Commit your changes in the database
	db.commit()
except:
	# Rollback in case there is any error
	db.rollback()

# disconnect from server
db.close()
