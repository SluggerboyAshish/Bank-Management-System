import pickle

print("_"*40)
print("********************BANK MANAGMENT SYSTEM********************")
print("_"*40)
l1=["Name","Address","PhoneNo.",'GovtId',"AccType","Amount"]
l2=[]       # USed for making the dictionary
mydic={}
bank={}         # nested Dictionary  

# Error handling used for Loading the data from file to dictionary bank{} if empty will give error

try:
    obj1=open("data.dat","rb")
    output=pickle.load(obj1)
    bank=output
except EOFError:
    print("File is Empty")

def new():
    #Error handling for file not found
    try:
        obj=open("data.dat","rb")
        file_data=pickle.load(obj) # load the data 
        account=int(input("Enter the Account "))   # account number used as keys
        if account in bank.keys():  #As two person cannot have the same acccount number logic for this
            print("Account Already exists")
        else:
            for x in l1:        # used for entering the data in the list and making the dict
                i=input(f"Enter {x} ")
                l2.append(i)
            mydic=dict(zip(l1,l2)) #making dictionary using zip() and dict()
            print(mydic)
            bank[account]=mydic     # this will take the account as key and my      
            obj=open("data.dat","wb")
            pickle.dump(bank,obj)
            obj.close()
            l2.clear()
            print( "ACCOUNT CREATED ")
            print("-"*50)
    #Error handling for file not found
    except FileNotFoundError:   # this will create the file in the directory
        print("File Not Found")
        obj=open("data.dat","wb")
        print("Now File is created")

def Ex():
    # obj=open("data.dat","rb")
    # res=pickle.load(obj)          #This is used to show the dict data or file data
    # for key in res:
    #     print(key,"-->",res[key])
    # obj.close()
    acc=int(input("Enter the account Number ")) # take the input of account number
    
    
    
    def check():
        print(f"Your account Bank Balance is {bank[acc]['Amount']} ")    #check the bank balance
    
    def withdraw():
        wit=int(input("Enter amount to withdraw: "))
        bank[acc]['Amount']=int(bank[acc]['Amount'])-wit            # this Will perform operation of deposit
        print("-"*40)                                       
        print("Withdraw Successful ")
        print("Available Balance :",bank[acc]['Amount'])                
        print("-"*40)
        obj=open("data.dat","wb")                    # this will write the data in the file
        pickle.dump(bank,obj)
        obj.close()
   
    
    def deposit():
        dep=int(input("Enter amount to withdraw: "))
        bank[acc]['Amount']=int(bank[acc]['Amount'])+dep
        print("-"*40)
        print("Deposit Successful ")
        print("Available Balance :",bank[acc]['Amount'])         #same as
        print("-"*40)
        obj=open("data.dat","wb")
        pickle.dump(bank,obj)
        obj.close()

    
    if acc in bank.keys():#  logic if account exist then perform these function
        cha=input("Record Found \n1. Check Balance \n2. Withdraw \n3. Deposit \nEnter the choice : ")
        if cha=="1":
            check()
        elif cha=="2":
            withdraw()
        elif cha=="3":
            deposit()
        else:
            ("Wrong Choice ")
    else:
        print("Account Number Not Found")



while(True):
    choice=int(input("1. New Customer \n2. Existing Customer \n3. Exit \nEnter the choice "))
    if choice==1:
        new()
    elif choice==2:
        Ex()
    elif choice==3:
        break 
    else:
        print("Wrong Input")