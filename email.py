email = input("Enter an email address: ")
k, j, d = 0,0,0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Email address format is incorrect! - 5")
                else:
                    print("Email address is correct.")
            else:
                print("Email address format is incorrect! - 4")
        else:
            print("Email address format is incorrect! - 3")
    else:
        print("Email address format is incorrect! - 2")
else:
    print("Email address format is incorrect! - 1")
