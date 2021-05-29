from random import *

def wallis(n):
    pi = 2
    for i in range(1,n+1):
        pi = pi * (4*(i*i))/(4*(i*i)-1)
    print(pi)

def monte_carlo(n):
    count_in = 0
    count_out = 0
    for i in range (1,n+1):
        x = random()
        y = random()
        if (x*x + y*y) <= 1:
            count_in  = count_in + 1
        else:
            count_out = count_out + 1
    pi = 4 * count_in/(count_out + count_in)
    print(pi)
