#input ka use kar ke 3 alag variables mein 3 integers ka input lein. Input lene ke baad inn 3 mein se 
#sabse bade number ko print karo Note: Isme aap loops ka use nahi kar sakte.
num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
if num1>num2 and num1>num3:
    print("num1 is greater")
elif num2>num1 and num2>num3:
    print("num2 is greater")
elif num3>num2 and num3>num1:
    print("num3 is greater")
else:
    ("among are equal")




