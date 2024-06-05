import sys
def add(num1,num2):
    sum = num1 + num2

    return sum

def subtract(num1,num2):
    sub=num1-num2
    return sub
def multiply(num1,num2):
    mul=num1*num2
    return mul
x = float(sys.argv[1])
operation = sys.argv[2]
y = float(sys.argv[3])

if operation== "add":
    print(add(x,y))
elif operation == "subtract":
    print(subtract(x,y))
elif operation == "multiply":
    print(multiply(x,y))
else:
    print("invalid operation")


