#functions and arguments
help(round)#tells what a function is about includes header and doctstrings

def greet (who = 'Sara'):
    """
    this function greets 
    """
    print (f"hello!{who} ")

greet('Afifa')
greet('Ayra')
greet()

help(greet)

print(1,2,3 ,sep='>')


#high order functions
"""
functions that operate on other functions are called high order functions
you can pass a function as an argument to another function
"""
def mult_by_five (n):
    return n*5

print(mult_by_five(5)) #25

def function_on_arg(fn,arg):
    return fn(arg)  

print(function_on_arg(mult_by_five,7)) # 35


def squared_multbyfive (fn,arg):
    return fn(fn(arg))

print(squared_multbyfive(mult_by_five,5)) #125


def modbyfive (m):
    return m % 5

print(modbyfive(32))
print(max (12,64,93 ,key= modbyfive))

print(round(23.3333,2))#round function