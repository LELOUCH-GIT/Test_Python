import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
try:
    print(re.match('com', 'www.runoob.com').span())  # 不在起始位置匹配
except:
    print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配
    print('傻逼，你刚才出错了')
finally:
    print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
    print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配
