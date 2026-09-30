# ATM Machine Simulation using Python
s=("Welcome to My Profile,Saurabh")
print(s)

balence = 1000

def balence_check():
   global balence
   print("Your Current balence is :",balence)
   
def deposite():
    global balence
    amt=int (input("Enter your deposite amount :"))
    balence +=amt
    print("your amt is succesfully deposite")
    print("your current balence is :",balence)
    
def widral():
    global  balence 
    amt=int(input("Enter your widrol amount : "))
    balence -=amt    
    if amt>=balence:
        print("Sorry Inuff balence")
    print("your amt is succesfully widrol")
    print("Your Current Balence is :",balence)
    
while True:
    print(" *** ATM Menu ***")
    print(" 1. balence check")
    print(" 2. deposite")
    print(" 3. widrol")  
    print(" 4.exit")
     
    choose= int(input("Enter the choise : "))
     
    if choose==1:
        balence_check()
    elif choose==2:
        deposite()
    elif choose==3:
        widral()
    elif choose==4:
        print("Thank you for choosing this ATM")
    
    else:
        print("Enter the valid number")
                       
                  
