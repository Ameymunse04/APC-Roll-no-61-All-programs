
class BankAccount:
    count = 1000

    def __init__(self, name):
        self.account_holder = name
        self.balance = 0
        BankAccount.count += 1
        self.account_number = BankAccount.count

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(self.account_holder, "Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful")
        else:
            print("Insufficient balance")


#  two accounts
a1 = BankAccount("Amey")
a2 = BankAccount("Rahul")

print("Account Number:", a1.account_number)
print("Account Number:", a2.account_number)

#  operations
a1.deposit(5000)
a1.withdraw(1000)
a1.transfer(2000, a2)

# Display balances
a1.display_balance()
a2.display_balance()
