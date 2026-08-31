def factorial(n):
    if n < 3:
        return 1
    
    return factorial(n-1) + factorial(n-2)