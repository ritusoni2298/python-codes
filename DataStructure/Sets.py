#a set is unordered collection with no duplicate elements

k={'a','b','c'}
x={'a','v','w','b','c','q'}

print(k<x)
print(x<k)

print(x | k)
print(x & k)
print(x ^ k)
print(x-k)

#with update()
#can be used with set but cant be used withj frozenset
x |= k
print(x)
x &= k
print(x)

#print(x ^=k)
#print(x -=k)

x.add('d')
print(x)
x.remove('a')
x.discard('c')
x.discard('h')
x.pop()
x.clear()

#set comprehensions

a={x for x in 'abracadabra' if x not in 'abc'}
print(a)

vowels={'a','e','i','o','u'}

fset=frozenset(vowels)
print(fset)

print(vowels | k)