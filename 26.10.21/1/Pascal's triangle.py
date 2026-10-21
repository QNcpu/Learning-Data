def generate_next_row(pre_row):
    if not pre_row:
        return([1])
    next_row=[1]
    for i in range(len(pre_row)-1):
        next_row.append(pre_row[i]+pre_row[i+1])
    next_row.append(1)
    return(next_row)

current_row=[]
for i in range(10):
    current_row=generate_next_row(current_row)
    print(current_row)