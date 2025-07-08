class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, name, initial_balance=0):
        if name in self.accounts:
            print(f"Account for {name} already exists.")
        else:
            self.accounts[name] = initial_balance
            print(f"Account opened for {name} with balance {initial_balance}.")

    def get_balance(self, name):
        return self.accounts.get(name, "Account does not exist.")

# Example usage:
if __name__ == "__main__":
    bank = Bank()
    bank.open_account("Alice", 100)
    print("Alice's balance:", bank.get_balance("Alice"))