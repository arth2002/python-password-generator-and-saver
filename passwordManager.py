import secrets
import string

while True:
    try:
        def password(length):
            source = string.ascii_letters + string.punctuation + string.digits
            secure_password = "".join(secrets.choice(source) for i in range(length))
            print(secure_password)
            return secure_password


        size = int(input("How many character you want in password: "))
        password(size)
        while True:
            ask = input("Are you using this password, Y for yes and N for No : ")
            if ask == "y" or ask == "Y":
                savePassword = password(size)
                forWhat = input("For which account or website's password is this: ")
                with open("password.txt", "a") as f:
                    f.write(forWhat)
                    f.write(" : ")
                    f.write(str(savePassword))
                exit(0)
            elif ask == "n" or ask == "N":
                break
            else:
                print("Enter valid choice")
                continue
        resumeOrNot = input("Q for Quit and press anything to continue.. ")
        if resumeOrNot == "Q" or resumeOrNot == "q":
            print("Thank you for using this programme")
            exit(0)
        else:
            continue
    except Exception as e:
        print("Enter valid choice")
        print(e)
