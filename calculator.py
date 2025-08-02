import math

def addition (a,b):
    return a+b
def subtraction (a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division (a,b):
    try: 
        return a/b
    except ZeroDivisionError :
        print("Division by zero is not possible")
def power(a,b):
    return a**b
def module(a,b):
    return(a%b)
def square_root(a,_=None):
    return math.sqrt(a)
        
operationDictionary={
    "+":addition,
    "-":subtraction,
    "*":multiplication,
    "/":division,
    "**":power,
    "%":module,
    "V":square_root
    
}
  
while True:       
    print("Cool Calculator \n")
    number1=float(input("Type a number: \n"))
    number2=float(input("Type a number: \n"))
    operation=input("Type operation calculator: +, -, *, /, **(power), %(module), V(square root) \n")

    if operation in operationDictionary:
        result=operationDictionary[operation](number1,number2)
        print("Result is: ",result)
    else:
        print("Invalid operation")
        
    continuee = input("continue? [Y]yes [N]No \n")
    if continuee.lower() != "y":
        break
    
    



        
