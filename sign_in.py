import mysql.connector
import datetime
now = datetime.datetime.utcnow()
mydb = mysql.connector.connect(host="localhost", port="3306", user="root", passwd="1234",
                                         database="lifechoicesonline")

print("===================Welcome to lifechoices====================")

mycursor = mydb.cursor()

sql = 'Insert into sign_in_users (full_name, username, password, login_date, login_time) VALUES(%s, %s, %s, curdate(), current_time() )'
val = (input("Enter Fullname: "), input("Enter Username: "), input("Enter Password: "))
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Login Successfull.")