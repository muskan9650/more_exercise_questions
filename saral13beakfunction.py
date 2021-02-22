def break_word(n):
    var=n.split()
    return var
sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
print(break_word(sentence))





words = "navgurukul is great"
counter = 0
while counter < len(words):
    print (words[counter], end=" ") 
    counter+=1