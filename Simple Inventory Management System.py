
inventory = {}

def view_inventory():
    print("\nInventory:")
    if len(inventory) == 0:
        print("The inventory is empty.")
    else:
        for item in inventory:
            print(item, ":", inventory[item], "units")


def add_item():
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))

    # Check if item already exists
    if item_name in inventory:
        inventory[item_name] += quantity  
    else:
        inventory[item_name] = quantity   

    print(item_name, "added/updated.")

# Function to update quantity of an existing item
def update_item():
    item_name = input("Enter item name to update: ")

    if item_name in inventory:
        new_quantity = int(input("Enter new quantity: "))
        inventory[item_name] = new_quantity
        print(item_name, "updated.")
    else:
        print("Item not found in inventory.")

# Function to display menu and get user choice
def show_menu():
    while True:
        print("\n--- Inventory Menu ---")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Start the program
show_menu()
