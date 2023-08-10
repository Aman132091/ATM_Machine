from cardholder import cardHolder

def print_menu():
    ###print options to the users
    print("choose option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")


def deposit(cardHolder):
    try:
        deposit = float(input("How much: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("thankyou for deposit.new balance: ",str(cardHolder.get_balance()))
    except:
        print("Invalid input")

def withdraw(cardHolder):
    try:
        withdraw= float(input("How much: "))
        ###check if user have enough money
        if(cardHolder.get_balance()<withdraw):
            print("Sufficient Balance: ")

        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("you are good to go! thankyou : ")
    except:
        print("Invalid input")

def check_balance(cardHolder):
    print("current balance: ",cardHolder.get_balance())

if __name__=="__main__":
    current_user=cardHolder("","","","","")

    ###create a repo cardHolder
    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("82486374682749249284",1234,"john","griffith",150.31))
    list_of_cardHolders.append(cardHolder("82759759879573498579",4321,"asg","sapna", 200.98))
    list_of_cardHolders.append(cardHolder("78562495060884847696",5678,"kjl","singh",1000.01))
    list_of_cardHolders.append(cardHolder("36352427143633445676",8765,"nans","thakur",134.21))
    list_of_cardHolders.append(cardHolder("76364759607846456975",9012,"aman","thakur",100.81))


###prompt user for debit card number
    debitCaedNum=""
    while True:
        try:
            debitCardNum = input("please insert your debit card :")
            ###check against repo
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            if(len(debitMatch)>0):
                current_user = debitMatch[0]
            else:
                print("card number not recognized. please try again.")
        except:
            print("card number not recognized. please try again.")
            
    
###prompt for pin

        while True:
            try:
                userPin=int(input("Plese enter your pin :").strip())
                if (current_user.get_pin() == userPin):
                    break
                else:
                    print("Invalid pin: ")

            except:
                print("Invalid pin: ")

     ###print options

        print("Welcome ", current_user.get_firstname(), " :)")
        option = 0
        while (option != 4):
            print_menu()
            try:
                option = int(input())
            except:
                print("Invalid Input: ")

            if (option == 1):
                deposit(current_user)
            elif(option == 2):
                withdraw(current_user)
            elif(option==3):
                check_balance(current_user)
            elif(option==4):
                break
            else:
                option = 0

        print("Thankyou. Have a nice day")











