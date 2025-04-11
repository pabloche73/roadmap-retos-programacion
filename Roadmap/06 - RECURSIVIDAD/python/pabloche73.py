# Recursividad

def down_to_zero(n): 
    if n < 0:
        return
    print(n)
    down_to_zero(n - 1)

down_to_zero(100)

# Estra

def factorial(n): 
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(10))

# Fibonacci

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5)) 