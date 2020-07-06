import mysql.connector
import datetime
from datetime import time
time
now = datetime.datetime
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="lifechoicesonline"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE sign_in_users (id INT AUTO_INCREMENT PRIMARY KEY, full_name VARCHAR(60),"
                 " username VARCHAR(50), password VARCHAR(20), login_date datetime, login_time datetime)")
mycursor.execute("CREATE TABLE register_users (id INT AUTO_INCREMENT PRIMARY KEY, full_name VARCHAR(60),"
                 " username VARCHAR(50), password VARCHAR(20), contact_number INT(10))")
mycursor.execute("CREATE TABLE sign_out_users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50),"
                 " password VARCHAR(20), logout_date datetime, logout_time datetime)")

