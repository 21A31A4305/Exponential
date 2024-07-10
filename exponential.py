def exp(a,n):
    if(n==0):
        return 1
    elif(n==1):
        return a
    elif(a%2==1):
        return a*exp(a,n-1)
    else:
        return(a*a,n//2)
a=int(input())
n=int(input())
print(exp(a,n))
