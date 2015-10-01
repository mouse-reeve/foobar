''' Find the number of strings that are unique forward and backwards '''

def answer(x):
    ''' halve the count of a list of all entries and their reversals '''
    x = list(set(x))
    y = x + [i[::-1] for i in x if (i[::-1] not in x) or (i[::-1] == i)]
    return len(y)/2
