def  ksubsets (n,  k):

# """

# generates the list of subsets (as index array) of n elements

# chosen k at a time. Combinations actually!

# """

#sanity check

    if n <0 or k <0 or n - k < 0:
        return None
        N = range(k)
        retval = [N[:]]
        print("initial N=", N)
        
        #update current N vector.
        level = k-1
        while level >=0:
            d = N[level]

    #test if element is already  at maximum value.

    if d < n - k + level:  
        # No, increment the value.  
        N[level]+= 1
        #repair trailing elements.
        for i in range(level+1,  k):
            N[i] = N[i-1] + 1
        #append newly generated subset.
        retval.append(N[:])
        level = k-1
    else:
        # position N[level] already at maximum value!
        level -= 1
    return retval
    
for i,  subset in enumerate(ksubsets(5,  3)):
    print(i,  subset)
