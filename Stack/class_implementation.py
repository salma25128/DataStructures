class Stack:
   def __init__(self):
       self.stack=[]

   def push(self,element):
       self.stack.append(element)

   def pop(self):
       if len(self.stack)<1:
           return None
       return self.stack.pop()

   def size(self):
       return len(self.stack)


stack_build=Stack()
stack_build.push('h')
stack_build.push('e')
stack_build.push('l')
stack_build.push('l')
stack_build.push('0')
stack_build.pop()

print(f'stack: {stack_build.stack}')
print(stack_build.size())
