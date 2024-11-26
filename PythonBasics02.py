## operaters in python
'''
operaters are used to perform some operations.
types pf operaters in python:
1) Arithmetic operater
2) Assignment operater
3) Relational/conditional operater
4) Logical Operater
5) Membership Operater
6) Identity Operater
7) Bitwise Operater
'''
#-----------------------------------------------
# Arithmetic Operator + ,-, *, /, %, //, **
'''print('Addition 5 + 4 =',5+4)
print('substraction 5 - 4 = ',5-4)
print('multiplication 5 * 4 = ',5*4)
print('division 10/3 =',10/3)
print('floor division 10 // 3=',10//3)
print('exponential operator 5**2 = ',5**2)
print('mode operater which returns reminder',5%4)'''
#--------------------------------------------------
# Assignment operater: =,+=,-=,/=,//=,*=,**=
'''a = 100 # equal to operater
a = a + 100
# print(a)
b = 200
print(b)
b = b - 50
print(b)
a = 300
print(a)
a = a * 50
print(a)'''
#------------------------------------------
# Relational/ conditional operater : <, >, <=, >=, ==, !=
# always returns a boolean output
'''print(3 < 4)
print(34 <= 34)
print('Python'=='python')
print('Python' != 'python') # != indicates is not equal to.'''
#------------------------------------------------------------------
#Logical Operater : associated with conditional checking
# here we need the help of comparison operators
# 3 options: and or not
# It is based on Truth Table
# what is truth table
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
# name = 'snehal'
# age = 23
# now we check conditions
# print(name =='snehal' and age == 23)
# print(name == 'sneha' and age == 23)
'''value of True is 1 and value of false is 0
print(int(True))
print(int(False))
print('x' and 'y')'''
# if ur X is True then return Y
# False means 0,None, ''
# if ur X is False then return X
# print(2 and 0)
# print(None and 2)
#--------------------------------------
'''Membership Operater : it  checks either an element is a 
member of a sequence or not. It has 2 types in, not in'''
#print('jaya' in 'Hema malini')
# print(5 in [2,3,4,5,6])
# print(6 not in (3,4,2,5))
#----------------------------------
'''# Identity operator: its check id / address of an objects
if address matches then it results True otherwise False
it has 2 types: is , is not'''
#interview question : vvvimp
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
# print(x is z) # address equality
# print(id(x))
# print(id(z))
# print(y is not z)
# print(x is y) # content euality-