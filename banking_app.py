# BANKING PROJECT.............

accounts={}

def AccountCreation():
    Username = input('Enter new name : ')
    account_number = int(input('New account number is : '))
    InitialBalance = int(input('Enter the initial balance : '))


    if account_number in accounts:
         print("Account Number Exists!")
         return

    accounts[account_number]={
         'holdername':Username,
         'balance':InitialBalance,
         'transactions':[]
    }

def DepositMoney():
    account_number = int(input('Account number is : '))
    Deposit_Money = float(input('How much deposit : '))

    accounts[account_number]['balance']+=Deposit_Money
    accounts[account_number]['transactions'].append(f'deposit money {Deposit_Money}')



def WithdrawMoney():
    account_number = int(input('Account number is : '))
    Withdraw_Money = float(input('How much do you withdraw'))

    accounts[account_number]['balance']-=Withdraw_Money
    accounts[account_number]['transactions'].append(f'Withdraw Money {Withdraw_Money}')

def CheckBalance():
    account_number = int(input('Account number is : '))
    
    if account_number in accounts:
         print("Balance:",accounts[account_number]['balance'])

def TransactionHistory():
     account_number = int(input('Account number is : '))

     if account_number in accounts:
          for transactions in accounts[account_number]['transactions']:
               print(transactions)
    
while True:  
    print('-----------user menu-------------') 
    print('1. Create Account \n'
        '2. Deposit Money \n'
        '3. Withdraw Money \n'
        '4. Check Balance \n'
        '5. Transaction History \n'
        '6. Exit')
    
    choice=int(input('Please select option :' ))

    if choice==1:
            AccountCreation() 

    elif choice==2:
            DepositMoney()
    
    elif choice==3:
        WithdrawMoney()

    elif choice==4:
        CheckBalance()

    elif choice==5:
        TransactionHistory()

    elif choice==6:
        break

    else:
         print("Invalid Choice!")
         break


