''' Compute a digest message '''

def answer(digest):
    ''' solve for m[1] '''
    message = []
    for i, v in enumerate(digest):
        pv = message[i - 1] if i > 0 else 0

        m = 0.1
        a = 0
        while m != int(m):
            m = ((256 * a) + (v ^ pv)) / 129.0
            a += 1
        m = int(m)
        message.append(m)

    return message
