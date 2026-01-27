from pprint import pprint
# Task 1
# Your task is to dynamically update the quantity of a supply item after a sale.

# Request as much information from the user in order to know what product is to be sold.

# Print out your inventory after each sale.

# Task 2
# Create a shopping list of supplies that are low in stock(fewer than 10)

# Task 3
# Find which animal type has the most variety. Variety in this case means the animal with the most headcount and number of breeds


# ask user for category
# check if the category exists
# ask user for specific item in category
# check if item is in category
# ask user for quantity of item
# check if the quantity is available
# subtract what is sold from quantity available
# print inventory showing what is available


petShop = {
    "animals": {
        "dogs": {"Labrador": 3, "Beagle": 2, "Poodle": 1, "Mastiff": 5},
        "cats": {"Persian": 2, "Siamese": 1, "Maine Coon": 2},
        "fish": {"Goldfish": 12, "Angelfish": 5, "Betta": 3},
        "birds": {"Parakeet": 4, "Canary": 3, "Cockatiel": 7}
    },
    "supplies": {
        "food": {"Dog Food": 20, "Cat Food": 9, "Fish Food": 25},
        "toys": {"Dog Toys": 30, "Cat Toys": 20},
        "habitats": {"Aquariums": 5, "Cat Trees": 8, "Dog Beds": 7}
    },
}


stock = petShop.keys()

stock_category = input(f"enter your category ({", ".join(stock)}): ")
# print(category)

while stock_category not in stock:
    print("Invalid category")
    stock_category = input(f"enter your category ({", ".join(stock)}): ")

category = petShop[stock_category].keys()
item_choice = input(f"enter your sub category ({", ".join(category)}): ")

while item_choice not in category:
    print("invalid sub category")
    item_choice = input(
        f"enter your sub_category ({", ".join(category)}): ")

product = petShop[stock_category][item_choice].keys()
item_name = input(f"Enter the item you want ({", ".join(product)}): ")

while item_name not in product:
    print("invalid item")
    item_name = input(f"Enter the item you want ({", ".join(product)}): ")


quantity = petShop[stock_category][item_choice][item_name]
print(quantity)
qty_requested = int(
    input(f"Enter the quantity, available quantity is '{quantity}': "))

while qty_requested > quantity or qty_requested < 0:
    print(f"Sorry we only have '{quantity}' in stock")
    qty_requested = int(
        input(f"Enter the quantity, available quantity is '{quantity}': "))

petShop[stock_category][item_choice][item_name] -= qty_requested

current_inventory = petShop
pprint(current_inventory)
