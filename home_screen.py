
def main_menu():
    select = input("""Hello ! Please select one of the following options:
    1. Sign in
    2. Sign out
    3. Register
    4. Admin
    Choose Option: """)
    try:
        option = int(select)
        if option == 1:
            import sign_in
        elif option == 2:
            import sign_out
        elif option == 3:
            import register
        elif option == 4:
            import admin
        else:
            print("the option you've chosen does not exist")
    except ValueError:
        print("Not Valid")

main_menu()
