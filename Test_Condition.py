import time
import calendar
num = 5
if num == 3:
    print("3")
elif num == 5:
    print('5')
else:
    print('23333333333333')
print('hello')
#  这里我们也顺便测试循环(loop)
numbers = [1, 2, 3, 4, 5]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if(number%2 == 0):
        even.append(number)
        print(number)
    else:
        odd.append(number)
        print(number)

for letter in 'Python':
    print(letter)
fruits = ['A', 'B', 'C']
for fruit in fruits:
    print(fruit)

prime = []
for num in range(2,100):  # 迭代 2 到 100 之间的数字
    for i in range(2,num): # 根据因子迭代
        if num%i == 0:      # 确定第一个因子
            break            # 跳出当前循环
    else:                  # 循环的 else 部分
        prime.append(num)
print(prime)
ticks = time.time()
print(ticks)
localtime = time.localtime(time.time())
print(localtime)
cal = calendar.month(2016, 1)
print(cal)