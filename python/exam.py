# 6


# create product and shopping cart classes
# add products remove products calculate total bill

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class ShoppingCart:
    def __init__(self):
        self.products=[]
    def add(self,product):
        self.products.append(product)
    def remove(self,product):
        self.products.remove(product)
    def total(self):
        total=0
        for product in self.products:
            total+=product.price
        return total
p1=Product("Apple",50)
p2=Product("Mango",60)
p3=Product("watermelon",40)
cart=ShoppingCart()
cart.add(p1)
cart.add(p2)
cart.add(p3)
cart.remove(p2)
print("total bill:",cart.total())



# write a lamba function to check wheather a number is Even


# even=lambda n:n%2==0
# n=int(input("Enter a number: "))
# print(even(n))

# write an example of closure


# def outer():
#     x=10
#     def inner():
#         print(x)
#     return inner
# a=outer()
# a()