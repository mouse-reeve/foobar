''' Calculate the number of lists that produce one binary tree '''
import math

def answer(seq):
    ''' use binomial coefficients of the sides to find the permutations '''
    if not seq:
        return 1
    l = [i for i in seq if i > seq[0]]
    r = [i for i in seq if i < seq[0]]
    return bin_coef(len(l), len(r))  * answer(l) * answer(r)

def bin_coef(ls, rs):
    ''' calculate the binomial coefficient '''
    return math.factorial(ls + rs) / (math.factorial(ls) * math.factorial(rs))

print answer([5, 9, 8, 2, 1])
