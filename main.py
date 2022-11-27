
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# ******************************
flag = 0
for i in range(len(num2)):
    if num2[i] not in num1:
        continue
    else:
        print('False')
        break
else:
    print('true')
# ******************************

# print ('True') or print ('False')
