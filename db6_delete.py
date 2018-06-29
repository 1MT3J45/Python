#!/usr/bin/python

import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","root","root101","mydb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to DELETE required records
sql = "DELETE FROM student WHERE roll = 2"
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
