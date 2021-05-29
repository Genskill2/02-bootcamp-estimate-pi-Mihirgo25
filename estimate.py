from random import *

def wallis(n1):
    pi = 2
    for i in range(1,n1+1):
        pi = pi * (4*(i*i))/(4*(i*i)-1)
    print(pi)

def monte_carlo(n2):
    count_in = 0
    count_out = 0
    for i in range (1,n2+1):
        x = random()
        y = random()
        if (x*x + y*y) <= 1:
            count_in  = count_in + 1
        else:
            count_out = count_out + 1
    pi = 4 * count_in/(count_out + count_in)
    print(pi)

n1 = int(input("Enter Number of iterations: "))
n2 = int(input("Enter Numer of trials: "))
wallis(n1)
monte_carlo(n2)