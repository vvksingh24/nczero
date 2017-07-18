f=dict()
f[1] = 1
f[2] = 1

def fib(n):
    
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        return f[n]
        
    if (f.get(n, None)):
        return f[n]
        
    k = (n+1)/2 if (n & 1)  else n/2
    
    f[n] = (fib(k)*fib(k) + fib(k-1)*fib(k-1)) if (n & 1) else (2*fib(k-1) + fib(k))*fib(k)
    
    return f[n]
t=input()
while t>0:
    n=input()
    print fib(n+2)%1000000007
    t-=1
