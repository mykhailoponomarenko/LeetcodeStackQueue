class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        if self.head:
            item = self.head
            self.head = self.head.next
            return item
        raise ValueError('Queue is empty.')

    @property
    def peek(self):
        return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.item)+' '
            current = current.next
        return f'start -> {s}<- end'
class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q1.add(x)

        while not self.q2.is_empty():
            self.q1.add(self.q2.pop().item)
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q2.pop().item

    def top(self) -> int:
        return self.q2.peek

    def empty(self) -> bool:
        return self.q2.is_empty()

