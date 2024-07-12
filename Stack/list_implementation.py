# stack >>> like a pile of books >>you can only add(append) or remove(pop) from the top >>
#pop >>> O(n)
#append >>> O(1)
#extend >>> O(len of list)


stack = []
stack.append('k')                #len+=1 >> single entry
stack.append('c')
stack.append('a')
stack.append('t')
stack.append('s')
print(f"hello add to pile :{stack}")


stack.append('salma')
print(f"hello check len{stack}")
print(len(stack))

stack.extend('salma')              # len=n of elements
print(stack)
print(len(stack))

stack.pop()                   #by default pop fn remove the last element on the list if you dont pass index
stack.pop()
print(f"hello remove from pile:{stack}")


