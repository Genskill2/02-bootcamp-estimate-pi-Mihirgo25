def wallis(n):
    pi = 2
    for i in range(1,n+1):
        pi = pi * (4*(i*i))/(4*(i*i)-1)
    print(pi)