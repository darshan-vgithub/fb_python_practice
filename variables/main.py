# Variable= A container for a value (string, int, float,bool)
# Strings
first_name="Darshan"
print(first_name) #normal printing the name 
print(f"Hello {first_name}") # this is format we can print the variable along with string 


# practice the f string 
food="pizza"
email="DqC7A@example.com"

print(f"Hello {first_name} your favorite food is {food} and your email is {email}")

print("====================================\n")
#Integers
age=24
print(f"you are {age} years old")

quantity=5
print(f"I purchased {quantity} of goldbees")

num_of_students=30
print(f"There are {num_of_students} students in the class\n")

print("====================================\n")


#Float
price=9.99
print(f"The price of the item is ${price}")

gpa=9.5
print(f"Your gpa is {gpa}")

distance=10.5
print(f"You have travelled {distance}km \n")

print("====================================\n")


#Boolean

is_student=False
print(f"You are a student {is_student}")
for_sale=True

if for_sale:
    if is_student:
        print("you cant buy the item")
    else:
        print("you can buy the item")

