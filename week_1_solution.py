import hou

class HouList:
    def __init__(self):
        self.nodes = hou.selectedNodes()
        self.head = self.nodes[0]

    def network_traversal(self):
        head = self.head
        try:
            while len(head.outputs()) >= 0:
                print(head.name())
                head = head.outputs()[0]
        except:
            pass

    def get_tail_node(self):
        last_node = self.head
        while len(last_node.outputs()) > 0:
            last_node = last_node.outputs()[0]
        print(last_node.name())

    def insert_at(self, node_name):
        traversal_node = self.head
        previous = None
        next_node = None

        while len(traversal_node.outputs()) > 0:
            if traversal_node.name() == node_name:
                print("Node found!")
                previous = traversal_node
                next_node = previous.outputs()[0]
                new_node = previous.createOutputNode("null")
                next_node.setInput(0, new_node)
                traversal_node = new_node
            traversal_node = traversal_node.outputs()[0]


net1 = HouList()
print("All the nodes in the chain: ")
net1.network_traversal()
print("-----------------")
print("The last node in the chain is: ")
net1.get_tail_node()
#the node network I have has some specific nodes in Houdini
#It happens to have some random nodes, lets find one with the name: color1
#we are trying to insert a "null" node after a node with that name
#we don't know if that node exists in our network chain
print("Inserted node after color1")
net1.insert_at("color1")
