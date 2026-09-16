# square=lambda x:x*x
# print(square(5))

a=int(input("enter a number"))
b=int(input("eneter second number"))

largest=lambda a,b: a if  a > b else b
print (largest(a,b))