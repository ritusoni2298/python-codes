tel={'jac':1,'sym':2}
tel['u']=3
tel['c']=4
print(tel)
print(tel['jac'])

del tel['c']
print(tel)
tel['x']=5
tel['b']=7

sorted(tel)
print(tel)

w=dict([('hello',1),('yes',2),('you',3)])
print(w)

#dict compreshensions

print(x: x**3 for x in (3,4,5))




for k in knights.items():
    print(k)


for w,e in enumerate(knights):
    print(w,e)

for r,y in enumerate([1,2,34,45]):
    print(r,y)

x=list(knights)

print(x)

print(sorted(knights))

print('gm' in knights)
print('ritu' in knights)

question=['a','b','c','d']
print(type(question))
answer=['one','two','three']

for a,b in zip(question,answer):
    print(a,b)

for x in zip(question,answer):
    for c in x:
        print(c,x)
        print(type(x),type(c))
        #traversed through both the values

b="my name is z"

knights={'hello':'ritu','gm':'rishabh sir'}
i=[9,4,6,2,3]
#problem occured
p=set(i)
print(p)
for i in knights.items():
    print(i)

print(i)
#cz python is a interpreter language
for j in i:
    print(j)

print(j)
#problem till here


te=1,3,5,7,9
for c in reversed(range(1,10,2)):
    print(c)
 basket=['set','pen','bat','hello','table','pen']

n={x : x*2 for x in basket }

for q,w in n.items():
    print(q,w)




