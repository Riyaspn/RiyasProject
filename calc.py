try:
    def cal(a, b, c):
        if c in "+":
            d = a + b
        if c in "-":
            d = a - b
        if c in "*":
            d = a * b
        if c in "/":
            d = a / b
        print("The value of", a, c, b, "is :", d)

    a = int(input("Enterr the first number "))
    b = int(input("Enterr the sec number "))
    c = input("Enterr the operator ")
    cal(a,b,c)
except ZeroDivisionError as err:
    print(err)
except:
    print("Invalid input")
