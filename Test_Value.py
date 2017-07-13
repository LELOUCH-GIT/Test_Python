a = b = c = [1, 2, 'jaune']
d, e, f = 1, 2, 'jaune'
print(a)
print(b)
print(c)
print("%d %d %s" % (d, e, f))
print(id(a))
print(id(b))
a[0]=3
print(a)
print(b)
str = 'I love my sister '
print(str[1:10])
print(str * 2)
print(a + b)
# 下面是字典
# 列表【】 元祖（） 字典{}
dict = {}
dict['one'] = "This is one"
dict[2]="This is two"
tinydict = {'name': 'john', 'code': 6754, 'dept': 'sales'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
x = 1, 2, 3
print(type(x))



