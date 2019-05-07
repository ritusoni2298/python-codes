#methods of list

a=['hello','I','am','ritu','soni','I','am','happy']
#append
a.append(3)

print(a)
a.append(34)
a.append(4.45)
a.append(len(a))
a.append(True)
print(a)
x=a.append(56) #extend and append do not return anything x is none
print(x)

#extend(iterable)

b=[1,2]
x=a.extend(b)
print(x)

a.extend(b)
print(a)

#insert
a.insert(1,0)
print(a)

#remove parameter = value that we want to remove
a.remove('hello')
a.remove(1)
a.remove(2)

#pop parameter = index that we want to pop element from.
x=a.pop(8)
print(x)
#it removes the element from the list and return it
print(a)

#a.clear() clears whole list

#index

v=a.index('ritu',2)
print(v)

#count

c=a.count(1)
print(c)

# cant sort the list with mixed values of str and int by a.sort()
a.reverse()
print(a)

c=a.copy()
print(c)
z=[1,2,3,4,5,6]
print(z[-6:-3])
print(z[:])







