class queuelist:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items)==0
    
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self,item):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty")
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return len(self.items)
q=queuelist()
q.enqueue(12)
q.enqueue(13)
q.enqueue(14)
q.enqueue(34)
print(q.items)
print(q.peek())
q.dequeue(14)
print(q.peek())
print(q.items)