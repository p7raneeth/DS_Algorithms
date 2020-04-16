class node:
    def __init__(self, value=None):
        self.value = value
        self.nextnode = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.nextnode != None:
            cur = cur.nextnode
        cur.nextnode = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.nextnode != None:
            total+=1
            cur = cur.nextnode
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.nextnode!=None:
            cur_node=cur_node.nextnode
            elems.append(cur_node.value)
        print('elems',elems)

    def get(self, idx):
        if idx > self.length():
            print('index out of range error')
            return None
        cur_index = 0
        cur = self.head
        while True:
            cur_node=cur.nextnode
            print(cur_node.value)
            if idx == cur_index: return cur_node.value
            cur_index += 1

my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()
print(my_list.get(3))