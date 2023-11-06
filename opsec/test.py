
#user login prototype
def check_login():
    user = input("Input username: ")
    password = input("Input password: ")

    if user == "gibz" and password == "1234":
        print("Access granted")
    else:
        print("Access denied, wrong password or username!!")
check_login()

