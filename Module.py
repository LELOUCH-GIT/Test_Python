import test_module
print(dir(test_module))
print(test_module.__file__)
def test():
    a = 1
    b = 2
    c = 3
    print(locals())
    print(globals())
    return
test()
