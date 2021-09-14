x = int(input("Key an integer to count the element numbers over than 1: "))
el_num = list(range(2, x+1))
for i in range(len(el_num)):
    if(el_num[i] == 0):
        continue
    if(el_num[i] ** 2 > x):
        break
    for j in range(((i + 2) ** 2 - 2), len(el_num)):
        if(el_num[j] == 0):
            continue
        if(el_num[j] % el_num[i] == 0):
            el_num[j] = 0
while 0 in el_num:
    el_num.remove(0)
print(el_num)
