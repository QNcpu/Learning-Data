def factorial (num):
    result=1
    if num==0:
        return(1)
    else:
        for i in range(1,num+1):
            result*=i
        return(result)

n=100
e=0
for i in range(n+1):
    i=factorial(i)
    e+=1/i
print(e)