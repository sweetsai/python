class singlyLinkedListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
def deleteNode(llist,position):
    if position==0:
        llist=llist.next
    else:
        current=llist
        for _ in range(position-1):
            current=current.next
        current.next=current.next.next
    return llist
def printLinkedList(llist):
    current=llist
    while current is not None:
        print(current.data)
        current=current.next
n=8
elements=[20,6,2,19,7,4,15,9]
position_to_delete=3
head=singlyLinkedListNode(elements[0])
current=head
for data in elements[1:]:
    current. next =singlyLinkedListNode(data)
    current=current.next
print("original Linked List:")
printLinkedList(head)
head=deleteNode(head,position_to_delete)
print("\nLinked List after deletion:")
printLinkedList(head)
