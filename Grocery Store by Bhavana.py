# Grocery Store Management System - Bhavana

# Step 1: Product Inventory
products = {
    1: {"name": "Milk", "price": 25, "stock": 50},
    2: {"name": "Bread", "price": 20, "stock": 100},
    3: {"name": "Rice", "price": 50, "stock": 80},
    4: {"name": "Eggs", "price": 6, "stock": 200}
}

# Step 2: Show available products
def show_products():
    print("\nAvailable Products:")
    for product_id, details in products.items():
        print(f"{product_id}. {details['name']} - ₹{details['price']} (Stock: {details['stock']})")

# Step 3: Billing logic
cart = []
total_amount = 0

while True:
    show_products()
    choice = input("\nEnter Product ID to buy (or type 'done' to finish): ")

    if choice.lower() == 'done':
        break

    if not choice.isdigit() or int(choice) not in products:
        print("Invalid Product ID. Please try again.")
        continue

    product_id = int(choice)
    quantity = int(input(f"Enter quantity for {products[product_id]['name']}: "))

    if quantity > products[product_id]['stock']:
        print("Sorry! Not enough stock.")
        continue

    # Update stock
    products[product_id]['stock'] -= quantity

    # Calculate price
    item_total = products[product_id]['price'] * quantity
    total_amount += item_total

    # Add to cart
    cart.append({
        "name": products[product_id]['name'],
        "price": products[product_id]['price'],
        "quantity": quantity,
        "total": item_total
    })

# Step 4: Final Bill
print("\n🧾 Final Bill:")
for item in cart:
    print(f"{item['name']} x {item['quantity']} = ₹{item['total']}")

print(f"\nTotal Amount: ₹{total_amount}")
print("Thank you for shopping with us! 🛍️")