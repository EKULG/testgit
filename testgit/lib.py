def find_factorial(x):
    """An excuse to write a recursive fucntion"""
    if x == 1:
        return 1
    else:
        return (x * find_factorial(x-1))

#Play around with different values of x
x = 5

print(f"The factorial of {x} is {find_factorial(x)}")
