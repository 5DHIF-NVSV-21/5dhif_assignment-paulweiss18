from product import Product
from shoppinglist import Shoppinglist


# Output class for console application


def draw_headline():
    print(" __   _     ___   ___   ___   _   _      __        _     _   __  _____ ")
    print("( (` | |_| / / \ | |_) | |_) | | | |\ | / /`_     | |   | | ( (`  | |  ")
    print("_)_) |_| | \_\_/ |_|   |_|   |_| |_| \| \_\_/     |_|__ |_| _)_)  |_|  ")
    pass



if __name__ == '__main__':

    list_handler = Shoppinglist()
    is_running = 1

    while(is_running):

        # Menu 
        print("\n\n")
        draw_headline()
        print("---------------------------------------------------------------------")
        print("Welcome to your shopping list!")
        print("You can choose between the following options: ")
        print("[1] Show all available products")
        print("[2] Show my product list")
        print("[3] Create a new product")
        print("[4] Add a product to my list")
        print("[5] Remove a product from my list")
        print("[6] Calculate the final price")
        print("[7] Export my products as XML")
        print("[0] Close Application")
        print("---------------------------------------------------------------------")

        option = input("Your choice: ")

        if option == "1":
            # Show all items
            list_handler.print_all_products()
            pass

        elif option == "2":
            # Show my product list
            list_handler.print_my_products()
            pass

        elif option == "3":
            # Create a new product
            name = input("Name: ")
            description = input("Description: ")
            price = input("Price: ")
            list_handler.create_product(name,description,price)
            pass

        elif option == "4":
            # Add a product to my list
            index = int(input("Index of item: "))
            number = int(input("Numbers of product: "))
            list_handler.add_product_to_list(index, number)
            pass

        elif option == "5":
            # Remove a product
            index = int(input("Index of item: "))
            number = int(input("Numbers of product: "))
            list_handler.remove_product(index, number)
            pass

        elif option == "6":
            # Calculate the final price
            print("Your total price: " + str(list_handler.calculate_price()) + "€ ")
            pass

        elif option == "7":
            # Export as XML
            list_handler.write_to_file()
            pass

        elif option == "0":
            # Close application
            is_running = 0
            pass