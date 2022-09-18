#create a basic banking application with the following feature


class BankAccount  :
    def __init__(self,account_number,balance,owner,type) :
        self.account_number=account_number
        self.balance=balance
        self.owner=owner
        self.type=type
    def __repr__(self):
        return f"<BankAccount {self.account_number} {self.balance} {self.owner} {self.type}> "
BankAccount=BankAccount("account 1",1220.34,"GLORIA","savings")
print(BankAccount.account_number)
print(BankAccount.balance)
print(BankAccount.owner)
print(BankAccount.type)

print(BankAccount)


#create a class called bank with the following attributes
class Bank :
    def __init__(self,name,account_number,balance,owner,type) :
        self.name=name
        self.account_number=account_number
        self.balance=balance
        self.owner=owner
        self.type=type
list =[]
list.append(Bank("stanbic","account 2",30000.0,"gloria","savings"))

for obj in list:
    print(obj.name,obj.account_number,obj.balance,obj.owner,obj.type) 
#create a class called customer with the following attributes
class Customer :
    def __init__(self,name,account_number,balance,owner,type) :
        self.name=name
        self.account_number=account_number
        self.balance=balance
        self.owner=owner
        self.type=type
list =[]
list.append(Customer("centenary","account 3",40000.0,"gloria","fixed"))

for obj in list:
    print(obj.name,obj.account_number,obj.balance,obj.owner,obj.type) 


#create a class called transactions with the following attributes
class Transactions:
    def __init__(self,account,amount,type) :
        self.account=account
        self.amount=amount
        self.type= type
    def __repr__(self):
        return f"<Transactions {self.account} {self.amount} {self.type}> "
Transactions=Transactions("account 4",344220.34,"fixed")
print(Transactions.account)
print(Transactions.amount)
print(Transactions.type)

print(Transactions)


#the application should have thefollowing functionality:
#create a new Bank object
class New_Bank(object):
    def __init__(self,name,account_number,balance,owner,type) :
        self.name=name
        self.account_number=account_number
        self.balance=balance
        self.owner=owner
        self.type=type 
New_Bank=New_Bank("absa","account5",23444.099,"gloria","borrowing")
print(New_Bank.name)
print(New_Bank.account_number)
print(New_Bank.balance)
print(New_Bank.owner)
print(New_Bank.type)

print(New_Bank)

#Create a new customer object
class New_Customer(object):
    def __init__(self,Customer_name,Customeraccount_number,Customer_balance,Customer_owner,Customer_type) :
        self.Customer_name=Customer_name
        self.Customeraccount_number=Customeraccount_number
        self.Customer_balance=Customer_balance
        self.Customer_owner=Customer_owner
        self.Customer_type=Customer_type
New_Customer=New_Customer("ADB","account6",26766644.099,"gloria","fixed")
print(New_Customer.Customer_name)
print(New_Customer.Customeraccount_number)
print(New_Customer.Customer_balance)
print(New_Customer.Customer_owner)
print(New_Customer.Customer_type)

print(New_Customer)
#create a new BankAccount
class New_BankAccount(object)  :
    def __init__(self,Newaccount_number,New_balance,New_owner,New_type) :
        self.Newaccount_number=Newaccount_number
        self.New_balance=New_balance
        self.New_owner=New_owner
        self.New_type=New_type
    def __repr__(self):
        return f"<New_BankAccount {self.Newaccount_number} {self.New_balance} {self.New_owner} {self.New_type}> "
New_BankAccount=New_BankAccount("account 7",1220099990.34,"GLORIA","faker")
print(New_BankAccount.Newaccount_number)
print(New_BankAccount.New_balance)
print(New_BankAccount.New_owner)
print(New_BankAccount.New_type)

print(New_BankAccount)

#add the bankaccount to the bank object
class BankAccount  :
    def __init__(self,account_number,balance,owner,type) :
        self.account_number=account_number
        self.balance=balance
        self.owner=owner
        self.type=type
class Bank(object):
    def __init__(self,name,account_number,balance,owner,type) :
        self.name=name
        self.account_number=account_number
        self.balance=balance
        self.owner=owner
        self.type=type
        self.BankAccount=[]

    def add_BankAccount(B):
        self.BankAccount.append(B)  
    def __repr__(self):
        return f"<Bank{self.name} {self.account_number} {self.balance} {self.owner} {self.type}> "
Bank=Bank("DFCU","account 8",1220988.34,"GLORIA","savings")
print(Bank.name)
print(Bank.account_number)
print(Bank.balance)
print(Bank.owner)
print(Bank.type)
       
print(Bank)  
print(BankAccount)      

class New_transaction:
    def __init__(self,New_account,New_amount,New_type) :
        self.New_account=New_account
        self.New_amount=New_amount
        self.New_type= New_type
    def __repr__(self):
        return f"<Transactions {self.New_account} {self.New_amount} {self.New_type}> "
New_transaction=New_transaction("account 9",3442253450.34,"fixed")
print(New_transaction.New_account)
print(New_transaction.New_amount)
print(New_transaction.New_type)

print(New_transaction)

    



        



    


        
        

    
    