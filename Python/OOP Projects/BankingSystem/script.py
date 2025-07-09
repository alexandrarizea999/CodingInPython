import json

class Transaction:
    def __init__(self, title, amount, type, note=""):
        self.title = title
        self.amount = amount
        self.type = type
        self.note = note

    def display_info(self):
        return f"Transaction:\n Expense: {self.title}\n Amount: {self.amount}$\n Type: {self.type}\n Note: {self.note}"


class Bank:
    def __init__(self):
        self.wallet = []

    def add_transaction(self, transaction):
        self.wallet.append(transaction)

    def delete_transaction(self, title):
        for tran in self.wallet:
            if tran.title == title:
                self.wallet.remove(tran)
                return f"{title} has been removed."
        return f"{title} is not found."

    def display(self):
        if not self.wallet:
            return "No transaction available in your wallet."
        return "\n".join([transaction.display_info() for transaction in self.wallet])

    def search_wallet(self, query):
        found = [trans for trans in self.wallet if query.lower() in trans.title.lower() or query.lower() in trans.type.lower()]

        if not found:
            return "No transactions!"
        return "\n".join([transaction.display_info() for transaction in self.wallet])

    def save_data(self, filename="wallet.json"):
        data = [{'Expense': transaction.title, 'Amount': transaction.amount, 'Type': transaction.type, 'Note': transaction.note} for transaction in self.wallet]

        with open(filename, "w") as file:
            json.dump(data, file)

    def load_data(self, filename="wallet.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.wallet = [Transaction(trans['Expense'], trans['Amount'], trans['Type'], trans['Note']) for trans in data]
        except FileNotFoundError:
            print("We don't have that file.")

def main():
    wallet = Bank()

    while True:
        print("\n=== Personal banking system ===")
        print("1. Add a transaction")
        print("2. Remove a transaction")
        print("3. Display all transactions")
        print("4. Search for a transaction")
        print("5. Save transaction to a file")
        print("6. Load transaction from a file")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter the title: ")
            amount = float(input("Enter amount: "))
            type = input("Expense or Deposit: ")
            transaction = Transaction(title, amount, type)
            wallet.add_transaction(transaction)
            print(f"{title} added successfully!")
        elif choice == "2":
            title = input("Enter the title: ")
            print(wallet.delete_transaction(title))
        elif choice == "3":
            print(wallet.display())
        elif choice == "4":
            query = input("Enter the title: ")
            print(wallet.search_wallet(query))
        elif choice == "5":
            wallet.save_data()
            print("Saved as JSON.")
        elif choice == "6":
            wallet.load_data()
            print("Loadded JSON")
        elif choice == "7":
            print("Exiting the program... Goodbye!")
            break
        else: print("Invalid option. Choose a number between 1 and 7!")

if __name__ == "__main__":
    main()
