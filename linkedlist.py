class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next
            
class MyLinkedList:

    


    def __init__(self):
        self.head = None
        self.tail = None

        

    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.val
            count += 1
            current = current.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val, None)
            self.tail = self.head
            return

        newHead = Node(val, None)
        newHead.next = self.Head
        self.head = newHead
        

    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.head = Node(val, None)
            self.tail = self.head
            return

        newtail = Node(val, None)
        self.tail.Next = newtail
        self.tail = newtail
        

    def addAtIndex(self, index: int, val: int) -> None:
        if self.head == None:
            self.head = Node(val, None)
            return

        newNode = Node(val, None)
        count = 0
        current = self.head
        prev = self.head

        while current:
            if count == index:
                newNode.next = current
                if count == 0:
                    self.head = newNode
                    return
                prev.next = newNode
                return
            prev = current
            current = current.next
        

    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return

        count = 0
        current = self.head
        prev = self.head

        while current:
            if count == index:
                prev.next = current.next
                if current.next == None:
                    self.tail = prev.next

                if count == 0:
                    self.head = None
                    self.tail = None
                    return
                return
            prev = current
            current = current.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)