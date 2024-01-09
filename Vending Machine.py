
print("""""

██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝""")

class VendingMachine:
    def __init__(self):
        self.items = {'1': {'name': 'PEPSI', 'price': 2, 'quantity': 10},
                      '2': {'name': 'FANTA', 'price': 3.50, 'quantity': 5},
                      '3': {'name': 'DEW', 'price': 5.50, 'quantity': 10},
                      '4':{'name':'LAYS','price':4.00,'quantity':5},
                      '5':{'name':'CANDY','price':1.00,'quantity':10},
                      '6':{'name':'EXTRA','price':2.50,'quantity':5},
                      '7':{'name':'LOLI','price':2.50,'quantity':10},
                      '8':{'name':'MILK','price':3.50,'quantity':5,
                      '9':{'name':'MARS','price':7.00,'quantity':10},
                      '10':{'name':'DAIRY','price':5.25,'quantity':5}}}
        self.balance = 0

    def display_items(self):
        print("Available items:")
        for code, item in self.items.items():
            print(f"{code}. {item['name']} - ${item['price']:.2f} - Quantity: {item['quantity']}")

    def insert_money(self, amount):
        self.balance += amount
        print(f"Inserted: ${amount:.2f}, Total Balance: ${self.balance:.2f}")

    def purchase_item(self, item_code):
        if item_code in self.items:
            item = self.items[item_code]
            if item['quantity'] > 0 and self.balance >= item['price']:
                self.balance -= item['price']
                item['quantity'] -= 1
                print(f"Purchased {item['name']} for ${item['price']:.2f}. Remaining Balance: ${self.balance:.2f}")
            else:
                print("Insufficient balance or item out of stock.")
        else:
            print("Invalid code.")

    def return_change(self):
        if self.balance > 0:
            print(f"Returning change: ${self.balance:.2f}")
            self.balance = 0

def main():
    vending_machine = VendingMachine()

    while True:
        print("\nOptions:")
        print("1. Display Items available")
        print("2. Insert cash")
        print("3. Purchase Item")
        print("4. Return Change")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            vending_machine.display_items()
        elif choice == '2':
            amount = float(input(" insert money: $"))
            vending_machine.insert_money(amount)
        elif choice == '3':
            item_code = input("Enter item code: ")
            vending_machine.purchase_item(item_code)
        elif choice == '4':
            vending_machine.return_change()
        elif choice == '5':
            exit = input("")
            break
        else:
            print("Invalid choice. Please try again.")
            

if __name__ == "__main__":
    main()