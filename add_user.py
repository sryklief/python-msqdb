import mysql.connector
mydb = mysql.connector.connect(host="localhost", port="3306", user="root", passwd="1234",
                                         database="lifechoicesonline")


mycursor = mydb.cursor()

sql = 'Insert into register_users (full_name, username, password, contact_number) VALUES(%s, %s, %s, %s)'
val = (input("Enter Fullname: "), input("Create Username: "), input("Enter Password: "),
       int(input("Enter cell number: ")))
mycursor.execute(sql, val)

mydb.commit()