# https://prod.liveshare.vsengsaas.visualstudio.com/join?9078EC5AC58CE701C5D48767145EB0C5406C

import users


# Opening a file from other dict
file = open("users.py", "r")
contents = file.read()
file.close()

# Welcoming message
welcoming_note = """
WELCOME TO SIGMABANK!

WHERE FINANCIAL FREEDOM BEGINS!

PLEASE, INSERT YOUR CARD...

"""
print(welcoming_note)

# User inserts the card and requested to enter the PIN
userPIN = users.user1["PIN"]

print(userPIN)

# Number of trials for loging in
Trials = 3
#Limiting the trials
while Trials != 0:
    PIN = int(input("Please, Enter your 4 digits PIN number: "))
    if len(str(PIN)) < 4 or len(str(PIN)) > 4:
        print("Your PIN must be made of 4 digits!, Please try again.") 
    elif PIN != userPIN:
        Trials -= 1        
        print("Oops! Wrong PIN number, You Have ", Trials, "Trials Left")
    
    if Trials == 0:
        print("The ATM card is blocked! Please consult the bank administration for further assistance.")

else:
    if userPIN == int(PIN):
        print("GLAD TO HAVE YOU DEAR, .....")
    print("""
            SELECT THE TRANSACTION CURRENCY:
            1: KSh
            2: USD      
""")
currencyChoice = int(input("Enter Your Choice: "))
if currencyChoice == 1:
    print('Welcome! Your Transactions will be executed in "Kenyan Shillings" currency.')
elif currencyChoice == 2:
    print('Welcome! Your Transactions will be exe1cuted in "USD" currency.')
    print("INVALID CHOICE, PLEASE SELECT 1 OR 2") 

else:
    userDirect = currencyChoice    
    print(userDirect)