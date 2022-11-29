
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# ******************************
flag = 0
for i in range(len(num2)):
    if num2[i] not in num1:
        print(False)
        break
    else:
        if i == len(num2)-1:
            print(True)
        else: 
            continue

        
 

# print ('True') or print ('False')
