class Customer:
    # Initializing
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._sales = 0

    # Using decorator property
    @property
    def sales(self):
        return self._sales

    # Using another functionality
    @sales.setter
    def sales(self, number):
        self._sales = number

    # Using special methods
    def __str__(self):
        return "Customer attributes name and age: " + self._name + ', ' + str(self._age)

    # Using special methods
    def __len__(self):
        return self.sales

    def print_customer(self):
        print("My customer has %d sales" % self.sales)

class Animal:
    def __init__(self):
        print("Animal criado")

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cachorro criado")

if __name__ == '__main__':

    # Creating new object
    customer = Customer("Antonio", 22)
    customer.sales = 400

    # Attribute exists?
    print(hasattr(customer, 'sales'))

    # Using decorator
    print(customer.sales)

    # Sales customer
    customer.print_customer()

    # Object
    print(type(customer))

    # Inheritance
    dog = Cachorro()