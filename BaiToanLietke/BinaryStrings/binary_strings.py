### Print all binary strings of length n ###
### Input: an integer from file bstr.inp.txt ###
### Output: binary strings of length n from file bstr.out.txt ### 

import math
import timeit

start = timeit.timeit()
in_file = open('bstr.inp.txt')
indata = in_file.read()
out_file = open('bstr.out.txt', 'w')

def binaryString(n):
    newBinary = []
    first_string = [0] * n
    for i in range(0, int(math.pow(2, n))):
        newBinary.append("".join(map(str,first_string))[::-1])
        first_string[0] += 1
        for j in range(0, len(first_string) - 1):
            if first_string[j] == 2:
                first_string[j] = 0
                first_string[j + 1] += 1
                continue
            else:
                break
    return newBinary

def main():
    s = int(indata)
    result = binaryString(s)
    out_file.write('\n'.join(result))
    in_file.close()
    out_file.close()
    end = timeit.timeit()
    print(end - start)

if __name__ == "__main__":
    main()      