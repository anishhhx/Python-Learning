
>>> s1 = {1,2,3,4,5}
>>> s1
{1, 2, 3, 4, 5}
>>> s2 = {1,2,3}
>>> help(s1.isdisjoint)
Help on built-in function isdisjoint:

isdisjoint(...) method of builtins.set instance
    Return True if two sets have a null intersection.

>>> s1
{1, 2, 3, 4, 5}
s
>>> 2
2
>>> s2
{1, 2, 3}
>>> s3 = {10,20,30}
>>> s3
{10, 20, 30}
>>> s1
{1, 2, 3, 4, 5}
>>> # we are going to check, unique ness of 2 sets
>>> s3.isdisjoint(s1)
True
>>> # in s3 and s1 we dont have any common value
>>> # hence answer is True
>>> s1.isdisjoint(s2)
False
>>> ##############
>>> help(s1.issubset)
Help on built-in function issubset:

issubset(...) method of builtins.set instance
    Report whether another set contains this set.

>>> s1
{1, 2, 3, 4, 5}
>>> s2
{1, 2, 3}
>>> s2.issubset(s1)
True
>>> s1.issubset(s2)
False
>>> ###################
>>> ##########################
>>> # Dictionary
>>> # Dict
>>> # Syntax:
>>> {}
{}
>>> type({})
<class 'dict'>
>>> set()
set()
>>> ######
>>> {}
{}
>>> dict()
{}
>>> ######
>>> # Features of dict
>>> # dict is a combinition of 2 things
>>> # key and value
>>> {1,2,3}
{1, 2, 3}
>>> type({1, 2, 3})
<class 'set'>
>>> #{key:value}
>>> ##{key:value,key:value,key:value,key:value}
>>> {1:10,2:20,3:30}
{1: 10, 2: 20, 3: 30}
>>> type({1: 10, 2: 20, 3: 30})
<class 'dict'>
>>> ############################
>>> # Dict can contain multiplekey value pair
>>> # there is no inherent limit
>>> # Duplicate keys are not allowed
>>> {1:100,2:200,1:'ABC'} # key 1 appears twice
{1: 'ABC', 2: 200}
>>> # rzn: Background data structure HASH TABLE
>>> # No array
>>> # No indexing
>>> # No slicing
>>> d = {1:10,2:20,3:30,4:40}
>>> d
{1: 10, 2: 20, 3: 30, 4: 40}
>>> len(d)
4
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    d[0]
KeyError: 0
>>> d[-1]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d[-1]
KeyError: -1
>>> # key playes a role of index
>>> d
{1: 10, 2: 20, 3: 30, 4: 40}
>>> d[3]
30
>>> d[1]
10
>>> d1 = {'name':'amol','age':23,'salary':34000}
>>> d1
{'name': 'amol', 'age': 23, 'salary': 34000}
>>> d1['salary']
34000
>>> # using key we can access values associated with it
>>> d2 = {1:[10,20,30,40]}
>>> d2
{1: [10, 20, 30, 40]}
>>> d2[1]
[10, 20, 30, 40]
>>> d2 = {1:{10,20,30,40}}
>>> d2
{1: {40, 10, 20, 30}}
>>> # Duplicate keys not allowed
>>> # but duplicate values are allowed
>>> # interview question
>>> d4 = {1:10,2:10,3:10}
>>> d4
{1: 10, 2: 10, 3: 10}
>>> {1: 10, 1: 10, 1: 10}
{1: 10}
>>> # if we have duplicate keys present in dict then it wil take
>>> # recent key value pair
>>> {1: 10, 1: 10, 1: 20}
{1: 20}
>>> {1:10,
     'A':'Renuka',
     'B':'Boss'}
{1: 10, 'A': 'Renuka', 'B': 'Boss'}
>>> ####################
>>> # Lets perform some operations over dict
>>> k = {}
>>> k
{}
>>> id(k)
1551175416064
>>> dir(k)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> help(k.update)
Help on built-in function update:

update(...) method of builtins.dict instance
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]

>>> k
{}
>>> k.update({'A':'Amol','C':'Chetan'})
>>> k
{'A': 'Amol', 'C': 'Chetan'}
>>> k.update({'A':'Amit'})
>>> k
{'A': 'Amit', 'C': 'Chetan'}
>>> id(k)
1551175416064
>>> # id is not changing hence it MUTABLE data type
>>> k
{'A': 'Amit', 'C': 'Chetan'}
>>> # i want to add manual data
>>> # dict[key]=value
>>> k['D'] = 'Deepak'
>>> k
{'A': 'Amit', 'C': 'Chetan', 'D': 'Deepak'}
>>> k['C'] = 'Chintamani'
>>> k
{'A': 'Amit', 'C': 'Chintamani', 'D': 'Deepak'}
>>> k['C'] = ['Chintamani','Chetak']
>>> k
{'A': 'Amit', 'C': ['Chintamani', 'Chetak'], 'D': 'Deepak'}
>>> # it accepts homo./hetro data
>>> k['D'] = ['Deepak',700]
>>> k
{'A': 'Amit', 'C': ['Chintamani', 'Chetak'], 'D': ['Deepak', 700]}
>>> #########################
>>> d
{1: 10, 2: 20, 3: 30, 4: 40}
>>> # How to access the values from dict
>>> # using method get
>>> d.get(1)
10
>>> d.get(3)
30
>>> d.get(30)
>>> help(d.get)
Help on built-in function get:

get(key, default=None, /) method of builtins.dict instance
    Return the value for key if key is in the dictionary, else default.

>>> # if key is present , return its value
>>> # if key is not present then return None
>>> d
{1: 10, 2: 20, 3: 30, 4: 40}
>>> d.get(2)
20
>>> d.get(20,'Not present')# key 20 is not present
'Not present'
>>> d.get(100,-1)
-1
>>> d
{1: 10, 2: 20, 3: 30, 4: 40}
>>> # mannual way
>>> #d[key]
>>> d[2]
20
>>> d[4]
40
>>> d[34]
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    d[34]
KeyError: 34
>>> ######################
>>> k
{'A': 'Amit', 'C': ['Chintamani', 'Chetak'], 'D': ['Deepak', 700]}
>>> k['C']
['Chintamani', 'Chetak']
>>> k['C'][0]
'Chintamani'
>>> k['C'][-1]
'Chetak'
>>> k['C'][-1] = 'Chinta'
>>> k
{'A': 'Amit', 'C': ['Chintamani', 'Chinta'], 'D': ['Deepak', 700]}
>>> k['C'][0]
'Chintamani'
>>> k['C'][0].upper()
'CHINTAMANI'
>>> # Amit(identifier) ---- 'Amit'(string/object)
>>> Amit = 'Amit'
>>> {1:Amit}
{1: 'Amit'}
>>> 
