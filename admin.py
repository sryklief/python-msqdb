def menu():
    select = input("""Please select one of the following options:
    1. Register user 
    2. Delete user 
    3. Register 
    4. Show sign in and sign out tables 
    5. Upgrade/Downgrade privileges
    Choose Option: """)
    try:
        option = int(select)
        if option == 1:
            import add_user
        elif option == 2:
            import delete_user
        elif option == 3:
            import register
        elif option == 4:
            import show_tables
        elif option == 5:
            import grants
        else:
            print("the option you've chosen does not exist")
    except ValueError:
        print("Not Valid")

menu()