from users import usersList 

# Welcoming message
welcoming_note = """
WELCOME TO SIGMABANK!

WHERE FINANCIAL FREEDOM BEGINS!

PLEASE, INSERT YOUR CARD...

"""
print(welcoming_note)

# User inserts the card and requested to enter the PIN

users,passwds = [],[]

for user in usersList:
    users.append(user["username"])
    passwds.append(user["PIN"])


# Number of trials for loging in
Trials = 3
#Limiting the trials
while Trials != 0:
    PIN = int(input("Please, Enter your 4 digits PIN number: "))
    if len(str(PIN)) < 4 or len(str(PIN)) > 4:
        print("Your PIN must be made of 4 digits!, Please try again.") 
    elif PIN not in passwds:
        Trials -= 1        
        print("Oops! Wrong PIN number, You Have ", Trials, "Trials Left")
    
    if Trials == 0:
        print("The ATM card is blocked! Please consult the bank administration for further assistance.")

    else:
        if PIN in passwds:
            print("GLAD TO HAVE YOU DEAR, .....")
            print("""
                SELECT THE TRANSACTION CURRENCY:
                1: KSh
                2: USD """)
            currencyChoice = int(input("Enter Your Choice: "))
            if currencyChoice == 1:
                print('Welcome! Your Transactions will be executed in "Kenyan Shillings" currency.')
            elif currencyChoice == 2:
                print('Welcome! Your Transactions will be exe1cuted in "USD" currency.')

            else:
                print("INVALID CHOICE, PLEASE SELECT 1 OR 2") 
                userDirect = currencyChoice    
                print(userDirect)
            break

def cash_deposit(deposit_amount):
    global opening_balance  
    print("Your A/C balance is ${}".format(opening_balance))
    opening_balance = opening_balance + deposit_amount  
    print("Your Updated A/C balance is ${}".format(opening_balance))

def change_pin(old_pin, new_pin):
    global current_pin  
    if not old_pin == current_pin:
        print('Invalid old PIN, Please try again or visit the nearest branch')
    else:
        current_pin = new_pin    
        print('ATM Card PIN ending with xx23 is updated Successfully!')

opening_balance = 20000
current_pin = 1234
def display_balance():
    print('Your A/C balance is ${}'.format(opening_balance))
    
def cash_withdraw(withdrawal_amount):
    global opening_balance  
    print('Your A/C balance is ${}'.format(opening_balance))
    opening_balance = opening_balance - withdrawal_amount  
    print("Your Updated A/C balance is ${}".format(opening_balance))

def cash_deposit(deposit_amount):
    global opening_balance  
    print("Your A/C balance is ${}".format(opening_balance))
    opening_balance = opening_balance + deposit_amount  
    print("Your Updated A/C balance is ${}".format(opening_balance))
    
    #Interface or Frontend (CLI i.e Command Line Interface)
    choice = None
    amount = None
    old_pin = None
    new_pin = None
    while True:
        print(""" 
            Welcome to SIGMABANK!  
            1. Check A/C Balance  
            2. Cash Withdraw  
            3. Cash Deposit  
            4. Change PIN
            """)
        choice = int(input("Please Enter Choice: "))
        if choice == 1:
            display_balance()
        elif choice ==2:
            amount = int(input("Enter Withdrawal Amount: "))
            cash_withdraw(amount)
        elif choice ==3:
            amount = int(input("Enter Deposit Amount: "))
            cash_deposit(amount)
        elif choice ==4:
            old_pin = int(input("Enter Your Current PIN: "))
            new_pin = int(input('Enter New PIN: '))
            change_pin(old_pin, new_pin)
        else:
            print("Invalid Choice.")

