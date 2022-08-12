def max(num1,num2,num3):
    if float(num1) > float(num2) and float(num1) > float(num3):
     return num1
    elif float(num2) > float(num3):
        return num2
    else: return num3

n1 = input("Enter first number")
n2 = input("Enter sec number")
n3 = input("Enter third number")
print("The greatest number is " + max(n1,n2,n3))

