my_dict= {1:'apple',2:'banana'}
print(my_dict)

a= {'name':'apple',2:[1,2,3]}
print(a)

# using dict function
x= dict({1:'apple',2:'banana'})
print(x)

dec= dict([(1, 'apple'), (2, 'banana')])
print(dec)
print(dec[1])

dec['price']= 300
print(dec)

# pop(key) , popitem(), clear() del
sq= {1:1, 2:4, 3:9, 4:16, 5:25}
print(sq)
print(sq.pop(4))
print(sq.popitem())
print(sq.clear)

