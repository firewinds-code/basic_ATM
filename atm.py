print('welcome to State Bank Of India ATM ')
restart=('y')
chances = 3
balance = 67.14
while chances >= 0:
    pin = int(input(' Please enter your 4 digit pin : '))
    if pin ==(1234):
        print('you entered your pin correctly \n')
        while restart not in ('n','No','no','N'):
            print('plese press 1 for your balance \n')
            print('plese press 2 to make withdrwal \n')
            print('plese press 3 to pay in \n')
            print('plese press 4 to return card \n')
            option = int(input('what would you like to choose ? '))
            if option == 1:
                print('your balance is : ₹',balance,'\n')
                restart = input('would you like to go back ?')
                if restart in ('n','No','no','N'):
                    print('thank you')
                    break
            elif option == 2:
                    option2 = ('y')
                    withdrwal = float(input('how much would you like to withdraw ? \n₹10/₹20/₹40/₹60/₹80/₹100 for other enter 1: '))
                    if withdrwal in [10,20,40,60,80,100]:
                        balance = balance - withdrwal
                        print(' \n your balance now is : ₹',balance)
                        if restart in ('n','No','no','N'):
                            print('thank you')
                            break
                        elif withdrwal !=[10,20,40,60,80,100]:
                            print('Invalid Amount, please re-try \n')
                            restart=('y')
                        elif withdrwal ==1 :
                            withdrwal = float(input('please enter desired amount :'))
            elif option == 3:
                pay_in = float(input('how much would you like to pay in ?'))
                balance = balance + pay_in
                print('\n your balance is now ₹',balance)
                restart = input('would you like to go back?')
                if restart in ('n','No','no','N'):
                    print('thank you')
                    break
            elif option ==4:
                print('please wait whilst your card is returned.....\n')
                print('thank you for waiting')
                break
            else:
                print(' please enter a correct number \n')
                restart=('y')
    elif pin !=('1234'):
        print('Incorrect pin/ password')
        chances = chances - 1
        if chances == 0:
            print ('\n No more tries')
            break

                



                


