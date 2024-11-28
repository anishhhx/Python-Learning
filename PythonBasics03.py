# String formatting
'''name = 'ramesh'
age = 33
print('my name is {}, my age is {}'.format(name, age))
c = 'my name is {} and my age is {}'
print(c.format(name, age))
# -----------------------------------
quantity = 4
itemno = 567
price = 1000
my_order = 'i want to pay {2} rs for {0} pieces of item no. {1}'
print(my_order.format(quantity, itemno, price))
# -----------------------------------------------------------
string = 'i have a {carname}, it is a {model}'
print(string.format(carname='ford', model='mustang'))'''
# ------------------------------------------------------
# string methods:  all string methods return the new value
# they do not change original string.
# 1) capitalize(): Converts the first character to upper case
string = 'livewire'
print(string.capitalize())
# 2) upper() : to convert string into upper case
print(string.upper())
# 3) lower() : to convert string into lower case
print(string.lower())
# 4) casefold()	Converts string into lower case
print(string.casefold())
str = 'ß'
print(str.lower())
print(str.casefold())
# 5) center()	Returns a centered string
# The center() method will center align the string,
# using a specified character (space is default) as the fill character.
# syntax : string.center(length, character)
print(string.center(20,'#'))
# 6) count():Returns the number of times a specified value occurs in a string
string = 'i love football, football is my favorite game'
print(string.count('football'))
# 7) endswith()	Returns true if the string ends with the specified value
print(string.endswith('game'))
# 8) The find() method finds the first occurrence of the specified value.
print(string.find('football'))
# The find() method returns -1 if the value is not found.
print(string.find('baseball'))
#
txt = "Hello, welcome to my world."
# 9) index() method also finds the first occurrence of the specified value.
# but if it raise exception if the value is not found
# print(txt.index('k'))
# 10) isalnum()	Returns True if all characters in the string are alphanumeric
string1 = '123good'
print(string1.isalnum())
# 11) isalpha
print(string1.isalpha())
name = 'ramesh'
print(name.isalpha())
# 12) isdigital()
age = '23'
print(age.isdigit())
height = '5.5'
print(height.isdecimal())