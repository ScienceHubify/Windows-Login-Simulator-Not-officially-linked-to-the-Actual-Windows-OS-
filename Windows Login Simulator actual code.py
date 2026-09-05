Operatingsystem = input("Kindly choose one of the operating system you want to boot into (Windows 11,Windows 10,Windows 7)")
if Operatingsystem == "Windows 11":
    Username = input ("Kindly choose one of the usernames you want to log into (Admin,User 1, Guest)")
    if Username == "Admin":
        Password = int(input ("Kindly enter your password here)"))
        if Password == 2024:
            print("Welcome, Windows is starting")
        else:
            print("You need to re-enter this password")
    elif Username == "User 1":
        Password = int(input("You need to enter your Password"))
        if Password == 2024:
            print("Welcome, Windows is starting")
        else:
            print("Please re-enter your password")
    elif Username == "Guest":
        print("This is a Guest account and this does not let you access the personal files or accounts of the users present on this computer, you will be provided with a small space allocated on the drive which will not affect any other user or administartor account present on this computer, and the space will be shortly cleaned as soon as you sign on, inclusing the browser and other work data also")
elif Operatingsystem == "Windows 10":
    Username = input("You need to choose one of these Usernames to sign in (Admin, User 1, User 2, Guest")
    if Username == "Admin":
        Password = input("You will need to enter your administrator password")
        if Password == "User@DFG":
            print("Welcome ..... ..... ....")
        else:
            print("You will need to re-enter the Password since, it is incorrect")
    elif Username == "User 1":
        Password = int(input("You will need to enter your password for signing into your account"))
        if Password == 2024:
            print("Welcome to Windows")
        else:
            print("You need to re-enter your password")
    elif Username == "User 2":
        Password = int(input("You need to enter your Password"))
        if Password == 2024:
            print("Welcome, Windows is Starting")
        else:
            print("You need to re-enter your password")
    elif Username == "Guest":
        print("This is a guest account and this will not let you access the internal disks, this will create a small allocated space for you to store and run your programs, which will be later erased once you sign out")
elif Operatingsystem == "Windows 7":
    Username = input("You will have to choose one of these usernames to continue logging into an account Admin or Guest")
    if Username == "Admin":
        Password = int(input("You will need to enter your password"))
        if Password == 2023:
            print("Windows is starting")
        else:
            print("You will need to re-enter the password")
    elif Username == "Guest":
        print("Any changes made to the computer will not work and Welcome to Windows")
  

    