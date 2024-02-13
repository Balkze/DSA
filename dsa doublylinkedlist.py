class node:
  def __init__(self,data=None):
    self.data=data 
    self.next=None
    self.prev=None 
# ! doublyl linkidlist
class doublylinkedlist:
  def __init__(self):
    self.head=None
    self.tail=None
    
  def is_empty(self):
    return self.head is None
    
  def append(self,data):
    new_node=node(data)
    if self.is_empty():
      self.head=new_node
      self.tail=new_node
    else:
      new_node.prev=self.tail 
      self.tail.next=new_node
      self.tail=new_node
  def prepend(self,data):
    new_node=node(data)
    if self.is_empty():
      self.head=new_node
      self.tail=new_node
    else:
      new_node.next=self.head
      self.head.prev=new_node
      self.head=new_node
  def delete(self,data):
    if self.is_empty():
      return
    current=self.head
    while current is not None and current.data!=data:
      current=current.next 
    if current is not None:
      if current.prev is not None:
        current.prev.next=current.next
      else:
        self.head=current.next
      if current.next is not None:
        current.next.prev=current.prev
      else:
        self.tail=current.prev
  def display_forword(self):
    element=[]
    current=self.head
    while current:
      element.append(current.data)
      current=current.next
    print("->".join(map(str,element)))
  def display_backword(self):
    element=[]
    current=self.tail 
    while current:
      element.append(current.data)
      current=current.prev
    print("->".join(map(str,element)))

doublylist=doublylinkedlist()
doublylist.append(1)
doublylist.append(2)
doublylist.append(3)
doublylist.prepend(4)

doublylist.display_forward()
doublylist.dispaly_backword()
doublylist.delete(2)
doublylist.display_forward()
doublylist.dispaly_backword()
