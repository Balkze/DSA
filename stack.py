class stack:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return len(self.items)==0
    
    def push(self,items):
        self.items.append(items)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")
    def size(self):
        return len(self.items)

dtack=stack()
print("stack is empty?",dtack.is_empty())

dtack.push(2)
dtack.push(5)
dtack.push(3)
print("stack",dtack.items)

print("top of stack",dtack.peek())
print("pop",dtack.pop())
print("stack after pop",dtack.items)
