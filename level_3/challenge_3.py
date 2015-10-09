''' Remove instances of an added word from a string '''

def answer(chunk, word):
    ''' remove the rightmost word instance that is the most nested '''
    if not word in chunk:
        return chunk

    chunk = chunk[::-1]
    word = word[::-1]

    nestedest = {'i': None, 'depth': None}
    for i in range(len(chunk)):
        end = i + len(word)
        if not word == chunk[i:end]:
            continue

        depth = 0
        if i > 0 and word in chunk[i-2:i] + chunk[end:end+3]:
            # a parent is present
            depth = get_depth(chunk, word, i)
        if depth > nestedest['depth']:
            nestedest = {'i': i, 'depth': depth}

    chunk = chunk[:nestedest['i']] + chunk[nestedest['i']+len(word):]
    return answer(chunk[::-1], word[::-1])


def get_depth(chunk, word, i, depth=0):
    ''' find the nest depth of an instance of a word '''
    if word in chunk[i-(len(word)-1):i] + chunk[i+len(word):i+(2*len(word)-1)]:
        if i == 0:
            return depth + 1
        else:
            return depth + get_depth(chunk[:i] + chunk[i+len(word):], word, i-1, depth=depth+1)
    else:
        return depth + 1
