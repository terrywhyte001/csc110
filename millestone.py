# Milestone deliverable: Basic shopping cart
shopping_cart = []

while True:
    # Display the contents of the shopping cart at the start of each loop
    if shopping_cart:
        print("\nCurrent contents of the shopping cart:")
        total_price = 0
        for i, (item, price) in enumerate(shopping_cart, start=1):
            print(f"{i}. {item} - ${price:.2f}")
            total_price += price
        print(f"\nTotal price of items in the cart: ${total_price:.2f}")
    else:
        print("\nThe cart is currently empty.")

    # Display the menu
    print("\nShopping Cart Menu:")
    print("1. Add item to cart")
    print("2. Display the contents of the shopping cart")
    print("3. Remove item from cart")
    print("4. Clear cart")
    print("5. Quit")
    choice = input("Please enter your choice (1-5): ").strip()

    if choice == "1":
        item = input("Enter the item you want to add to the cart: ").strip()
        try:
            price = float(input(f"Enter the price of {item}: ").strip())
            shopping_cart.append((item, price))  # Store item as a tuple (name, price)
            print(f"{item} has been added to your cart.")
        except ValueError:
            print("Invalid price. Please enter a valid number.")

    elif choice == "2":
        # This option is now redundant since the cart contents are displayed at the start
        print("\nThe contents of the shopping cart are already displayed above.")

    elif choice == "3":
        if shopping_cart:
            print("\nThe contents of the shopping cart are:")
            for i, (item, price) in enumerate(shopping_cart, start=1):
                print(f"{i}. {item} - ${price:.2f}")
            try:
                index = int(input("Enter the number of the item you want to remove: ").strip())
                if 1 <= index <= len(shopping_cart):
                    removed_item, removed_price = shopping_cart.pop(index - 1)
                    print(f"{removed_item} has been removed from your cart.")
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("\nThe cart is empty. Nothing to remove.")

    elif choice == "4":
        shopping_cart.clear()
        print("The cart has been cleared.")

    elif choice == "5":
        print("Thank you for using the shopping cart program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
