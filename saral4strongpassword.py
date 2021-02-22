# Fir check kariye ki user ka password sakht hai ya nahi. Ek sakht password ko yeh sab rule follow karne chaiye:
# 1.Kam se kam uski length 6 honi chaiye
# 2.Jada se jada length 16 se jyada na ho
# 3.Kam se kam ek dollar ka sign ($) hona chaiye
# 4.Kam se kam password mein 2 ya 8 hona chaiye
# 5.Password mein capital A ya capital Z hona chaiye
# 6.Agar password yeh rules follow kar raha hai toh "Strong Password" print karo, nahi toh "Weak Password" type karo
password=input("enter a password")
if len(password)>=6 and len(password)<=16:
    if "$" in password:
        if "2" in password  or "8" in password:
            if "A" in password or "Z" in password:
                print("strong password")
            else:
                print("week password, A or Z is require")
        else:
            print("week password, 2 or 8 is require ")
    else:
        print("week password, $ is require")
else:
    print("week password, password length should be 6")