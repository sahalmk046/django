# create a dictionary

# numbers=[1,2,3,4,5]
# square_dict = {x:x**2 for x in numbers}
# print(square_dict)

# from a range

# cube_dict = {x: x**3 for x in range(1,6)}
# print(cube_dict)

# using condition
# create a dictionary of even numbers only
# even_dict={x:x*x for x in range(10) if x%2==0}
# print(even_dict)

# swap keys and values

student={
    "name": "john",
    "age":22,
    "coure": "python"
}
swapped={value: key for key, value in student.items()}
print(swapped)