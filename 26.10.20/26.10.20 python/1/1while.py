#1
total=0
i=1
while i<=100:
    if i%3==0:
        total+=i
    i+=1
print(total)

#2
total=0
i=1
while i<=100:
    total+=i
    i+=2
print(total)

#3
num1=int(input("Please input the first number:"))
num2=int(input("Please input the second number:"))
if num1>num2:
    lcm=num1
else:
    lcm=num2
while True:
    if lcm%num1==0 and lcm%num2==0:
        break
    lcm+=1
print(f"{lcm}")

#4
num1=int(input("Please input the first number:"))
num2=int(input("Please input the second number:"))
if num1<num2:
    gcd=num1
else:
    gcd=num2
while gcd>0:
    if num1%gcd==0 and num2%gcd==0:
        break
    gcd-=1
print(gcd)

#5
num=int(input("Please input the number:"))
if num<=1:
    print("no")
else:
    i=2
    is_prime=True
    while i<num:
        if num%i==0:
            is_prime=False
            break
        i+=1
    if is_prime:
        print("yes")
    else:
        print("no")

