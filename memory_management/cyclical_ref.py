
# cyclical Reference >>> 2 ref points to each other
# can not detected by ref count carbage collection type alone
class Cycle:
    def __init__(self,value):
        self.value = value

    def child(self,child):
        self.child = child


x = Cycle("x")
y = Cycle("Y")
z = Cycle("z")

x.child(y)
y.child(z)
z.child(y)