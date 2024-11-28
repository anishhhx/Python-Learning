''' list: Lists are used to store multiple items in a single variable
how to declare list: it is declare with square bracket []
Feature of a list
Background data structure is array hence it supports indexing
It supports slicing
List is a mutable,ordered datatype in python
'''
k = [10,20,30,40,50]
print(k)
print(type(k))
# ',' is a separeter in list
# k1 = [1 2 3 4]
# print(k1)
#--------------------------
# positive indexing
print(k[1],k[4])
#----------------------
# negative indexing
print(k[-2])
#--------------------------
# slicing
l1 = ['ramesh','suresh','mahesh','ganesh','dinesh']
print(l1[:4])
l2 = [1,3,4,54,65,35,76,98,67,45]
print(l2[::-1]) # for reversing list
print(l2[-2:-4:-1])
# it accepts homogeneus/hetorogeneus values
w = [12,34.5,'python',4+5j]
# w list contains int,float,string,complex
#------------------------------------------------
# It preserves sequence order
h = [1,2,3,4,5,6]
print(h)
h1 = [2,3,4,1,5,7,9]
print(h1)
# it allows duplicate values
d1 = [1,2,3,4,3,2,1]
print(d1)
# list is a mutable (changeable) datatype
c = [2,4,6,8,10,12,16]
print(c)
print(id(c))
c[-1] = 14
print(c)
print(id(c))
# lets replace 8,10 by 100,20
print(c[3:5])
c[3:5] = [100,20]
print(c)
#--------------------------------------
# when we are performing the changes in an object, and changes persist in the same object
# here new object is not required to save the changes
# then that data type is MUTABLE
#----------------------------------------------
# now if  i want to check all the methods of a list
# print(dir(c))
# append, clear, copy, count, extend, index, insert,
# pop, remove, reverse, sort
#  if we want to check doc. of any method from data structure then use help()
lst = []
# print(help(lst.append))
#---------------------------------------------------------------------------
lst.append('anish') # if you print this statement then it returns None
print(lst) # you have to print list to see appended object
#---------------------------------------------------------
lst.clear()
print(lst) # clear all objects present in list
#---------------------------------------------------
a = ['A',12,30,50,100,'B']
print('this is list a', a)
print('this is id of a', id(a))
# copy method is used to create a new copy of ur object
# new object will have same elements as that of old one
b = a.copy()
print('this is list b',b)
print('this is id of b', id(b))
#  here id's are different, this is a deep copy.
# means a new object with same element gets created
#------------------------------------------------------
# now lets try to change any list
b[0] = 'Amit'
print(b)
# now check list a
print(a)
# copy() creates an individual objects using same data
#-----------------------------------------------------------
# now i want to creat object with same value and same id
c = a
print(c)
print('id of a:', id(a),',','id of c:', id(c))
# here we have same id's. this is known as shallow copy.
# hence changes performed in any of the object persist in both
a[-1] = 'bipin'
print('this is list a', a)
print('this is list c', c)
# interview question : what is shallow copy and deep copy ?
''' 
A shallow copy of a list creates a new list object but does not create 
copies of the elements within the original list. Instead, it copies 
references to the objects in the original list. As a result, changes 
made to the elements within the copied list may affect the original list 
and vice versa if the elements are mutable objects 
(e.g., lists, dictionaries, custom objects).
'''
import copy

original_list =
shallow_copy = copy.copy(original_list)

# Modifying an element in the shallow copy affects the original list.
shallow_copy[1][0] = 99
print(original_list)  # Output: [1, [99, 3], 4]

'''
A deep copy of a list creates a completely independent duplicate of the 
original list, including all the nested objects within it. It recursively
copies all the elements and their sub-elements, ensuring that changes to 
the copied list or its elements do not affect the original list.
'''

original_list = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original_list)

# Modifying an element in the deep copy does not affect the original list.
deep_copy[1][0] = 99
print(original_list)  # Output: [1, [2, 3], 4]
