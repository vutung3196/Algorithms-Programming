# A recursive algorithm for Towers of Hanoi puzzle

import timeit
start = timeit.default_timer()
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)
    
count = 0
moveTower(15,"A","B","C")
end = timeit.default_timer()
print(end - start)