### Given a positive integer number ###
### find all ways to analyse this number to sums of positive numbers. ###
import sys
import timeit

start = timeit.default_timer()
in_file = open('analyse.inp.txt')
indata = in_file.read()
out_file = open("analyse.out.txt", 'w')
sys.stdout = out_file

def print_result(k):
    print(n, '=', end = ' ')
    for i in range(0, k):
        print(x[i], '+', end = ' ')
    print(x[k])    

def analyse_number(i):
    for j in range(x[i - 1], (n - t[i - 1]) // 2 + 1):
        x[i] = j
        t[i] = t[i - 1] + j
        analyse_number(i + 1)
    x[i] = n - t[i - 1]
    print_result(i)  
    
x = []
t = []
n = int(indata)
for b in range(0, n):
    x.append(1)
    t.append(1)
analyse_number(1)
in_file.close()
end = timeit.default_timer()
print('Time:', end - start)
out_file.close()
