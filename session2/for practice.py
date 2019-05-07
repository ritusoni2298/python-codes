words=['cat','window','def']
for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w)>4:
        words.insert(0,w)

print(words)


print(range(0,5))
#this will print only range(0,5)
# to print values we write

print(list(range(0,6)))

"""the else keyword in for loop specifies 
a block of code to be executed 
after the loop is finished"""
for i in range(4):
    print(i)
else:
    print("finally executed")


