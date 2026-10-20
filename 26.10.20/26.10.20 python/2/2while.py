""" #1
for i in range(1,101):
    is_prime=True
    if i<2:
        is_prime=False
    else:
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
    if is_prime:
        print(i)
#2
num_input=input("Please input the numbers:")
num_list=[int(x) for x in num_input.split()]
num_list.sort()
print(list(num_list))
#3
for i in range(100,1000):
    hundreds=i//100
    tens=(i//10)%10
    units=i%10
    if hundreds**3+tens**3+units**3==i:
        print(i)
#3（2）
i=100
while i<1000:
    hundreds=i//100
    tens=(i//10)%10
    units=i%10

    if hundreds**3+tens**3+units**3==i:
        print(i)
    
    i+=1 """
#4
num_input=(input("Please input the numbers"))
num_list=[int(x) for x in num_input.split()]
num_list.sort(reverse=True)
print(list(num_list))