class Employee:
    '所有员工的基类'
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print('Total Employee %d' % Employee.empCount )
    def displayEmployee(self):
        print('name :',self.name,'salary:',self.salary)

emp1 = Employee('hehe',2000)
emp2 = Employee('haha',3000)

emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
print(emp2.empCount)
print(Employee.empCount)
setattr(Employee,'age',10)
setattr(emp1,'age',20)
print(emp1.age)
print(emp2.age)
print(Employee.age)
print(Employee.__dict__)
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)

class Parent:
    '这是父类'
    parentAttr = 100
    def __init__(self):
        print('调用父类构造函数')
    def parentMethod(self):
        print('调用父类方法')
    def setAttr(self, attr):
        Parent.parentattr = attr
    def getAttr(self):
        print('父类属性 ：', Parent.parentAttr)

class Child(Parent):
    '这是子类'
    def __init__(self):
        print('调用子类构造函数')
    def childMethod(self):
        print('调用子类方法')

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

class Vector:
    __hehe = 1
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):# 这个真是666666
        return 'Vector (%d,%d)' % (self.a, self.b)
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(1, 1)
v2 = Vector(2, 2)
print(v1._Vector__hehe)
print(v1 + v2)
