
# مجموعة متناسقة مرنة قابلة للتغيير(Mutable)
# array is not builtin python datastructure but we can implement it by array module.
# ana zy list f kol haga ela etnen ('datatypes', 'typecode')
# > 1-store only items that are of the same single data type.
# >>2- The type is specified at object creation time by using a type code('i', 'd' , .........)

# from array import *           #>> importing all the functionalities available just call array()
# import array                  #>> array.array() or

import array as arr             # >>> define an alias name as(arr)


a = arr.array('i',[1,2,25,9,10,8])


# access data by index / know memory location
# array base address+single value stores count * index
# single value stores count = number of array elements
print(id(f" array base address = {a}"))
print(f" index[1] = {139816498015664+6*1}")

# ------------------------------------------------------------------

a.insert(1,2)
print(f"insert takes 2 args index,value: {a} hello it's grow")
print(id(f" array base address = {a}"))


a.append(5)
print(f"append-add one single value at the end of an array{a} it's grow tany")

print(id(f" array base address = {a}"))


#a.extend([6,8,'s'])
#print(a)  #it will pombing in your face it's arraaaay pro no existance for strangers

a.extend([6,8,12])
print(f"extend-takes an iterable{a} it's grow talt")

a.remove(2)
print(f"remove- remove first element only{a} hello it's shrink now")

a.pop(4)
print(f" pop remove the last item if no parameter(index) {a}" )

b = [0] * 5
print(b)





