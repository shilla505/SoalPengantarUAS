def mystery(n, m):
    p = 0
    e = 0

    while e < n:
        p += 1
        e += m
    return p

print(mystery(4, 3)) 