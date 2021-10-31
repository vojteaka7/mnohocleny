# l[i] < p[j]

def is_bigger_than(a, b):
    a = (a[0], sorted(a[1]))
    b = (b[0], sorted(b[1]))

    stupen_a = a[1][0][0]
    stupen_b = b[1][0][0]

    if stupen_a > stupen_b:
        return True
    elif stupen_a < stupen_b:
        return False
    else:
        pismena = [a[1][0][1], b[1][0][1]]
        if pismena == sorted(pismena):
            return True
        else:
            return False

def merge(l, p):
    i = 0
    j = 0
    r = []

    while i != len(l) and j != len(p):
        if is_bigger_than(l[i], p[j]):
            r.append(l[i])
            i += 1
        else:
            r.append(p[j])
            j += 1

    while i != len(l):
        r.append(l[i])
        i += 1

    while j != len(p):
        r.append(p[j])
        j += 1

    return r

def mergesort(l):
    n = len(l)

    # base case
    if len(l) == 1:
        return l

    # dělení pole na poloviny
    leva, prava = l[:n//2], l[n//2:]

    leva = mergesort(leva)
    prava = mergesort(prava)

    # slévání
    vysledek = merge(leva,prava)

    return vysledek
