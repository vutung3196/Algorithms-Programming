# A recursive algorithm example for factorial problem

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

a = int(input())
result = factorial(a)
print(result)