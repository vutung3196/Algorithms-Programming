# A recursive algorithm to prove Collatz's hypothesis
# Given a positive integer X. If X is even, X:= X // 2 else X = X * 3 + 1
# After limited steps, X will be equal to 1

def collatz_recur(n):
    if n == 1:
        return n
    else:
        if n % 2 == 0:
            return collatz_recur(n // 2)
        else:
            return collatz_recur(3 * n + 1)

a = int(input())
result = collatz_recur(a)
print(result)   