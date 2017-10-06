#This is the backtracking algorithm solution for binary strings problem.
import timeit

start = timeit.default_timer()
in_file = open('bs.inp.txt')
indata = in_file.read()
out_file = open('bs.out.txt', 'w')

# Double recursions in this function
def backTrack_one(k):
    if k < 1:
        b.append("".join(map(str, a))[::-1])
    else:
        a[k - 1] = 0
        backTrack_one(k - 1)
        a[k - 1] = 1
        backTrack_one(k - 1)
    return b

# Just use one recursion
def backTrack_two(i):
    for j in range(0, 2):
        a[i] = j
        if i == n - 1:
            b.append("".join(map(str, a))[::-1])
        else:
            backTrack_two(i + 1)
    return b    

n = int(indata)
a = [0] * n  
b = []  
result = backTrack_two(0)
out_file.write('\n'.join(result))
in_file.close()
out_file.close()
end = timeit.default_timer()
print(end - start)