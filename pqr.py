class p:
    def m1(self):
        print('parent')


class i1(p):
    def m3(self):
        print('intermediate cls')

class i2(i1):
    def m4(self):
        print('intermediate cls')

class c(i2):
    def m2(self):
        print('child')

obj=c()
obj.m2()
obj.m4()
obj.m3()
obj.m1()





