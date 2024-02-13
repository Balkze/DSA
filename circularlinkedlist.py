class node:
  def __init__(self,data=None):
    self.data=data 
    self.next=None
# ! circular linkidlist
class circularlinkedlist:
  def __init__(self):
    self.head=None
    
  def is_empty(self):
    return self.head is None
    
  def append(self,data):
    new_node=node(data)
    if self.is_empty():
      self.head=new_node
      new_node.next=self.head
    else:
      current=self.head
      while current.next!=self.head:
        current=current.next
      current.next=new_node
      new_node.next=self.head

  def prepend(self,data):
    new_node=node(data)
    if self.is_empty():
      self.head=new_node
      new_node.next=self.head
    else:
      current=self.head
      while current.next!=self.head:
        current=current.next
      current.next=new_node
      new_node.next=self.head
      self.head=new_node
  def delete(self,data):
    if self.is_empty():
      return 
    if self.head.data==data:
      current=self.head
      while current.next!=self.head:
        current=current.next
      if self.head.next==self.head:
        self.head=None
      else:
        self.head=self.head.next
        current.next=self.head
    else:
      current=self.head
      while current.next !=self.head and current.next.data !=data:
         current=current.next
      if current.next.data==data:
        current.next=current.next.next 
  def display(self):
    elements=[]
    current=self.head
    if current:
      repeat=True
      while repeat:
        elements.append(current.data)
        current=current.next
        if current == self.head:
          repeat=False
    print("->".join(map(str,elements)))
    
  def search(self,target):
    if self.is_empty():
      return False 
    current=self.head
    repeat=True
    while repeat:
      if current.data==target:
        return True
      current=current.next
      if current == self.head:
        repeat=False      
    return False
circularlist=circularlinkedlist()
circularlist.append(10)
circularlist.append(20)
circularlist.append(30)
circularlist.append(40)
circularlist.append(50)
circularlist.append(60)
circularlist.append(70)
circularlist.append(80)
circularlist.append(90)
circularlist.display()
circularlist.prepend(0)
circularlist.delete(20)
circularlist.display()
