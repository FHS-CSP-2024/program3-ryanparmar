## Problem 1 ##
#Fix the following code so that its output matches
# Sample output:
# --------------------------------------------------
# my name is Tim Tester, I am 20 years old
# 
# my skills are
#  - python (beginner)
#  - java (veteran)
#  - programming (semiprofessional)
#  
# I am looking for a job with a salary of 2000-3000 dollars per month

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is ", name, ", I am ", age, "years old")
print(" ")
print("my skills are")
print("- ", skill1, "("+str(level1)+")")
print("- ", skill2, "(" +str(level2)+")")
print("- ", skill3, "(" +str(level3)+")")
print("I am looking for a job with a salary of " +str(lower)+ "-" +str(upper)+ " dollars per month")





## Problem 2 ##
#Please finish the script so that: 
# - the following output is printed:
# Sample output:
# --------------------------------------------------
# X val: 27
# Y val: 15
#
# 27 + 15 = 42
# 27 - 15 = 12
# 27 * 15 = 405
# 27 / 15 = 1.8
#
# - The program should work correctly even if the values of the variables are changed.

x = input("X val: ")
y = input("Y val: ")
a = int(x) + int(y)
b = int(x) - int(y)
c= int(x) * int(y)
d= int(x) / int(y)
print(x+" + "+y+" = "+(str(a)))
print(x+" - "+y+" = "+(str(b)))
print(x+" * "+y+" = "+(str(c)))
print(x+" / "+y+" = "+(str(d)))