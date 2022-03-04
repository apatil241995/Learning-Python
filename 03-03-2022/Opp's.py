class Bank:
  def __init__(self, name, account_no):
   self.balance = 0
   self.name = name
   self.account_no = account_no

  def Account_details(self):
   return f"name:- {self.name}, Account No. :- {self.account_no}"


  def Account_balance(self):
   return f"Account balance:- {self.balance} "


  def Withdraw(self, amount):
   self.balance -= amount
   return self.balance


  def Deposit(self, amount):
   self.balance += amount
   return self.balance