import math

def answer(n):
    # check for 1 square
    if math.sqrt(n) == int(math.sqrt(n)):
        return 1

    #  Fermat's theorem on the sum of two squares
    m = n
    while not m % 2:
        m = m / 2

    for i in range(int(math.sqrt(m))):
        if math.sqrt(m - i**2) == int(math.sqrt(m - i**2)):
            return 2

    # Legendre's three-square theorem
    m = n
    while not m % 4:
        m = m / 4
    if int((m - 7.0) / 8.0) == (m - 7.0) / 8.0:
        return 4

    # Lagrange's four-square theorem
    return 3
