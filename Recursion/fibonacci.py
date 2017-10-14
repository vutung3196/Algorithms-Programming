# A recursive algorithm for fibonacci problem
# Find nth element in a fibonacci sequence

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)    

a = int(input())   
result = fibonacci(a)
print(result)