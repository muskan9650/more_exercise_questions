#1 se 1000 tak saare numbers print karne ka loop likho. Lekin * Agar number 3 se divisible hai toh "nav" print karvao.
#Agar number 7 se divisible hai toh "gurukul" print karvao.
#Agar number 21 se divisible hai toh "navgurukul" print karvao.
i=0
while i<=1000:
    if i%3==0:
        if i%21==0:
            print(i, "navgurukul")
        else:
            print(i, "nav")
    elif i%7==0:
        if i%21==0:
            print(i, "navgurukul")
        else:
            print(i, "gurukul")
    i+=1