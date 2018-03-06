import time
global balanceJack, balanceSatan, balanceSnoop, balanceLandfried, balanceSteve, balanceBarack, balanceTrump, name, egg
balanceSatan = 666666
balanceJack = 134321
balanceSnoop = 2346354862
balanceLandfried = 10000000000000000
balanceSteve = 3745725437
balanceObama = 2334563457
balanceTrump = 2346
balancenew = 0
name = []
egg = 'false'
   
def inv():
    print 'Invalid input'

def options():
    print ('\'Balance\' to see your balance, \'Deposit\' to deposit more money, \'Withdraw\' to witdraw money,')
    print ('\"deposit\" to deposit, \"exit\" to exit, or \"transfer\" to transfer' )

def atm(): 
    def new():
        global balancenew, balanceJack, balanceSatan, balanceSnoop, balanceLandfried, balanceSteve, balanceObama, balanceTrump, name, egg 
        if egg == 'true':
            def newb():
                global balancenew, balanceJack, balanceSatan, balanceSnoop, balanceLandfried, balanceSteve, balanceObama, balanceTrump, egg
                options()
                action = raw_input(name)
                if action == 'Balance' or action == 'balance':
                    print 'Your balance is', balancenew
                    newb()
                elif action == 'Deposit' or action == 'deposit':
                    print 'How much would you like to deposit?'
                    deposit = int(raw_input('Deposit:'))
                    balancenew += int(deposit)
                    newb()
                elif action == 'Withdraw' or action == 'withdraw':
                    print 'How much would you like to withdraw?'
                    withdraw = int(raw_input('Withdraw:'))
                    if int(withdraw) < balancenew:
                        balancenew -= int(withdraw)
                        newb()
                    elif int(withdraw) > int(balancenew):
                        print 'Sorry insufficient funds.'
                        newb()
                    else:
                        print 'Unknown command'
                        newb()
                elif action == 'Transfer' or action == 'transfer':
                    print 'Who would you like to transfer to?'
                    who = raw_input('Enter Name:')
                    if who == 'jack' or who == 'Jack':
                        print 'How much would you like to transfer to jack.'
                        money = int(raw_input('Enter Amount:'))
                        if int(money) < int(balancenew):
                            balancenew -= int(money)
                            balanceJack += int(money)
                            print money, 'has been transferred to jacks account'
                            print 'Your current balance is', balancenew
                            newb()
                        elif money > balancenew:
                            print 'Insufficient funds.'
                            newb()
                        else:
                            print 'Unknown command.'
                            newb()
                    elif who == 'satan' or who == 'Satan':
                        print 'How much would you like to transfer to satan.'
                        money = int(raw_input('Enter Amount:'))
                        if money < balancenew:
                            balancenew -= money
                            balanceSatan += money
                            print money, 'has been transferred to satanss account'
                            print 'Your current balance is', balancenew
                            newb()
                        elif money > balancenew:
                            print 'Insufficient funds.'
                            newb()
                        else:
                            print 'Unknown command.'
                            newb()
                    elif who == 'snoop' or who == 'Snoop':
                        print 'How much would you like to transfer to snoop.'
                        money = int(raw_input('Enter Amount:'))
                        if money < balancenew:
                            balancenew -= money
                            balanceSnoop += money
                            print money, 'has been transferred to snoops account'
                            print 'Your current balance is', balancenew
                            newb()
                        elif money > balancenew:
                            print 'Insufficient funds.'
                            newb()
                        else:
                            print 'Unknown command.'
                            newb()
                    elif who == 'landfried' or who == 'Landfried':
                        print 'How much would you like to transfer to landfried.'
                        money = int(raw_input('Enter Amount:'))
                        if money < balancenew:
                            balancenew -= money
                            balanceLandfried += money
                            print money, 'has been transferred to landfrieds account'
                            print 'Your current balance is', balancenew
                            newb()
                        elif money > balancenew:
                            print 'Insufficient funds.'
                            newb()
                        else:
                            print 'Unknown command.'
                            newb()
                    elif who == 'steve' or who == 'Steve':
                        print 'How much would you like to transfer to steve.'
                        money = int(raw_input('Enter Amount:'))
                        if money < balancenew:
                            balancenew -= money
                            balanceSteve += money
                            print money, 'has been transferred to steves account'
                            print 'Your current balance is', balancenew
                            newb()
                        elif money > balancenew:
                            print 'Insufficient funds.'
                            newb()
                        else:
                            print 'Unknown command.'
                            newb()
                    elif who == 'obama' or who == 'Obama':
                        print 'How much would you like to transfer to obama.'
                        money = int(raw_input('Enter Amount:'))
                        if money < balancenew:
                            balancenew -= money
                            balanceObama += money
                            print money, 'has been transferred to obamas account'
                            print 'Your current balance is', balancenew
                            newb()
                        elif money > balancenew:
                            print 'Insufficient funds.'
                            newb()
                        else:
                            print 'Unknown command.'
                            newb()
                    elif who == 'trump' or who == 'Trump':
                        print 'How much would you like to transfer to trump.'
                        money = int(raw_input('Enter Amount:'))
                        if money < balancenew:
                            balancenew -= money
                            balanceTrump += money
                            print money, 'has been transferred to trumps account'
                            print 'Your current balance is', balancenew
                            newb()
                        elif money > balancenew:
                            print 'Insufficient funds.'
                            newb()
                        else:
                            print 'Unknown command.'
                            newb()
                elif action == 'exit' or action == 'Exit':
                    atm()
                else:
                    print 'Unknown Command'
                    newb()
            newb()
        else:
            print 'Welcome to Champion National Bank.'
            print 'To start a new account enter your name.'
            name = raw_input('Name:') + ":"
            print 'Welcome', name[0:6]
            print 'You currently have 0 dollars in your account, deposit some money to open your account.'
            deposit = int(raw_input('Deposit:'))
            if deposit > 0:
                egg = 'true'
                balancenew += int(deposit)
                def newa():
                    global balancenew, balanceJack, balanceSatan, balanceSnoop, balanceLandfried, balanceSteve, balanceObama, balanceTrump
                    print 'Type \'Balance\' to see your balance, \'Deposit\' to deposit more money, \'Withdraw\' to withdraw money'
                    print '\"Transfer\" to transfer, or \"Exit\" to exit.'
                    action = raw_input(name)
                    if action == 'Balance' or action == 'balance':
                        print 'Your balance is', balancenew
                        newa()
                    elif action == 'Deposit' or action == 'deposit':
                        print 'How much would you like to deposit?'
                        deposit = int(raw_input('Deposit:'))
                        balancenew += int(deposit)
                        newa()
                    elif action == 'Withdraw' or action == 'withdraw':
                        print 'How much would you like to withdraw?'
                        withdraw = raw_input('Withdraw:')
                        if int(withdraw) < int(balancenew):
                            balancenew -= int(withdraw)
                            newa()
                        elif withdraw > balancenew:
                            print 'Sorry insufficient funds.'
                            newa()
                        else:
                            print 'Unknown command'
                            newa()
                    elif action == 'Transfer' or action == 'transfer':
                        print 'Who would you like to transfer to?'
                        who = raw_input('Enter Name:')
                        if who == 'jack' or who == 'Jack':
                            print 'How much would you like to transfer to jack.'
                            money = int(raw_input('Enter Amount:'))
                            if money < balancenew:
                                balancenew -= int(money)
                                balanceJack += int(money)
                                print money, 'has been transferred to jacks account'
                                print 'Your current balance is', balancenew
                                newa()
                            elif money > balancenew:
                                print 'Insufficient funds.'
                                newa()
                            else:
                                print 'Unknown command.'
                                newa()
                        elif who == 'satan' or who == 'Satan':
                            print 'How much would you like to transfer to satan.'
                            money = int(raw_input('Enter Amount:'))
                            if money < balancenew:
                                balancenew -= money
                                balanceSatan += money
                                print money, 'has been transferred to satanss account'
                                print 'Your current balance is', balancenew
                                newa()
                            elif money > balancenew:
                                print 'Insufficient funds.'
                                newa()
                            else:
                                print 'Unknown command.'
                                newa()
                        elif who == 'snoop' or who == 'Snoop':
                            print 'How much would you like to transfer to snoop.'
                            money = int(raw_input('Enter Amount:'))
                            if money < balancenew:
                                balancenew -= money
                                balanceSnoop += money
                                print money, 'has been transferred to snoops account'
                                print 'Your current balance is', balancenew
                                newa()
                            elif money > balancenew:
                                print 'Insufficient funds.'
                                newa()
                            else:
                                print 'Unknown command.'
                                newa()
                        elif who == 'landfried' or who == 'Landfried':
                            print 'How much would you like to transfer to landfried.'
                            money = int(raw_input('Enter Amount:'))
                            if money < balancenew:
                                balancenew -= money
                                balanceLandfried += money
                                print money, 'has been transferred to landfrieds account'
                                print 'Your current balance is', balancenew
                                newa()
                            elif money > balancenew:
                                print 'Insufficient funds.'
                                newa()
                            else:
                                print 'Unknown command.'
                                newa()
                        elif who == 'steve' or who == 'Steve':
                            print 'How much would you like to transfer to steve.'
                            money = int(raw_input('Enter Amount:'))
                            if money < balancenew:
                                balancenew -= money
                                balanceSteve += money
                                print money, 'has been transferred to steves account'
                                print 'Your current balance is', balancenew
                                newa()
                            elif money > balancenew:
                                print 'Insufficient funds.'
                                newa()
                            else:
                                print 'Unknown command.'
                                newa()
                        elif who == 'obama' or who == 'Obama':
                            print 'How much would you like to transfer to obama.'
                            money = int(raw_input('Enter Amount:'))
                            if money < balancenew:
                                balancenew -= money
                                balanceObama += money
                                print money, 'has been transferred to obamas account'
                                print 'Your current balance is', balancenew
                                newa()
                            elif money > balancenew:
                                print 'Insufficient funds.'
                                newa()
                            else:
                                print 'Unknown command.'
                                newa()
                        elif who == 'trump' or who == 'Trump':
                            print 'How much would you like to transfer to trump.'
                            money = int(raw_input('Enter Amount:'))
                            if money < balancenew:
                                balancenew -= money
                                balanceTrump += money
                                print money, 'has been transferred to trumps account'
                                print 'Your current balance is', balancenew
                                newa()
                            elif money > balancenew:
                                print 'Insufficient funds.'
                                newa()
                            else:
                                print 'Unknown command.'
                                newa()
                    elif action == 'exit' or action == 'Exit':
                        atm()
                    else:
                        print 'Unknown Command'
                        newa()  
                newa()  
                
            elif deposit <= 0:
                print 'You cant do this, we need to restart now.'
                new()
            else:
                print 'Unknown command, restarting'
                new() 
        
    def old():   
        global attempts, balanceJack, balanceSatan, balanceSnoop, balanceLandfried, balanceSteve, balanceObama, balanceTrump
        attempts = 5
        def meme():
            global attempts, balanceJack, balanceSatan, balanceSnoop, balanceLandfried, balanceSteve, balanceObama, balanceTrump
            while attempts > 0: 
                accountNumber = raw_input('Enter your 3 digit pin code:')
                if int(accountNumber) == 123:
                    print 'Welcome Jack Trudeau'
                    def Jack():
                        global balanceJack, balanceSatan, balanceSnoop, balanceLandfried, balanceSteve, balanceObama, balanceTrump
                        options()
                        
                        action = raw_input('Jack: ')
                        if action == "balance":
                            print 'Your total balance is $', balanceJack 
                            Jack()
                        elif action == 'withdraw':
                            print 'How much would you like to withdraw'
                            withdraw = int(raw_input("Withdraw: "))
                            if withdraw > balanceJack:
                                print 'you do not have the required funds'
                                Jack()
                            else:
                                balanceJack -= withdraw
                                print 'Current balance $', balanceJack
                                Jack()
                        elif action == 'deposit':
                            print 'How much would you like to deposit'
                            deposit = int(raw_input("Deposit: "))
                            balanceJack += deposit
                            print 'Current balance $', balanceJack
                            Jack()
                        elif action == 'transfer':
                            print 'Who would you like to transfer funds to?'
                            who = raw_input('Account Name:')
                            if who == 'satan' or who == 'Satan':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceJack:
                                    print 'You do not have enough money for this transfer.'
                                    Jack()
                                elif money < 0:
                                    inv()
                                    Jack()
                                else:
                                    balanceJack -= money
                                    balanceSatan += money
                                    print 'You have sent', money, 'to satan.'
                                    print 'Your balance is', balanceJack
                                    Jack()
                            elif who == 'snoop' or who == 'Snoop':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceJack:
                                    print 'You do not have enough money for this transfer.'
                                    Jack()
                                elif money < 0:
                                    inv()
                                    Jack()
                                else:
                                    balanceJack -= money
                                    balanceSnoop += money
                                    print 'You have sent', money, 'to snoop.'
                                    print 'Your balance is', balanceJack
                                    Jack()
                            elif who == 'landfried' or who == 'Landfried':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceLandfried:
                                    print 'You do not have enough money for this transfer.'
                                    Jack()
                                elif money < 0:
                                    inv()
                                    Jack()
                                else:
                                    balanceJack -= money
                                    balanceLandfried += money
                                    print 'You have sent', money, 'to Landfried.'
                                    print 'Your balance is', balanceJack
                                    Jack()
                            elif who == 'steve' or who == 'Steve':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceJack:
                                    print 'You do not have enough money for this transfer.'
                                    Jack()
                                elif money < 0:
                                    inv()
                                    Jack()
                                else:
                                    balanceJack -= money
                                    balanceSteve += money
                                    print 'You have sent', money, 'to Steve.'
                                    print 'Your balance is', balanceJack
                                    Jack()
                            elif who == 'obama' or who == 'Obama':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceJack:
                                    print 'You do not have enough money for this transfer.'
                                    Jack()
                                elif money < 0:
                                    inv()
                                    Jack()
                                else:
                                    balanceJack -= money
                                    balanceObama += money
                                    print 'You have sent', money, 'to obama.'
                                    print 'Your balance is', balanceJack
                                    Jack() 
                            elif who == 'trump' or who == 'Trump':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceJack:
                                    print 'You do not have enough money for this transfer.'
                                    Jack()
                                elif money < 0:
                                    inv()
                                    Jack()
                                else:
                                    balanceJack -= money
                                    balanceTrump += money
                                    print 'You have sent', money, 'to trump.'
                                    print 'Your balance is', balanceJack
                                    Jack()  
                        elif action == 'exit':
                            atm()
                        else: 
                            print 'command not recognized'
                            Jack()
                    Jack()
                    
                elif int(accountNumber) == 666:
                    print 'Welcome Satan'
                    def Satan():
                        global balanceJack, balanceSatan, balanceSnoop, balanceLandfried, balanceSteve, balanceObama, balanceTrump
                        options()
                        
                        action = raw_input('Satan: ')
                        if action == "balance":
                            print 'Your total balance is $', balanceSatan 
                            Satan()
                        elif action == 'withdraw':
                            print 'How much would you like to withdraw'
                            withdraw = int(raw_input("Withdraw: "))
                            if withdraw > balanceSatan:
                                print 'you do not have the required funds'
                                Satan()
                            else:
                                balanceSatan -= withdraw
                                print 'Current balance $', balanceSatan
                                Satan()
                        elif action == 'deposit':
                            print 'How much would you like to deposit'
                            deposit = int(raw_input("Deposit: "))
                            balanceSatan += deposit
                            print 'Current balance $', balanceSatan
                            Satan()
                        elif action == 'transfer':
                            print 'Who would you like to transfer funds to?'
                            who = raw_input('Account Name:')
                            if who == 'jack' or who == 'Jack':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceSatan:
                                    print 'You do not have enough money for this transfer.'
                                    Satan()
                                elif money < 0:
                                    inv()
                                    Satan()
                                else:
                                    balanceSatan -= money
                                    balanceJack += money
                                    print 'You have sent', money, 'to jack.'
                                    print 'Your balance is', balanceSatan
                                    Satan()
                            elif who == 'snoop' or who == 'Snoop':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceSatan:
                                    print 'You do not have enough money for this transfer.'
                                    Satan()
                                elif money < 0:
                                    inv()
                                    Satan()
                                else:
                                    balanceSatan -= money
                                    balanceSnoop += money
                                    print 'You have sent', money, 'to snoop.'
                                    print 'Your balance is', balanceSatan
                                    Satan()
                            elif who == 'landfried' or who == 'Landfried':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceLandfried:
                                    print 'You do not have enough money for this transfer.'
                                    Satan()
                                elif money < 0:
                                    inv()
                                    Satan()
                                else:
                                    balanceSatan -= money
                                    balanceLandfried += money
                                    print 'You have sent', money, 'to Landfried.'
                                    print 'Your balance is', balanceSatan
                                    Satan()
                            elif who == 'steve' or who == 'Steve':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceSatan:
                                    print 'You do not have enough money for this transfer.'
                                    Satan()
                                elif money < 0:
                                    inv()
                                    Satan()
                                else:
                                    balanceSatan -= money
                                    balanceSteve += money
                                    print 'You have sent', money, 'to Steve.'
                                    print 'Your balance is', balanceSatan
                                    Satan()
                            elif who == 'obama' or who == 'Obama':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceSatan:
                                    print 'You do not have enough money for this transfer.'
                                    Satan()
                                elif money < 0:
                                    inv()
                                    Satan()
                                else:
                                    balanceSatan -= money
                                    balanceObama += money
                                    print 'You have sent', money, 'to obama.'
                                    print 'Your balance is', balanceSatan
                                    Satan() 
                            elif who == 'trump' or who == 'Trump':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceSatan:
                                    print 'You do not have enough money for this transfer.'
                                    Satan()
                                elif money < 0:
                                    inv()
                                    Satan()
                                else:
                                    balanceSatan -= money
                                    balanceTrump += money
                                    print 'You have sent', money, 'to trump.'
                                    print 'Your balance is', balanceSatan
                                    Satan()
                        elif action == 'exit':
                            atm()
                        else: 
                            print 'command not recognized'
                            Satan()
                    Satan()
                    
                elif int(accountNumber) == 220:
                    print 'Welcome Snoop Dogg'
                    def Snoop():
                        global balanceJack, balanceSatan, balanceSnoop, balanceLandfried, balanceSteve, balanceObama, balanceTrump
                        options()
                        
                        action = raw_input('Snoop: ')
                        if action == "balance":
                            print 'Your total balance is $', balanceSnoop 
                            Snoop()
                        elif action == 'withdraw':
                            print 'How much would you like to withdraw'
                            withdraw = int(raw_input("Withdraw: "))
                            if withdraw > balanceSnoop:
                                print 'you do not have the required funds'
                                Snoop()
                            else:
                                balanceSnoop -= withdraw
                                print 'Current balance $', balanceSnoop
                                Snoop()
                        elif action == 'deposit':
                            print 'How much would you like to deposit'
                            deposit = int(raw_input("Deposit: "))
                            balanceSnoop += deposit
                            print 'Current balance $', balanceSnoop
                            Snoop()
                        elif action == 'transfer':
                            print 'Who would you like to transfer funds to?'
                            who = raw_input('Account Name:')
                            if who == 'satan' or who == 'Satan':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceSnoop:
                                    print 'You do not have enough money for this transfer.'
                                    Snoop()
                                elif money < 0:
                                    inv()
                                    Snoop()
                                else:
                                    balanceSnoop -= money
                                    balanceSatan += money
                                    print 'You have sent', money, 'to satan.'
                                    print 'Your balance is', balanceSnoop
                                    Snoop()
                            elif who == 'jack' or who == 'Jack':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceSnoop:
                                    print 'You do not have enough money for this transfer.'
                                    Snoop()
                                elif money < 0:
                                    inv()
                                    Snoop()
                                else:
                                    balanceSnoop -= money
                                    balanceJack += money
                                    print 'You have sent', money, 'to jack.'
                                    print 'Your balance is', balanceSnoop
                                    Snoop()
                            elif who == 'landfried' or who == 'Landfried':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceLandfried:
                                    print 'You do not have enough money for this transfer.'
                                    Snoop()
                                elif money < 0:
                                    inv()
                                    Snoop()
                                else:
                                    balanceSnoop -= money
                                    balanceLandfried += money
                                    print 'You have sent', money, 'to Landfried.'
                                    print 'Your balance is', balanceSnoop
                                    Snoop()
                            elif who == 'steve' or who == 'Steve':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceJack:
                                    print 'You do not have enough money for this transfer.'
                                    Snoop()
                                elif money < 0:
                                    inv()
                                    Snoop()
                                else:
                                    balanceSnoop -= money
                                    balanceSteve += money
                                    print 'You have sent', money, 'to Steve.'
                                    print 'Your balance is', balanceSnoop
                                    Snoop()
                            elif who == 'obama' or who == 'Obama':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceSnoop:
                                    print 'You do not have enough money for this transfer.'
                                    Snoop()
                                elif money < 0:
                                    inv()
                                    Snoop()
                                else:
                                    balanceSnoop -= money
                                    balanceObama += money
                                    print 'You have sent', money, 'to obama.'
                                    print 'Your balance is', balanceSnoop
                                    Snoop() 
                            elif who == 'trump' or who == 'Trump':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceSnoop:
                                    print 'You do not have enough money for this transfer.'
                                    Snoop()
                                elif money < 0:
                                    inv()
                                    Snoop()
                                else:
                                    balanceSnoop -= money
                                    balanceTrump += money
                                    print 'You have sent', money, 'to trump.'
                                    print 'Your balance is', balanceSnoop
                                    Snoop()
                        elif action == 'exit':
                            atm()
                        else: 
                            print 'command not recognized'
                            Snoop()
                    Snoop()
                    
                elif int(accountNumber) == 321:
                    print 'Welcome Landfried'
                    def Landfried():
                        global balanceJack, balanceSatan, balanceSnoop, balanceLandfried, balanceSteve, balanceObama, balanceTrump
                        options()
                        
                        action = raw_input('Landfried: ')
                        if action == "balance":
                            print 'Your total balance is $', balanceLandfried
                            Landfried()
                        elif action == 'withdraw':
                            print 'How much would you like to withdraw'
                            withdraw = int(raw_input("Withdraw: "))
                            if withdraw > balanceLandfried:
                                print 'you do not have the required funds'
                                Landfried()
                            else:
                                balanceLandfried -= withdraw
                                print 'Current balance $', balanceLandfried
                                Landfried()
                        elif action == 'deposit':
                            print 'How much would you like to deposit'
                            deposit = int(raw_input("Deposit: "))
                            balanceLandfried += deposit
                            print 'Current balance $', balanceLandfried
                            Snoop()
                        elif action == 'transfer':
                            print 'Who would you like to transfer funds to?'
                            who = raw_input('Account Name:')
                            if who == 'satan' or who == 'Satan':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceLandfried:
                                    print 'You do not have enough money for this transfer.'
                                    Landfried()
                                elif money < 0:
                                    inv()
                                    Landfried()
                                else:
                                    balanceLandfried -= money
                                    balanceSatan += money
                                    print 'You have sent', money, 'to satan.'
                                    print 'Your balance is', balanceLandfried
                                    Landfried()
                            elif who == 'snoop' or who == 'Snoop':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceLandfried:
                                    print 'You do not have enough money for this transfer.'
                                    Landfried()
                                elif money < 0:
                                    inv()
                                    Landfried()
                                else:
                                    balanceLandfried -= money
                                    balanceSnoop += money
                                    print 'You have sent', money, 'to snoop.'
                                    print 'Your balance is', balanceLandfried
                                    Landfried()
                            elif who == 'jack' or who == 'Jack':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceLandfried:
                                    print 'You do not have enough money for this transfer.'
                                    Landfried()
                                elif money < 0:
                                    inv()
                                    Landfried()
                                else:
                                    balanceLandfried -= money
                                    balanceJack += money
                                    print 'You have sent', money, 'to jack.'
                                    print 'Your balance is', balanceLandfried
                                    Landfried()
                            elif who == 'steve' or who == 'Steve':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceJack:
                                    print 'You do not have enough money for this transfer.'
                                    Jack()
                                elif money < 0:
                                    inv()
                                    Jack()
                                else:
                                    balanceJack -= money
                                    balanceSteve += money
                                    print 'You have sent', money, 'to Steve.'
                                    print 'Your balance is', balanceJack
                                    Jack()
                            elif who == 'obama' or who == 'Obama':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceJack:
                                    print 'You do not have enough money for this transfer.'
                                    Jack()
                                elif money < 0:
                                    inv()
                                    Jack()
                                else:
                                    balanceJack -= money
                                    balanceObama += money
                                    print 'You have sent', money, 'to obama.'
                                    print 'Your balance is', balanceJack
                                    Jack() 
                            elif who == 'trump' or who == 'Trump':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceJack:
                                    print 'You do not have enough money for this transfer.'
                                    Jack()
                                elif money < 0:
                                    inv()
                                    Jack()
                                else:
                                    balanceJack -= money
                                    balanceTrump += money
                                    print 'You have sent', money, 'to trump.'
                                    print 'Your balance is', balanceJack
                                    Jack()  
                        elif action == 'exit':
                            atm()
                        else: 
                            print 'command not recognized'
                            Landfried()
                    Landfried()
                    
                elif int(accountNumber) == 222:
                    print 'Welcome Steve Buschemi'
                    def Steve():
                        global balanceJack, balanceSatan, balanceSnoop, balanceLandfried, balanceSteve, balanceObama, balanceTrump
                        options()
                        
                        action = raw_input('Steve: ')
                        if action == "balance":
                            print 'Your total balance is $', balanceSteve
                            Steve()
                        elif action == 'withdraw':
                            print 'How much would you like to withdraw'
                            withdraw = int(raw_input("Withdraw: "))
                            if withdraw > balanceSteve:
                                print 'you do not have the required funds'
                                Steve()
                            else:
                                balanceSteve -= withdraw
                                print 'Current balance $', balanceSteve
                                Steve()
                        elif action == 'deposit':
                            print 'How much would you like to deposit'
                            deposit = int(raw_input("Deposit: "))
                            balanceSteve += deposit
                            print 'Current balance $', balanceSteve
                            Steve()
                        elif action == 'transfer':
                            print 'Who would you like to transfer funds to?'
                            who = raw_input('Account Name:')
                            if who == 'jack' or who == 'Jack':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceSteve:
                                    print 'You do not have enough money for this transfer.'
                                    Steve()
                                elif money < 0:
                                    inv()
                                    Steve()
                                else:
                                    balanceSteve -= money
                                    balanceSatan += money
                                    print 'You have sent', money, 'to satan.'
                                    print 'Your balance is', balanceSteve
                                    Steve()
                            elif who == 'snoop' or who == 'Snoop':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceSteve:
                                    print 'You do not have enough money for this transfer.'
                                    Steve()
                                elif money < 0:
                                    inv()
                                    Steve()
                                else:
                                    balanceSteve -= money
                                    balanceSnoop += money
                                    print 'You have sent', money, 'to snoop.'
                                    print 'Your balance is', balanceSteve
                                    Steve()
                            elif who == 'landfried' or who == 'Landfried':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceLandfried:
                                    print 'You do not have enough money for this transfer.'
                                    Steve()
                                elif money < 0:
                                    inv()
                                    Steve()
                                else:
                                    balanceSteve -= money
                                    balanceLandfried += money
                                    print 'You have sent', money, 'to Landfried.'
                                    print 'Your balance is', balanceSteve
                                    Steve()
                            elif who == 'steve' or who == 'Steve':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceSteve:
                                    print 'You do not have enough money for this transfer.'
                                    Steve()
                                elif money < 0:
                                    inv()
                                    Steve()
                                else:
                                    balanceSteve -= money
                                    balanceJack += money
                                    print 'You have sent', money, 'to Jack.'
                                    print 'Your balance is', balanceSteve
                                    Steve()
                            elif who == 'obama' or who == 'Obama':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceSteve:
                                    print 'You do not have enough money for this transfer.'
                                    Steve()
                                elif money < 0:
                                    inv()
                                    Steve()
                                else:
                                    balanceSteve -= money
                                    balanceObama += money
                                    print 'You have sent', money, 'to obama.'
                                    print 'Your balance is', balanceSteve
                                    Steve() 
                            elif who == 'trump' or who == 'Trump':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceSteve:
                                    print 'You do not have enough money for this transfer.'
                                    Steve()
                                elif money < 0:
                                    inv()
                                    Steve()
                                else:
                                    balanceSteve -= money
                                    balanceTrump += money
                                    print 'You have sent', money, 'to trump.'
                                    print 'Your balance is', balanceSteve
                                    Steve()  
                        elif action == 'exit':
                            atm()
                        else: 
                            print 'command not recognized'
                            Steve()
                    Steve()
                    
                elif int(accountNumber) == 111:
                    print 'Welcome Barack Obama'
                    def Obama():
                        global balanceJack, balanceSatan, balanceSnoop, balanceLandfried, balanceSteve, balanceObama, balanceTrump
                        options()
                        
                        action = raw_input('Obama: ')
                        if action == "balance":
                            print 'Your total balance is $', balanceObama
                            Obama()
                        elif action == 'withdraw':
                            print 'How much would you like to withdraw'
                            withdraw = int(raw_input("Withdraw: "))
                            if withdraw > balanceObama:
                                print 'you do not have the required funds'
                                Obama()
                            else:
                                balanceObama -= withdraw
                                print 'Current balance $', balanceObama
                                Obama()
                        elif action == 'deposit':
                            print 'How much would you like to deposit'
                            deposit = int(raw_input("Deposit: "))
                            balanceObama += deposit
                            print 'Current balance $', balanceObama
                            Obama()
                        elif action == 'transfer':
                            print 'Who would you like to transfer funds to?'
                            who = raw_input('Account Name:')
                            if who == 'satan' or who == 'Satan':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceObama:
                                    print 'You do not have enough money for this transfer.'
                                    Obama()
                                elif money < 0:
                                    inv()
                                    Obama()
                                else:
                                    balanceObama -= money
                                    balanceSatan += money
                                    print 'You have sent', money, 'to satan.'
                                    print 'Your balance is', balanceObama
                                    Obama()
                            elif who == 'snoop' or who == 'Snoop':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceObama:
                                    print 'You do not have enough money for this transfer.'
                                    Obama()
                                elif money < 0:
                                    inv()
                                    Obama()
                                else:
                                    balanceObama -= money
                                    balanceSnoop += money
                                    print 'You have sent', money, 'to snoop.'
                                    print 'Your balance is', balanceObama
                                    Obama()
                            elif who == 'landfried' or who == 'Landfried':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceLandfried:
                                    print 'You do not have enough money for this transfer.'
                                    Obama()
                                elif money < 0:
                                    inv()
                                    Obama()
                                else:
                                    balanceObama -= money
                                    balanceLandfried += money
                                    print 'You have sent', money, 'to Landfried.'
                                    print 'Your balance is', balanceObama
                                    Obama()
                            elif who == 'steve' or who == 'Steve':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceObama:
                                    print 'You do not have enough money for this transfer.'
                                    Obama()
                                elif money < 0:
                                    inv()
                                    Obama()
                                else:
                                    balanceObama -= money
                                    balanceSteve += money
                                    print 'You have sent', money, 'to Steve.'
                                    print 'Your balance is', balanceObama
                                    Obama()
                            elif who == 'jack' or who == 'Jack':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceObama:
                                    print 'You do not have enough money for this transfer.'
                                    Obama()
                                elif money < 0:
                                    inv()
                                    Obama()
                                else:
                                    balanceObama -= money
                                    balanceJack += money
                                    print 'You have sent', money, 'to Jack.'
                                    print 'Your balance is', balanceObama
                                    Obama() 
                            elif who == 'trump' or who == 'Trump':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceObama:
                                    print 'You do not have enough money for this transfer.'
                                    Obama()
                                elif money < 0:
                                    inv()
                                    Obama()
                                else:
                                    balanceObama -= money
                                    balanceTrump += money
                                    print 'You have sent', money, 'to trump.'
                                    print 'Your balance is', balanceObama
                                    Obama()  
                        elif action == 'exit':
                            atm()
                        else: 
                            print 'command not recognized'
                            Obama()
                    Obama()
                    
                elif accountNumber == "0iq":
                    print 'Welcome Donald Trump'
                    def Trump():
                        global balanceJack, balanceSatan, balanceSnoop, balanceLandfried, balanceSteve, balanceObama, balanceTrump
                        options()
                        
                        action = raw_input('Donald: ')
                        if action == "balance":
                            print 'Your total balance is $', balanceTrump 
                            Trump()
                        elif action == 'withdraw':
                            print 'How much would you like to withdraw'
                            withdraw = int(raw_input("Withdraw: "))
                            if withdraw > balanceTrump:
                                print 'you do not have the required funds'
                                Trump()
                            else:
                                balanceTrump -= withdraw
                                print 'Current balance $', balanceTrump
                                Trump()
                        elif action == 'deposit':
                            print 'How much would you like to deposit'
                            deposit = int(raw_input("Deposit: "))
                            balanceTrump += deposit
                            print 'Current balance $', balanceTrump
                            Trump()
                        elif action == 'transfer':
                            print 'Who would you like to transfer funds to?'
                            who = raw_input('Account Name:')
                            if who == 'satan' or who == 'Satan':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceTrump:
                                    print 'You do not have enough money for this transfer.'
                                    Trump()
                                elif money < 0:
                                    inv()
                                    Trump()
                                else:
                                    balanceTrump -= money
                                    balanceSatan += money
                                    print 'You have sent', money, 'to satan.'
                                    print 'Your balance is', balanceTrump
                                    Trump()
                            elif who == 'snoop' or who == 'Snoop':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceTrump:
                                    print 'You do not have enough money for this transfer.'
                                    Trump()
                                elif money < 0:
                                    inv()
                                    Trump()
                                else:
                                    balanceTrump -= money
                                    balanceSnoop += money
                                    print 'You have sent', money, 'to snoop.'
                                    print 'Your balance is', balanceTrump
                                    Trump()
                            elif who == 'landfried' or who == 'Landfried':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceLandfried:
                                    print 'You do not have enough money for this transfer.'
                                    Trump()
                                elif money < 0:
                                    inv()
                                    Trump()
                                else:
                                    balanceTrump -= money
                                    balanceLandfried += money
                                    print 'You have sent', money, 'to Landfried.'
                                    print 'Your balance is', balanceTrump
                                    Trump()
                            elif who == 'steve' or who == 'Steve':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceTrump:
                                    print 'You do not have enough money for this transfer.'
                                    Trump()
                                elif money < 0:
                                    inv()
                                    Trump()
                                else:
                                    balanceTrump -= money
                                    balanceSteve += money
                                    print 'You have sent', money, 'to Steve.'
                                    print 'Your balance is', balanceTrump
                                    Trump()
                            elif who == 'obama' or who == 'Obama':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceTrump:
                                    print 'You do not have enough money for this transfer.'
                                    Trump()
                                elif money < 0:
                                    inv()
                                    Trump()
                                else:
                                    balanceTrump -= money
                                    balanceObama += money
                                    print 'You have sent', money, 'to obama.'
                                    print 'Your balance is', balanceTrump
                                    Jack() 
                            elif who == 'jack' or who == 'Jack':
                                print 'How much money would you like to transfer?'
                                money = int(raw_input('Enter Amount:'))
                                if money > balanceTrump:
                                    print 'You do not have enough money for this transfer.'
                                    Trump()
                                elif money < 0:
                                    inv()
                                    Trump()
                                else:
                                    balanceTrump -= money
                                    balanceJack += money
                                    print 'You have sent', money, 'to Jack.'
                                    print 'Your balance is', balanceTrump
                                    Trump()  
                        elif action == 'exit':
                            atm()
                        else: 
                            print 'command not recognized'
                            Trump()
                    Trump()
                    
                else:
                    attempts -= 1
                    print 'Wrong pin code', attempts, 'attempts remaining.'
                    meme()
            print 'Sorry, you are locked out of this atm, Too many wrong pin codes, try again in 30 seconds.'
            time.sleep(30)
            old()
        meme()
    print 'Welcome to this ATM'
    print 'Type \'old\' if you already have an account or type \'new\' to make a new account'
    oldornew = raw_input('Old or New:')
    if oldornew == 'Old' or oldornew == 'old':
        old()
    elif oldornew == 'New' or oldornew == 'new':
        new()
    elif oldornew == 'exit' or oldornew == 'e':
        print 'k'
    else:
        print 'Unknown command'
        atm()
