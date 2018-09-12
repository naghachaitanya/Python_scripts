#method for adding of two numbers 
def add(x,y):
    return x+y
#method for multiply of two numbers
def multiply(x,y):
    return x*y
#method for substracting of two numbers
def subtract(x,y):
    return x-y
#method for division of two numbers
def division(x,y):
    return x/y
#showing the operations for user to choose
print("select the operation to perform")
print("1.add")
print("2.multiply")
print("3.subtract")
print("4.division")

#capturing the user choice
choice = input("Enter the input choice(1/2/3/4)")

#capturing the input numbers to perform selected operations
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
    print(num1, "*",num2,"=", multiply(num1,num2))
elif choice == '3':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=",division(num1,num2))
else:
    print("invalid input")
