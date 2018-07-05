print ("Welcome to Programming World!")
name = input("Enter your name >")
pword = input("Enter your password >")
while True:
    if(name == "admin" and pword == "123"):
        print("login successful!")
        break
