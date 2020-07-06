import mysql.connector
try:
    mydb = mysql.connector.connect(host="localhost", port="3306", user="root", passwd="1234",
                                         database="lifechoicesonline")


    mycursor = mydb.cursor()

    cursor = mydb.cursor()
    sql_Delete_query = """DELETE from register_users where username = %s"""
    usernameId = (input("Enter Username: "))
    cursor.execute(sql_Delete_query, (usernameId,))
    mydb.commit()
    print("Record Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to Delete record from table: {}".format(error))
finally:
    if mydb.is_connected():
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")