
yr=int(input("enter year to be checked"))

if(yr%400==0 & yr%100==0 & yr %4==0):
    print("leap")

else :
    print("not leap")