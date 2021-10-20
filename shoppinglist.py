from product import Product
import os

class Shoppinglist:

    def __init__(self):
        self.all_products = []
        self.my_list = {}
        pass

    def create_product(self, name, description, price):
        product = Product(name, description, price)
        self.all_products.append(product)
        pass
    

    def add_product_to_list(self, index, number):
        try:
            if self.all_products[index] is not None:
                self.my_list[index] = number
            else:
                print("Wrong index")
        except:
            print("Wrong index")

    
    def print_all_products(self):
        print("All products: ")
        for i in range(len(self.all_products)):
            print ("  " + str(i) + " - "+ str(self.all_products[i]))


    def print_my_products(self):
        print("My shopping list: ")
        for key in self.my_list:
            print("   - " + str(self.my_list[key]) + " mal " + str(self.all_products[key].getName()))

    def remove_product(self, index, number):
        try:
            if self.all_products[index] is not None:
                self.my_list[index] = self.my_list[index] - number
            else:
                print("Wrong index")
        except:
            print("Wrong index")

    def calculate_price(self):
        sum_price = 0
        for key in self.my_list:
            sum_price = sum_price + (int(self.all_products[key].getPrice()) * int(self.my_list[key]))
            pass
        return sum_price
    
    def write_to_file(self):
        if os.path.exists("products.csv"):
            f = open("products.csv", "a")
        else:
            f = open("products.csv", "x")

        for product in self.all_products:
            f.write(product.getName()+";"+product.getDescription()+";"+product.getPrice()+"\n")
        f.close()
        pass

        