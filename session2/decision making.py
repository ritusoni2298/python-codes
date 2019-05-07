y=int(input("please enter int "))

if y<0 :
    y=0
    print("negative value")
elif y==0 :
    print("zero")
elif y==1 :
    print("single")
else :
    print("more")

words=['cat','window','def']
inte=[1,2,3]
for w in words :
    for x in inte:
        print(w,len(w),x)

