# Create a list of 10 numbers and print each element using a loop.

# l=[1,2,3,4,5,6,7]
# for i in l:
#     print(i)

# Find the sum of all elements in a list

# l=[1,2,3,4,5,6,7]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)

# Find the largest element in a list.

# l=[12,35,17,22,75,67,37]
# largest=l[0]
# for i in l:
#     if i>largest:
#         largest=i
# print(largest)

# Find the smallest element in a list

# l=[12,35,17,22,75,67,37]
# smallest=l[0]
# for i in l:
#     if i<smallest:
#         smallest=i
# print(smallest)

# print number of odd and even

even=0
odd=0
l=[10,21,30,43,50,60]
for i in l:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print ("number of odd=",odd)
print ("number of even=",even)