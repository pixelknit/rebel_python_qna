class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        pass
    #create a new node
    def push(self, value):
        newNode = Node(value)
        newNode.next = None
        return newNode

    #traverse and print the list
    def printList(self, head):
        while head is not None:
            print(head.value)
            head = head.next

    #insert a new node after you find a node with a specific value
    def insertAt(self, head, previousValue, newValue):
        traversalNode = head
        while traversalNode is not None:
            if traversalNode.value == previousValue:
                newNode = self.push(newValue)
                newNode.next = traversalNode.next
                traversalNode.next = newNode
            traversalNode = traversalNode.next

if __name__ == "__main__":

    #how many nodes
    num_objects = 10

    #create a linked list head and tail will be the same because you start with 1 node
    list1 = LinkedList()
    #create the head first with a value, allocate this in memory
    head = list1.push(0)
    tail = head

    counter = 0

    #create your connected nodes, move the tail as your list grows
    while counter < num_objects:
        counter += 1
        new_node = list1.push(counter)
        tail.next = new_node
        tail = new_node

    #original created list
    list1.printList(head)

    #lets insert a node with the value 12, after a given value for the previous node
    list1.insertAt(head, 5, 12)

    print("--------------------")
    #check the list again
    list1.printList(head)
