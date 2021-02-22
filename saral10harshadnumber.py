def harshad(k):
    i=1
    while i<=k:
        sum=0
        n=i
        j=1
        while j<=i:
            sum = sum + n%10
            n=n//10
            j=j+1
        if i%sum==0:
            print(i, "harshid number")
        i+=1

harshad(100)



