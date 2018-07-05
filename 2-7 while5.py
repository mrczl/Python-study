print ("Welcome to Programming World!")
name = input("Enter your name >")
pword = input("Enter your password >")
while True:
    if(name == "admin" and pword == "123"):
        print("login successful!")
        break
    elif(name == "admin" and pword != "123"):
        print("Password error!!!")
        continue
    else:
        print("Username is existed!")
         continue