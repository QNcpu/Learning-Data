weight=float(input("Please input the weight:"))
waistline=float(input("Please input the waistline:"))

a=waistline*0.74
b=weight*0.082+34.89
BFM=a-b
BFR=(BFM/weight)*100
print(f"Body Fat Rate(lady)is:{BFR}%")

b=weight*0.082+44.74
BFM=a-b
BFR=(BFM/weight)*100
print(f"Body Fat Rate(man)is:{BFR}%")