import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","root","root101","mydb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS becomp")

# Create table as per requirement
sql = """CREATE TABLE student (
FIRST_NAME CHAR(20) NOT NULL,
AGE INT,
MARKS FLOAT )"""
cursor.execute(sql)

# disconnect from server
db.close()
