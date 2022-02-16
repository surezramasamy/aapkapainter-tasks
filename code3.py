Sample_Input=str(input())
str1=Sample_Input.split(" ")[0].lower()
str2=Sample_Input.split(" ")[1].lower()

if(len(str1) == len(str2)):

    sort_str1 = sorted(str1)
    sort_str2 = sorted(str2)


    if(sort_str1 == sort_str2):
        print("Yes")
    else:
        print("No")
else:
    print("No")
