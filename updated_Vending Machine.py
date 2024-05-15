

print("Hello")
print("Welcome to Vending Machine")

# Created a dictionary for the items, prices and stocks
items = {
    "Drinks": {
        "A1": {"option": "Pepsi-Cola","price":2.00, "stock":5},
        "A2": {"option": "Dew","price":2.00, "stock":5}, 
        "A3": {"option": "Fanta","price":2.00, "stock":5},
        "A4": {"option": "Coca cola","price":2.00, "stock":5},
        "A5": {"option": "Diet-Pepsi","price":2.50, "stock":5},
    },
    "Candies": {
        "B1": {"option": "Kit-Kat","price":1.50, "stock":5},
        "B2": {"option": "Milka","price":3.00, "stock":5},
        "B3": {"option": "Oreo","price":2.00, "stock":5},
        "B4": {"option": "Dairy milk","price":2.00, "stock":5},
        "B5": {"option": "Ferero","price":4.00, "stock":5},
    },
    "Chips":{
        "C1": {"option": "Oman chips","price":1.00, "stock":5},
        "C2": {"option": "Cheetos","price":2.50, "stock":5},
        "C3": {"option": "Pringles","price":3.00, "stock":5},
        "C4": {"option": "Lays","price":1.00, "stock":5},
        "C5": {"option": "Takis","price":4.00, "stock":5},
    },
    }

# Function for printing the menu
def print_menu(items):
    print("menu:\n")
    for category, category_items in items.items():
        print(category +":")
        for code, item in category_items.items():
            print(f'{code}: {item["option"]} ({item["price"]:.2f} usd)')

# Function for getting the code of the item from the user
def get_code(items):
    while True:
        code= input("Enter code:")
# If entered an invalid code returning to get a valid code
        for category, category_items in items.items():     
            if code in category_items:
                return code    
                print("Invaid code entered. Please enter a valid code")


# Function to get the paymet from the user
def get_payment(items, code):

    for category,  category_items in items.items():
        if code in category_items:
            item = category_items[code]
            break
    else:
        print(f'"Invalid code "{code}".')
        return
    while True:
        payment = float(input("ENTER AMOUNT OF MONEY:"))
# If payment not sufficient returning to get sufficient amount
        if payment < item["price"]:
            print( f' Not enough money paid, please insert valid money {item["price"] - payment:.2f}usd more to enjoy your Snacks') 
        else:
            return payment

# Function for dispensing the item from the mschine
def dispense_item(items,code,payment):
    for category,  category_items in items.items():
        if code in category_items:
           item=category_items[code]
           break
    else:
            print(f'invalid code"{code}".')
            
# If item out of stock
    if item["stock"]  >0:

            print(f'\ndispensing {item["option"]}..')
            change= payment - item["price"]
            item["stock"] -=1
            print(f"returning ${change:.2f} change..\n")
    else:
                print(f'\nError: {item["option"]}is out of stock :(')


# Function for suggesting additional products to be purchased
def suggest_purchase(items, code):
    if code in items["Drinks"]:
        print("People usually buy with this:")
        for code, items in items["Candies"].items():
            print(f'{code}:{items["option"]} ({items["price"]:.2f}usd)')
    elif code in items["Candies"]:
        print("People usually buy with this")     
        for code, items in items["Drinks"].items():
            print(f'{code}:{items["option"]} ({items["price"]:.2f}usd)')             

# Main loop of the program
while True:
    # for printing menu
    print_menu(items)

    # for the users input of the items code
    code = get_code(items)

    # for the payment from the user
    payment = get_payment(items, code)

    # to dispense the item
    dispense_item(items,code,payment)

    # to suggest additional item
    suggest_purchase(items,code)

    # loop if the user wants to make another purchase
    while True:
        response = input("\n make another purchase ? (yes/no)")
        if response.lower() == "yes":
          break
        elif response.lower() == "no":
          print("THANK YOU AND ENJOY YOUR SNACKS")
          exit()
        else:
          print("invalid reply try again.")            
