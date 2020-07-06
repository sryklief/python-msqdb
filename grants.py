import mysql.connector
mydb = mysql.connector.connect(host="localhost", port="3306", user="root", passwd="1234",
                                         database="lifechoicesonline")


mycursor = mydb.cursor()

# Define a method to create MySQL users
def create_User(mycursor, userName, password):
    try:
        sql = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';" % (userName, password);
        mycursor.execute(sql);
    except Exception as Ex:
        print("Error creating MySQL User: %s" % (Ex));
def grant_privileges(mycursor, userName, password):
    try:
        sql = "Grant CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';" % (userName, password);
        mycursor.execute(sql);
    except Exception as Ex:
        print("Error creating MySQL User: %s" % (Ex));
create_User(mycursor, input("Enter user: "), (input("Enter Password: ")))
mycursor.execute("select host, user from mysql.user;")
# Fetch all the rows
all_my_users = mycursor.fetchall()
print("List of users:")
for user in all_my_users:
    print(user)