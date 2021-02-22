string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"] 
new_list=[]
for i in range(len(string_list)):
    if string_list[i] not in new_list:
        new_list.append(string_list[i])
print(new_list)

