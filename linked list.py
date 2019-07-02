class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self, item):
        if self.head==None:
            self.head=Node(item)
        else:
            z=self.head
            while z.next!=None:
                z=z.next
            z.next=Node(item)

    def display(self):
        if self.head==None:
            print('Linked list is empty')
        else:
            z=self.head
            while z!=None:
                print(z.data)
                z=z.next     

    def delete(self,item):
        if self.head.data==item:
            self.head=self.head.next
        else:
            z=self.head
            while z.next!=None and z.next.data!=item:
                z=z.next
            if z.next==None:
                print('No item matched')  
            else:      
                z.next=z.next.next   
        
    def update(self,initialData, finalData):
        z=self.head
        while z.next!=None and z.data!=initialData:
            z=z.next
        if z.data!=initialData:    
            z.data=finalData
            print('Updated Succesfully')    
        else:
            print('Item not Found')    

    def size(self):
        self.s=0
        z=self.head
        while z!=None:
            self.s+=1
            z=z.next
        print('Size of linked list is '+str(self.s))

    def search(self, item):
        z=self.head
        self.position=1
        while z!=None and z.data!=item:
            z=z.next
            self.position+=1
        if z!=None:
            print('Item found at postion '+str(self.position))
        else:
            print('Item not found')
                   



l1=LinkedList()
l1.insert('apple')
l1.insert('banana')
l1.insert('orange')
l1.insert('Merc')
l1.insert('BMW')
l1.insert('Audi')

l1.display()
l1.delete('apple')
print('------------------------------------')
l1.display()
print('------------------------------------')
l1.update('xxx', 'Mercedes')
l1.display()

l1.size()

l1.search('BMW')