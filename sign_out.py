import mysql.connector
import datetime
now = datetime.datetime.utcnow()
mydb = mysql.connector.connect(host="localhost", port="3306", user="root", passwd="1234",
                                         database="lifechoicesonline")

mycursor = mydb.cursor()

sql = 'Insert into sign_out_users (username, password,logout_date ,logout_time) VALUES(%s, %s, curdate(),current_time())'
val = (input("Enter Username: "), input("Enter Password: "))
mycursor.execute(sql, val)

mydb.commit()