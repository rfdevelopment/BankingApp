print("Welcome to the Bank Of Ross Terminal App")

class bankAccount():
    
    def __init__(self, acct_num, balance):
        self.acct_num = acct_num
        self.balance = balance
        
    def get_balance(self):
        return self.balance
    
    def complete_withdrawl(self, amt):
        self.balance -= amt
    
    def complete_deposit(self, amt):
        self.balance += amt
    
    
class savingsAccount(bankAccount):
    
    def __init__(self, acct_num, balance, interest_rate):
        super().__init__(acct_num, balance)
        
        self.interest_rate = interest_rate
        
    def apply_interest(self):
        self.balance = (self.balance * (self.interest_rate + 1))

class checkingAccount(bankAccount):
    
    def __init__(self, acct_num, balance, min_balance, monthly_fee):
        super().__init__(acct_num, balance)
        
        self.min_balance = min_balance
        self.monthly_fee = monthly_fee

    #Returns true if current balance is greater or equal to the minimum balance for the account
    def meets_min_balance(self):
        if(self.balance >= self.min_balance):
            return True
        return False

    #Deduct monthly fees
    def deduct_monthly_fees(self):
        self.balance -= self.monthly_fee

#Check for float as input
def is_float(m):

    #Check for valid string to be converted to float
    try:
        m = float(m)
    except Exception:
        return -1
    
    return m

#Show current balances          
def display_balances(checking_acct, savings_acct):
    meets = True
    print("--------------------------------------")

    if(checking_acct.meets_min_balance() == False) :
        msg = "** "
        meets = False
    else:
        msg = ""
    
    msg += "Checking Account \t\t: $%.2f" % checking_acct.get_balance()
    print(msg)
        
    msg = "Savings Account \t\t: $%.2f" % savings_acct.get_balance()
    print(msg)
    
    if(meets == False):
        print("\n** Account below minimum balance\n")
        
#Select one of two accounts and return the selected
def choose_acct(checking_acct, savings_acct):
    meets = True
    cont = False
    while(cont == False):
        print("--------------------------------------")
    
        if(checking_acct.meets_min_balance() == False) :
            msg = "** "
            meets = False
        else:
            msg = ""
        
        msg += "1 - Checking Account \t\t: $%.2f" % checking_acct.get_balance()
        print(msg)
        
        msg = "2 - Savings Account \t\t: $%.2f" % savings_acct.get_balance()
        print(msg)
        
        if(meets == False):
            print("\n** Account below minimum balance\n")
        
        selection = input()
        if(selection == "1"):
            return checking_acct
        elif(selection == "2"):
            return savings_acct
        else:
            print("Invalid selection")
    
#Start Deposit Functions
def make_deposit(checking_acct, savings_acct):
    acct = choose_acct(checking_acct, savings_acct)
    cont = False
    while(cont == False):
        msg = "Amount to Deposit (in dollars) :"
        print(msg)
        dep_str = input()
        dep = is_float(dep_str)
        if(dep > 0):
            acct.complete_deposit(dep)
            cont = True
        else:
            print("Invalid Input")
        

#Start Withdrawl Functions
def make_withdrawl(checking_acct, savings_acct):
    acct = choose_acct(checking_acct, savings_acct)
    cont = False

    if(acct.balance <= 0):
        cont = True
        print("No funds available to withdraw.")

    while(cont == False):
        msg = "Amount to Withdraw (in dollars) :"
        print(msg)
        dep_str = input()
        dep = is_float(dep_str)
        if(dep > 0 and dep <= acct.balance):
            acct.complete_withdrawl(dep)
            cont = True
        else:
            print("Invalid Input")


#Charges fees and applies interest gains
def init_fees_n_interest(checking_acct, savings_acct):
    
    #Apply fees
    msg = "Deducting monthly fee from acct #%i" % checking_acct.acct_num + " - $%.2f" % checking_acct.monthly_fee
    print(msg)
    checking_acct.deduct_monthly_fees()
    
    #Apply interest gains to savings accounts
    msg = "Depositing interest gains to acct #%i" % savings_acct.acct_num + " at rate of %.2f%%\n" % (100 * savings_acct.interest_rate)
    print(msg)
    savings_acct.apply_interest()
        
checking_acct = checkingAccount(239801807, 100.00, 50.00, 5.00)
savings_acct = savingsAccount(239801801, 25.00, 0.02)
cont = False

while(cont == False):
    display_balances(checking_acct, savings_acct)
    
    print("--------------------------------------")
    print("D - Make Deposit")
    print("W - Make Withdrawl")
    print("T - Transfer Funds")
    print("A - Apply monthly fee and interest gains")
    print("X - Exit")
    print(">")
    
    cmd = input()
    cmd = cmd.upper()
    
    if(cmd == "D"):
        make_deposit(checking_acct, savings_acct)
    elif(cmd == "W"):
        make_withdrawl(checking_acct, savings_acct)
    elif(cmd == "A"):
        init_fees_n_interest(checking_acct, savings_acct)
    elif(cmd == "X"):
        exit()
    elif(cmd == "T"):
        print("Feature not active yet")
    else:
        print("Invalid Command.")

