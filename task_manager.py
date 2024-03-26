from helper import signup, login

if __name__ == '__main__':
    print("WELCOME TO TASK MANAGER APP")
    print("Are you new to this software ??")
    a = int(input("Type 1 if new otherwise press 0 ::"))
    if a == 1:
        signup()
    elif a == 0:
        login()
    else:
        print("You have provided wrong input !")