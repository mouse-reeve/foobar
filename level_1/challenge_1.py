''' find the relationship between two disordered lists '''

def answer(y, x):
    ''' average and compare the two lists '''
    return int(100 * (1 - 1/((sum(x) / len(x)) / (sum(y) / len(y)))))
