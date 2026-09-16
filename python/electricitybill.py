a=int(input('Enter you electricity bill : '))
if(a<=100):
    print(a*5)
elif(a<=200):
    print((100*5)+((a-100)*7))
else:
    print((100*5)+((a-100)*7)+((a-200)*10))