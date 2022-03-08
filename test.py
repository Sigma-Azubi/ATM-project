def importUsers():
    from users import user1

    # Opening a file from other dict
    file = open("users.py", "r")
    contents = file.read()
    file.close()

    # print(type(dictionary))
    # print(dictionary)
    print(contents)
    # dictionary = user1.literal_eval(contents)
    
    
    

def close():
    userChoice = """ 
    PLEASE SELECT TRANSACTION:
    1- STATEMENT
    2- CHECK BALANCE
    3- WITHDRAW
    4- DEPOSIT
    5- QUIT 
    """
        
    userExit = input("Would you like to continue? Y/N: ").upper()
    if userExit == "N":
        userExitConfirm = input("Are You Sure You Want To Exit? Y/N: ").upper()
        if userExitConfirm == "Y":
            print("THANK YOU FOR BANKING WITH US")
            print("PLEASE PICK YOUR CARD")
            
        elif userExitConfirm == "N":
            print(userChoice)
            choiceSelected  = input("PLEASE SELECT TRANSACTION: ")
        
        
        elif userExitConfirm != "Y" or "N":
            print('INVALID CHOICE, PLEASE ENTER "Y" or "N"')
            

    elif userExit == "Y":
        print(userChoice)
        choiceSelected  = input("PLEASE SELECT TRANSACTION: ")
        


from users import usersList

#all user pins will be recorded here
allpins = []
usersNumber = len(usersList) # 1 - 9

# print(usersNumber)
for user in range(usersNumber):
    usersname = usersList[user]["username"]
    usersPins = usersList[user]["PIN"]
    print(usersPins, usersname)
    # allpins.append(usersPins)


# passwd = input("Please enter pin: ")
# if passwd in allpins:
#     print("You have sucessfully logged In!")
