import com.test.testclass

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        
print("******* Scope Test ******")       
def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

    
for c in reverse("a"):
    print(c)
    scope_test()
    print("In global scope:", spam)    

xx = com.test.testclass()
print(xx.fun("akbar"))    