def factorial(n):
    if n<1:
        pass
    else:
        n=n*factorial(n-1)
    return n
print(factorial(-10))