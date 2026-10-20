numbers=[]
for i in range(7):
    number=int(input(f"Please input the {i+1} number:"))
    numbers.append(number)
data_range=max(numbers)-min(numbers)
average=sum(numbers)/len(numbers)
RR=(data_range/average)
print(RR)