list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
list3=[]

for i in range(len(list1)):
    if list1[i] not in list3:
        list3.append(list1[i])
for j in range(len(list2)):
    if list2[j] not in list3:
        list3.append(list2[j])
print(sorted(list3))
