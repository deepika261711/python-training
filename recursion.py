'''class MethodOverride1:
    def display(self):
        print("method invoked from base class")

class MethodOverride2(MethodOverride1):
    def display(self):
        print("method invoked from derived class")

ob = MethodOverride2()
ob.display()'''
def kk(n):
    if n==5:
        return
    kk(n+1)
    print((n))
kk(1)
