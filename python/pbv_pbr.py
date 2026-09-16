# pass by value
# pass by referrence

# immutable

# def change(x):
#     x = 20

# a = 10
# change(a)

# print(a)

# mutable

def change(x):
    x[0] = 20

a = [10]
change(a)

print(a)