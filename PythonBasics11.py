
>>> # Dict methods
>>> # {key:value}
>>> # Sequence order is preseved
>>> d = {1:100,'A':'ABC',0:200}
>>> d
{1: 100, 'A': 'ABC', 0: 200}
>>> # accepts homo./hetro data
>>> # dir(d)
>>> dir(d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> # suppose if we want to fecth keys of dict
>>> d
{1: 100, 'A': 'ABC', 0: 200}
>>> d.keys()
dict_keys([1, 'A', 0])
>>> # suppose if we want to fecth values of dict
>>> d.values()
dict_values([100, 'ABC', 200])
>>> ## suppose if we want to fecth key,value pair of dict as a tuple
>>> d.items()
dict_items([(1, 100), ('A', 'ABC'), (0, 200)])
>>> #################
>>> # Lets try to remove elements/pairs
>>> d
{1: 100, 'A': 'ABC', 0: 200}
>>> d.pop(1)
100
>>> d
{'A': 'ABC', 0: 200}
>>> d.pop(1) # already key 1 and its value removed
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d.pop(1) # already key 1 and its value removed
KeyError: 1
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> # pop(key) needs a key--> return value
>>> #############
>>> d
{'A': 'ABC', 0: 200}
>>> help(d.popitem)
Help on built-in function popitem:

popitem(...) method of builtins.dict instance
    D.popitem() -> (k, v), remove and return some (key, value) pair as a
    2-tuple; but raise KeyError if D is empty.

>>> d.popitem()
(0, 200)
>>> d
{'A': 'ABC'}
>>> d.popitem()
('A', 'ABC')
>>> d
{}
>>> d.popitem()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d.popitem()
KeyError: 'popitem(): dictionary is empty'
>>> ##################
>>> #fromkeys
>>> help(dict.fromkeys)
Help on built-in function fromkeys:

fromkeys(iterable, value=None, /) method of builtins.type instance
    Create a new dictionary with keys from iterable and values set to value.

>>> t = ['supriya','rakesh','umesh','shital']
>>> t
['supriya', 'rakesh', 'umesh', 'shital']
>>> dict.fromkeys(t)
{'supriya': None, 'rakesh': None, 'umesh': None, 'shital': None}
>>> dict.fromkeys(t,100)
{'supriya': 100, 'rakesh': 100, 'umesh': 100, 'shital': 100}
>>> h = [10,20,30,40]
>>> dict.fromkeys(h)
{10: None, 20: None, 30: None, 40: None}
>>> dict.fromkeys(h,'value')
{10: 'value', 20: 'value', 30: 'value', 40: 'value'}
>>> dict.fromkeys(h,[1,2,3])
{10: [1, 2, 3], 20: [1, 2, 3], 30: [1, 2, 3], 40: [1, 2, 3]}
>>> #####################
>>> # Interview question
>>> t = [(1,20),(2,40),(3,300)]
>>> t
[(1, 20), (2, 40), (3, 300)]
>>> dict(t)
{1: 20, 2: 40, 3: 300}
>>> ############
>>> a1 = ['A','B','C']
>>> a1
['A', 'B', 'C']
>>> b1 = [10,20,30]
>>> # create a dict in a such way: elements of a1 should be key and elements of b1 should be value
>>> dict(a1:b1)
SyntaxError: invalid syntax
>>> dict.fromkeys(a1,b1)
{'A': [10, 20, 30], 'B': [10, 20, 30], 'C': [10, 20, 30]}
>>> help(zip)
Help on class zip in module builtins:

class zip(object)
 |  zip(iter1 [,iter2 [...]]) --> zip object
 |  
 |  Return a zip object whose .__next__() method returns a tuple where
 |  the i-th element comes from the i-th iterable argument.  The .__next__()
 |  method continues until the shortest iterable in the argument sequence
 |  is exhausted and then it raises StopIteration.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> a1
['A', 'B', 'C']
>>> b1
[10, 20, 30]
>>> zip(a1,b1)
<zip object at 0x000001A3D5855148>
>>> list(zip(a1,b1))
[('A', 10), ('B', 20), ('C', 30)]
>>> dict(zip(a1,b1))
{'A': 10, 'B': 20, 'C': 30}
>>> # if we have extra element in iterable
>>> a1
['A', 'B', 'C']
>>> c1 = [4,5,6,7]
>>> dict(zip(a1,c1))
{'A': 4, 'B': 5, 'C': 6}
>>> dict(zip(c1,a1))
{4: 'A', 5: 'B', 6: 'C'}
>>> ############
>>> help(d.setdefault)
Help on built-in function setdefault:

setdefault(key, default=None, /) method of builtins.dict instance
    Insert key with a value of default if key is not in the dictionary.
    
    Return the value for key if key is in the dictionary, else default.

>>> a = {4: 'A', 5: 'B', 6: 'C'}
>>> a
{4: 'A', 5: 'B', 6: 'C'}
>>> a.setdefault(4)
'A'
>>> a.setdefault(44)
>>> a
{4: 'A', 5: 'B', 6: 'C', 44: None}
>>> a.setdefault('python',1989)
1989
>>> a
{4: 'A', 5: 'B', 6: 'C', 44: None, 'python': 1989}
>>> a.setdefault('python')
1989
>>> 
