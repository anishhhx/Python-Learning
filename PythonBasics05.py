l = ['jan', 'feb', 'march']
l.append('april')
# assign list to values
list_one = ['January', 'February', 'March']

# use the extend method
list_one.extend(['April', 'May', 'June'])

# displaying the list
print(list_one)
# assign list to values
list_one1 = ['January', 'February', 'March']

# use the extend method
list_one1.append(['April', 'May', 'June'])

# displaying the list
print(list_one1)
# --------------------------------------------------
c = [1,2,3,4,5]
c.append(6)
print(c)
# c.extend(6)
# print(c) extend does not accepts int,float,complex,boolean
c.extend([7])
print(c)
# Iterable ? it means a collection of multiple elements,objects
# on which we can perform iterations
list1 = []
list1.append('shital')
list1.extend('sheetal')
# -------------------------------------------
print(list1)
k = [10, 20, 10, 30, 40, 10, 1, 2, 3, 'A', 'B']
print(k.index('A'))
# ------------------------------------------------
k = [10, 20, 10, 30, 40, 10, 1, 2, 3, 'A', 'B']
k.insert(12,'C')
print(k)
#----------------------------------------------
# Interview question
# add element 90 between B and C using -ve indexing
#-------------------------------------------------------
print(k.pop()) # remove and return last element of list
print(k)
print(k.pop(0)) # remove element which is present at given index
print(k)
#print(k.pop(3,4)) # raise error coz pop allow only remove single index value
#-----------------------------------------------------------
# if we want to remove elemnt from list by giving element then
# use remove method
print(k)
k.remove(40)
print(k)
# remove is value based
# pop is index based
k.reverse()
print(k)
# reverse method made permenant change in list
# if you want to temporary change list then use slicing option
c1 = [12,24,36,48,60]
print(c1[::-1]) # this is temporary change
print(c1)
#-----------------------------------------------
# using builtin function reversed() we can reverse the sequence
c1 = [12,24,36,48,60]
print(list(reversed(c1))) # this is temporary changes
# ------------------------------------------------------
# difference between reverse() and reversed()
#-------------------------------------------------
# reverse():is a method of list
# reversed() is built in function (python)
#-----------------------------------------
# reveres(): in -place/ permanent changes
# reversed(): temp.
#----------------------------------------
# reverse() : does not return anything
# reversed(): returns output in the form of object
#---------------------------------------------------
# sort() :
d = [10,99,34,0,4,34,56,1,3]
print(d)
d.sort() # default is ascending
print(d)
# if want in descending order then used reverse=True
d = [10,99,34,0,4,34,56,1,3]
d.sort(reverse=True)
print(d)
#----------------------------------------------
f = [2,3,1,'A','d','g']
# f.sort() # list contains str and int not able to sort list
f1 = ['f','g','a','u']
f1.sort()
print(f1)
f1.sort(reverse=True)
print(f1)
string = ['shital','ram','om','prameela','rohan']
string.sort(key=len)
print(string)
# ------------------------------------------------------------------
# tuple : tuple having almost same feature as list except one
# list is mutable datatype
# tuple is immutable datatype
t1 = (1,2,3,4,5,6,7,8)
print(t1[2:6])
# t1[2] = 0
print(t1)
# tuple does not support item assignment
print(dir(()))
# only two methods of tuple : count, index
# list have many methods are used for direct manipulation of data
# hence list is mutable and tuple is immutable
a = 10,20,30
print(type(a)) # everything is comma seperated object is tuple
b = (23,)
print(type(b))
b = ('a',)
print(type(b))
# tuple allowed duplicates and all datatypes
t2 = ('a',23,34.57,6+5j,False)
print('type od t2:',type(t2))
# interview question :
# how to add new object in tuple
# method 1 : change into list
t3 = list(t2)
t3.append('67')
t2 = tuple(t3)
print(t2)
#----------------------------
# method 2 : add tuple to tuple
t4 = (True,)
t2 += t4 # t2 = t2 + t4
print(t2)
# ---------------------------------------------------
# count()
tup = (1,4,6,2,5,3,7,8,5,6,9,7,8,7,7)
print(tup.count(7))
print(t2 + tup)
# index()
print(tup.index(5))
#----------------------------------
t6 = (2,2,4,5)
print('this is size of tuple: ', t6.__sizeof__())
l1 = [2,2,4,5]
print('this is size of list:', l1.__sizeof__())
# interview qsn: why list take more memory than tuple ?
# interview qsn : which is faster list or tuple ?
#-------------------------------------------------------------
# packing and unpacking of tuple: vvvvvimp
print(type(23))
s1 = 10,34
print(type(s1))
# everything is comma seperated is tuple
#-----------------------------
# Packing: grouping multiple objects in a single identifier
film = 'kgf','nun','horror'
# Unpacking = opposite of packing means
# to unfold packed values, we need multiple identifiers
print(len(film))
x,y,z = film
print(x)
print(y)
print(z)
#------------------------------------------------------------
# string formating
name = "Alice"
age = 30
formatted_string = "Name: %s, Age: %d" % (name, age)
print(formatted_string)
# %s String Placeholder--> %s is used for formatting strings.
# It can be used to insert strings, numbers, or other data types,
# and Python will automatically convert them to strings.
#----------------------------------------------------------------
# %d integer placeholder
# %d is used for formatting integers. It is used to insert integer values into a string.
num = 42
formatted_string = "The answer is %d" % num
print(formatted_string)
# -----------------------------------------------------------------------
# %f Floating-Point Placeholder
# %f is used for formatting floating-point numbers (i.e., decimals)
# It allows you to control the number of decimal places.
price = 19.9956
formatted_string = "The price is %.2f dollars" % price
print(formatted_string)
# -----------------------------------------------------------------------
# Using f-strings
name = "Anish"
age = 22
formatted_string = f"Name: {name}, Age: {age}"
print(formatted_string)

num = 22
formatted_string = f"The age is {num}"
print(formatted_string)

cgpi = 8.98
formatted_string = f"The cgpi is {cgpi:.2f}"
print(formatted_string)


