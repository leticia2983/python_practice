def add(num1,num2):
        sum = num1 + num2

        return sum

def subtract(num1,num2):
        sub=num1-num2
        return sub
def multiply(num1,num2):
        mul=num1*num2
        return mul



print("enter the two numbers")
x=int(input('firstnumber'))
y=int(input('secondnumber'))

print("addition: ",add(x,y))
print("subtraction: ",subtract(x,y))
print("multiplication: ",multiply(x,y))