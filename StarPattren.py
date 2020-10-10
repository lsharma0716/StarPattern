# right triangle pattren

n = int(input('Enter number of rows: '))
for i in range(n):
    print(''.center(i+1,'*'))
print()

# inverse triangle
for i in range(n):
    print(' '.rjust(n-i,'*'))

#tree pattren
def pattren(n):
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=' ')
        k = k- 1
        for j in range(0, i +1):
            print('* ', end='')
        print('\r')
pattren(n)
