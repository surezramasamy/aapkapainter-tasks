array =[1,2,2,3,0,2,0]
num = set()
for i in array:
    if i in num:
        print(i)
        break
    else:
        num.add(i)
