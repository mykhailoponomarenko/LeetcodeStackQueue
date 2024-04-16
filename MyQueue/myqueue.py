class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        item = self.head.item
        self.head = self.head.next
        return item

    @property
    def peek(self):
        return self.head.item

    def __len__(self):
        count = 0
        cur = self.head
        while cur is not None:
            count +=1
            cur = cur.next
        return cur

    def __str__(self):
        s = ''
        cur = self.head
        while cur is not None:
            s = str(cur.item) + ' ' +s
            cur = cur.next
        return 'bottom -> '+ s+'<- top'
class MyQueue:


    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        

    def push(self, x: int) -> None:
        self.stack1.push(x)
        

    def pop(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
        

    def peek(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek

    def empty(self) -> bool:
        return self.stack1.is_empty() and self.stack2.is_empty()
