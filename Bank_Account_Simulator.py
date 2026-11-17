class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return False

        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance


def main():
    account = BankAccount("Dileep", 2000)

    account.deposit(500)
    account.withdraw(200)

    print("Owner:", account.owner)
    print("Balance:", account.get_balance())


if __name__ == "__main__":
    main()