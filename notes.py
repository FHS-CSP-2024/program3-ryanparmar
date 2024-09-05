# More about variables #
#**Learning objectives**
#
#After this section:
#
#* You will be able to use variables in different contexts
#* You will know what kind of data can be stored in variables
#* You will understand the difference between strings, integers and floating point numbers


myXVAL =10
myxval = 7

print(myXVAL)
name="Chuck"
number=100
newnumber ="100"

print(number/2)
#print(newnumber/2) doesnt work because it is a string
print(int(newnumber)/2)

myFloat = 3.54

num1=100
num2=75
numm3=967
avg=(num1+num2+num3)/3
print(r"Average: (avg)")
print(avg)
print("Average", avg)
print("Average " + str(avg))


beds = 3
bath = 3
adress = "4028 Dog drive"
city = "Folsom"
zip= 95630
rent= 7000

print(f"House for rent at {adress} in {city} ({zip})")
print(f"\t{beds} bedrooms, {bath} bathrooms")
print(f"\trent is ${rent}/month")

#file path example
print("I have a file located at: C:\\Users\\mrJohnson\\Documents...")

## Live Demo ##
#
# Casing
#name = input("What is your name? ")
#Name = input("What is your name? ")
#print(name)
#print(Name)
#
# Talk about Variable Types
#   * int vs string vs float
#intNum = 75
#print(intNum/2)
#number = "100"
#print(number / 2)
#number1 = 2.5
#number2 = -1.25
#number3 = 3.62
#
#print(f"Mean: {mean}")
#mean = (number1 + number2 + number3) / 3
#
# Printing different types and Casting
#result = 10 * 25
#print("The result is " + result)
#print("The result is " + str(result))
#print("The result is", result)
#print(f"The result is {result}") # Format string {} denotes values to be printed
#name = "Mark"
#age = 37
#city = "Palo Alto"
#print(f"Hi {name}, you are {age} years old. You live in {city}.")
#
# Printing invisible things
#print("\n") # newline
#print("\t") # tab
#print("\\") # \
