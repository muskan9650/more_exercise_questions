list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
list3=[]
for i in range(len(list2)):
    if list2[i] in list1:
        list3.append(list2[i])
print(list3)