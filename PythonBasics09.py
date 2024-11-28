# Dictionary and its methods
# d1={}
# print(type(d1))
# x= dict()
# print(type(x))
# d1={'a':'anish','b':21}
# # # print(d1)
# x={1:'kk',2:{1,2,3}}
# # # print(x[2][0])
# # x.update({'a':'anish'})
# x.clear()
#  print(x)
# -------------------------------------------------------------/
d1={}
d1['a']= 20
d1[25]='ani'
# print(d1)
# get function to fetch the value by accessing it
# print(d1.get(20))      not present key then none in get and error in manual
# d1[25]=200      upddate any value
# print(d1)
d={'a':'anish','b':'football'}
# print(d['a'].upper())   temporary change
# print(d.keys())
# print(d.values())
# print(d.items())
# print(d.popitem())
# print(d)
# convert any  list to dict
# x=['amit','shety','golly']
# print(dict.fromkeys(x,10))
# zip function  list to dict
a1={1:2,3:4}
b1=[11,22,33,44]
c1=zip(a1,b1)
print(dict(c1))
# setdefault--add any key and value to dict
a1.setdefault(5,'job')
print(a1)
print(dir(a1))
# mc

