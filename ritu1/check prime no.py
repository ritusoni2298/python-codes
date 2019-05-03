""" if the for loop is breaked by break than the else statement
of for will not be executed"""
"""for n in range (2,10):
    print('n=',n)
    for x in range(2,n):
        print('x=',x)
        if n%x==0:
            print(n,'equals',x,'*',n//x)
            break
    else:
        print(n,'is prime no')
"""

x=int(input("enter inetger"))

if(x==2 or x==3):
    print("prime no.")
else:
    for i in range(x):
        if(6*i+1 == x or 6*i-1 ==x):
            print("prime")
            break
    else :
            print("not prime")