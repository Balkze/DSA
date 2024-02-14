class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class stacklinkedlist:
    def __init__(self):
        self.top=None
        
    def is_empty(self):
        return self.is_empty is None
    
    def push(self,item):
        new_node=node(item)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if not self.is_empty():
            pop_item=self.top.data
            self.top=self.top.next
            return pop_item
        else:
            raise IndexError("pop from an empty stack")
    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError("peek from empty stack")
    def size(self):
        count=0
        current=self.top
        while current:
            count+=1
            current=current.next
            
        return count
sl=stacklinkedlist()
sl.push(23)
sl.push(43)
sl.push(253)
sl.push(237)
sl.push(283)
sl.push(2663)
print("top",sl.peek())
print("size",sl.size())
print("pop",sl.pop())
        