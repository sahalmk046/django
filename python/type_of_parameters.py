# 1 multiple parameters and argument


def new(a, b):
    print(a+b)

new(3,5)


# 2 default parameter:


def greet(name, message="Welcome"):
    print (message,name)
greet('fajas')


# 3 keyword argument

def keyword(name,place):
    print(name,place)

keyword(place="mahe",name="sahal")

# 4 position argument

def greet(name,message):
    print(name,message)

greet('hello','fajas')