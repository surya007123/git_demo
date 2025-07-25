# ATM MACHINE TASK
from datetime import datetime
now=datetime.now()
balance=0
Transaction=[] #[]--->for empty list
pin=2003
while True:
    print('ATM')
    print('WELCOME TO ATM')
    print('INSERT CARD HERE---->')
    # print('enter the pin:')
    # card_pin=int(input())        
    a=int(input('0-NO,1-yes'))
    if a==1:
        print('1:DEPOSIT    2:WITHDRAW    3:BALANCE_CHECK    4:PIN_CHANGE    5:EXIT')
        option=int(input('select any one option above'))
        if option ==1:
            print('enter the pin:')
            pinNumber=int(input())
            print('enter the amount to be deposited')
            amount=int(input())
            if amount%100==0:
                print('cash had been accepted')
                balance += amount
                Transaction.append(amount)
            else:
                print('please provide multiples of 100')
            print('balance=',balance)
        elif option==2:
            print('enter the amount to be withdraw')
            amount=int(input())
            if amount<=balance:
                balance-=amount
                print('please wait.......')
                print('collect the amount')
                Transaction.append(-amount)
                    
            elif amount%100 !=0:
                print('entered amount should be multiple of 100')
                     
            else:
                print('insufficient funds :(')
        elif option==3:
            print('*********STATE BANK OF INDIA**********')
            date=now.date()
            time=now.time()
            print(f"date:{date} \t time:{time}")
            for i in Transaction:
                print('Transaction:',i)      
            print('Balance:',balance)
            print('*************************************')        
        elif option==4:
            #global pin
            print('enter the new pin')
            new_pin=int(input())
            if new_pin == pin:
                print('entered pin is old pin')
            else:
                print('re-enter the new pin')
                re_enter=int(input())
                print('confirm the pin')
                confirm=int(input()) 
                
            pin=new_pin
            print('the new pin is:',pin)
        elif option==5:
            break
                
                    
                    
                
            