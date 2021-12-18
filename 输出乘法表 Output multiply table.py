a = 1
b = 1
while a <= 9:
    while b <= a:
        c = a*b
        print('%d*%d=%d' %(b, a, c),end='\t')
        b += 1
    a += 1
    print()
    b = 1