"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
import random
#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

add_cache = {}
sub_cache = {}

def f(x):
    return x * 4 + 6

# Your code here
def sumdiff(input):
    
    #find all possible combinations for adding and subtracting and put them in their own dict
    for i in range(len(input)):
        for j in range(len(input)):
            add_cache[(q[i], q[j])] = f(q[i]) + f(q[j])
            sub_cache[(q[i], q[j])] = f(q[i]) - f(q[j])
    print(add_cache)
    #find all combinations where the results of addition are equal to subtraction
    for i in add_cache:
        for j in sub_cache:
            if add_cache[i] == sub_cache[j]:
                string1 = f"f({i[0]}) + f({i[1]}) = f({j[0]}) - f({j[1]})"
                string2 = f"{f(i[0])} + {f(i[1])} = {f(j[0])} - {f(j[1])}"

                # print( '{:<40s} {:<40s}'.format(string1, string2) )




sumdiff(q)
