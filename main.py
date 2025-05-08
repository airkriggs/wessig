menu = {
    "Burgers": {
        "Cheeseburger": 4.99,
        "Bacon Cheeseburger": 5.99,
        "Double Sonic Burger": 6.49
    },
    "Hot Dogs": {
        "Classic Hot Dog": 2.99,
        "Chili Cheese Dog": 3.49,
        "Premium Hot Dog": 3.99
    },
    "Drinks": {
        "Cherry Limeade": 1.99,
        "Soft Drink": 1.49,
        "Milkshake": 3.99
    },
    "Sides": {
        "Fries": 1.99,
        "Tater Tots": 2.29,
        "Mozzarella Sticks": 3.49
    }
}

order = {}

def print_menu():
    print("Welcome to Sonic!")
    print("Here is the menu:\n")
    for category, items in menu.items():
        print(f"== {category} ==")
        for item, price in items.items():
            print(f"{item} - ${price:.2f}")
        print("")

def take_order():
    ordering = True
    while ordering:
        print("What would you like to order? (type 'done' when finished)")
        item = input(" - ").strip()
        if item.lower() == "done":
            ordering = False
            print("\nDone ordering!\n")
            break

        in_menu = False
        for category in menu:
            if item in menu[category]:
                in_menu = True
                try:
                    amount = int(input(f"How many {item}s would you like? "))
                except ValueError:
                    print("Please enter a valid number.\n")
                    break

                if item in order:
                    order[item]['quantity'] += amount
                else:
                    order[item] = {
                        "price": menu[category][item],
                        "quantity": amount
                    }
                print(f"Added {amount} {item}(s) to your order.\n")
                break

        if not in_menu:
            print("Sorry, that item is not on the menu. Try again.\n")

def receipt():
    total = 0
    print("Here’s your receipt:\n")
    for item, details in order.items():
        line_total = details['price'] * details['quantity']
        total += line_total
        print(f"{item} x {details['quantity']} = ${line_total:.2f}")
    print(f"\nYour total is: ${total:.2f}")
    print("\nThank you for visiting Sonic!")

if __name__ == "__main__":
    print_menu()
    take_order()
    receipt()
