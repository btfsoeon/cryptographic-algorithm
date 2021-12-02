
index = list(range(26))
alphabets = ['a','b','c','d','e','f','g','h','i','j'
            ,'k','l','m','n','o','p','q','r','s','t'
            ,'u','v','w','x','y','z']
FROM_INDEX_TO_ALPB = dict(zip(index, alphabets))
FROM_ALPB_TO_INDEX = dict(zip(alphabets, index))
N_ALPHABET = 26


def shift_cipher(ptext, key):
    #TODO if key is integer
    result = ''
    for t in ptext:
        # only valid for alphabets
        #TODO case sensitive
        if t not in alphabets:
            result = result + t
            continue
        i = FROM_ALPB_TO_INDEX[t]
        ni = (i + int(key)) % N_ALPHABET
        result = result + FROM_INDEX_TO_ALPB[ni]
    return result


def shift_decipher(etext, key):
    #TODO if key is integer
    result = ''
    for t in etext:
        # only valid for alphabets
        #TODO case sensitive
        if t not in alphabets:
            result = result + t
            continue
        i = FROM_ALPB_TO_INDEX[t]
        ni = (i - int(key)) % N_ALPHABET
        result = result + FROM_INDEX_TO_ALPB[ni]
    return result


def vigenere_cipher(ptext, key):
    #TODO if key is integer
    result = ''

    for i in range(len(ptext)):
        t = ptext[i]
        ri = i % len(key)
        k = key[ri]
        if t not in alphabets:
            result = result + t
            continue
        ti = FROM_ALPB_TO_INDEX[t]
        nti = (ti + int(k)) % N_ALPHABET
        result = result + FROM_INDEX_TO_ALPB[nti]

    return result


def vigenere_decipher(etext, key):
    #TODO if key is integer
    result = ''

    for i in range(len(etext)):
        t = etext[i]
        ri = i % len(key)
        k = key[ri]
        if t not in alphabets:
            result = result + t
            continue
        ti = FROM_ALPB_TO_INDEX[t]
        nti = (ti - int(k)) % N_ALPHABET
        result = result + FROM_INDEX_TO_ALPB[nti]

    return result
