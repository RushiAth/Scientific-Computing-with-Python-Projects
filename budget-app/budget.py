class Category:

  def __init__(self, cat=""):
    self.budgetCat = cat
    self.ledger = []
    self.balance = 0
    
  def deposit(self, amt, des=""):
    self.ledger.append({"amount":amt, "description":des})
    self.balance += amt
    
  def withdraw(self, amt, des=""):
    if self.check_funds(amt):
      self.ledger.append({"amount":-amt, "description":des})
      self.balance -= amt
      return True
    else:
      return False
      
  def get_balance(self):
    return self.balance

  def transfer(self, amt, cat):
    if self.check_funds(amt):
      self.withdraw(amt, "Transfer to " + cat.budgetCat)
      cat.deposit(amt, "Transfer from " + self.budgetCat)
      return True
    else:
      return False

  def check_funds(self, amt):
    return not amt > self.balance 

  def __str__(self):
    n = 30-len(self.budgetCat)
    returning = '*'*(n//2) + self.budgetCat
    n = n - (n//2)
    returning += '*'*n + '\n'

    for line in self.ledger:
      returning += f'{line["description"][:23]}' + ' '*(23-len(line["description"]))
      returning += f'{line["amount"]:7.2f}\n'

    returning += f'Total: {self.balance:.2f}'

    return returning


def create_spend_chart(categories):

  returning = "Percentage spent by category\n"

  totals, names = [], []

  for cat in categories:
    tempTotal = 0

    for line in cat.ledger:
      if line["amount"] < 0:
        tempTotal += -line["amount"]

    totals.append(tempTotal)
    names.append(cat.budgetCat)
  
  percents = [round(totals[i]/sum(totals) * 100, 2) for i in range(len(totals))]

  for i in range(100, -1, -10):
    returning += f'{i:3d}' + '|'

    for p in percents:
      returning += ' o ' if p >= i else ' '*3

    returning += ' \n'

  returning += ' '*4 + '-'*(3*len(categories)) + '-\n'

  lenNames = [len(names[i]) for i in range(len(names))]
  maxLen = max(lenNames)

  for i in range(maxLen):
    returning += ' '*5
    
    for j in range(len(names)):
      if not i >= lenNames[j]:
        returning += names[j][i] + '  '
      else:
        returning += ' '*3

    returning += '\n'

  return returning[:-1]