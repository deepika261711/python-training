class Account:
    def __init__(self, balance, accno):
        self.balance = balance
        self.accno = accno

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} is debited, balance is {self.getbal()}")
        else:
            print("Insufficient funds")

    def credit(self, amount):
        self.balance += amount
        print(f"{amount} is credited, balance is {self.getbal()}")

    def getbal(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, balance, accno, interest):
        super().__init__(balance, accno)
        self.interest = interest

    def interestrate(self):
        interest_amount = self.balance * (self.interest / 100)
        self.balance += interest_amount
        print(f"Interest added. New balance is {self.getbal()}")


# Using Account
acc1 = Account(1000, "acc123")
acc1.credit(500)
acc1.debit(100)

# Using SavingsAccount
acc2 = SavingsAccount(1000, "sav123", 5)
acc2.credit(500)
acc2.interestrate()
