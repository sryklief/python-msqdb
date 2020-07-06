import mysql.connector
mydb = mysql.connector.connect(host="localhost", port="3306", user="root", passwd="1234",
                                         database="lifechoicesonline")


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM sign_in_users, sign_out_users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)