### Print all subsets which have K elements ###
import timeit
import pprint

start = timeit.default_timer()
def subSet(n, k):
    allSet = []
    firstSet = []
    for i in range(1, k + 1):
        firstSet.append(i)
    index = 0
    while True:
        index = k - 1
        allSet.append(firstSet[:])
        while index >= 0 and firstSet[index] == (n - k + index + 1):
            index -= 1
        if index >= 0:
            firstSet[index] += 1
            for j in range(index + 1, k):
                firstSet[j] = firstSet[j - 1] + 1
        if index == -1:
            break
    return allSet

def main():
    with open('subset.inp.txt') as f:
        k, n = [int(x) for x in next(f).split()]
    result = subSet(k, n)
    with open('subset.out.txt', 'w') as outputFile:
        outputFile.write("Result: ")
        pprint.pprint(result, outputFile)
    end = timeit.default_timer()
    print(end - start)

if __name__ == "__main__":
       main()   