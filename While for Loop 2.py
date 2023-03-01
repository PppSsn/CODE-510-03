A = 0
i = 1
while i <= 10:
    print('frame # %d'%i)
    n = int(input('Number of pins down in first ball:'))
    if n == 10:
        print('strike')
        i += 1
        A += n
    else:
        p = int(input('Number of pins down in second ball:'))
        q = n+p
        if q == 10:
            print('Spare')
            i += 1
            A += q
        else:
            print('Open frame')
            i += 1
            A += q
print('Total score %d'%A)
