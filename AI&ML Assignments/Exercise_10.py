# Shopping list tuples format: (item_name, quantity, unit_price, category)
shopping_cart = [
    ("Yam Tuber", 2, 2500, "Food"),
    ("Rice 1kg", 3, 1600, "Food"),
    ("Bathing Soap", 4, 600, "Toiletries"),
    ("Bleach", 1, 1200, "Cleaning"),
    ("Electric Kettle", 1, 15000, "Electronics"),
    ("Bread", 3, 1000, "Food")
]

# Variables to keep track of totals
total_without_tax = 0
total_tax = 0

# Variables for category subtotals
food_total = 0
toiletries_total = 0
cleaning_total = 0
electronics_total = 0

# Set to count unique categories
categories_set = set()

print("....................................")
print("        SUPERMARKET RECEIPT         ")
print("....................................")

# Loop through the cart to process each item
for item, qty, price, category in shopping_cart:
    
    line_cost = qty * price
    total_without_tax = total_without_tax + line_cost
    categories_set.add(category)
    
    # Calculate VAT (7.5%) only if it is not Food
    item_tax = 0
    if category != "Food":
        item_tax = line_cost * 0.075
        total_tax = total_tax + item_tax
        
    # Add to the correct category subtotal
    if category == "Food":
        food_total = food_total + line_cost
    elif category == "Toiletries":
        toiletries_total = toiletries_total + line_cost
    elif category == "Cleaning":
        cleaning_total = cleaning_total + line_cost
    elif category == "Electronics":
        electronics_total = electronics_total + line_cost

    # Check for flag over 5000
    flag = ""
    if line_cost > 5000:
        flag = "[*** EXPENSIVE ITEM ***]"
        
    # Print the item line
    print(f"{item} (x{qty}) - ₦{line_cost} {flag}")

print("------------------------------------")
# Print Subtotals
print("SUBTOTALS BY CATEGORY:")
print(f"Food: ₦{food_total}")
print(f"Toiletries: ₦{toiletries_total}")
print(f"Cleaning: ₦{cleaning_total}")
print(f"Electronics: ₦{electronics_total}")

print("------------------------------------")
# Print final numbers
grand_total = total_without_tax + total_tax
print(f"Unique Categories Bought: {len(categories_set)}")
print(f"Total Before Tax: ₦{total_without_tax}")
print(f"VAT (7.5% on non-food): ₦{total_tax}")
print("....................................")
print(f"GRAND TOTAL: ₦{grand_total}")
print("....................................")
print("Thank you for shopping with us!")