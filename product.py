

# Bean class for Product

class Product:

    def __init__ (self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        pass

    def getName(self):
        return self.name
        pass
    
    def getDescription(self):
        return self.description
        pass

    def getPrice(self):
        return self.price
        pass

    def __repr__(self):
        return self.name + ": " + self.price + "€"