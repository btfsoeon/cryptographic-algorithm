

UNICODE_SIZE = pow(2,16)*17-1


def shift_cipher(ptext, key):
    nkey = ord(key)
    result = ''
    for t in ptext:
        i = ord(t)
        ni = (i + nkey) % UNICODE_SIZE
        result = result + chr(ni)
    return result


def shift_decipher(etext, key):
    nkey = ord(key)
    result = ''
    for t in etext:
        i = ord(t)
        ni = (i - nkey) % UNICODE_SIZE
        result = result + chr(ni)
    return result


def vigenere_cipher(ptext, key):
    snkey = str(ord(key))
    result = ''
    for i in range(len(ptext)):
        t = ptext[i]
        ri = i % len(snkey)
        k = snkey[ri]
        ti = ord(t)
        nti = (ti + int(k)) % UNICODE_SIZE
        result = result + chr(nti)
    return result


def vigenere_decipher(etext, key):
    snkey = str(ord(key))
    result = ''
    for i in range(len(etext)):
        t = etext[i]
        ri = i % len(snkey)
        k = snkey[ri]
        ti = ord(t)
        nti = (ti - int(k)) % UNICODE_SIZE
        result = result + chr(nti)
    return result


# def affine_cipher(ptext, key):
