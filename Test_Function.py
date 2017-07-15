def printme(str):
    print(str)
    return
def function(argl, *vartuple ):
    print(argl)
    for var in vartuple:
        print(var)
    return
sum = lambda arg1, arg2: arg1 + arg2
print(sum(1, 2))
print(sum('a', 'b'))
printme('hello')
function(10)
function(10,20,30)
globalvar = 0
def set_global_var():
    global globalvar
    globalvar = 1
set_global_var()
print(globalvar)
