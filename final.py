class ListNode:
    #单链表的节点
    def __init__(self, data):
        self.data = data
        self.next = None

class BinaryTreeNode:
    #创建二叉树
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    


class Convert_List2Tree:
    #用于将链表转化为二叉树的class
    #创建储存表头的构造函数
    def __init__(self, data = None):
        self.head = None
        self.root = None
    def push(self, new_data):

        # Creating a new linked list node and storing data
        # Move the head to point to new node
        # Make next of new node as head
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def convert2Binary(self):

        # Queue to store the parent nodes
        queue = []
        # 前提
        if self.head is None:
            self.root = None
            return
        # The first node is always the root node,
        # And add it to the queue
        self.root = BinaryTreeNode(self.head.data)
        #把没有head的root添加到queue的开头
        queue.append(self.root)
        # Advance the pointer to the next node
        self.head = self.head.next
        # Until the end of linked list is reached, do:
        while(self.head):
            # Take the parent node from the queue and
            # and remove it from queue
            parent = queue.pop(0) # Front of queue
            # Take next two nodes from the linked list.
            # We will add them as children of the current
            # parent node in step 2.b.
            # Push them into the queue so that they will be
            # parent to the future node
            leftChild= None
            rightChild = None
            leftChild = BinaryTreeNode(self.head.data)
            queue.append(leftChild)
            self.head = self.head.next
            if(self.head):
                rightChild = BinaryTreeNode(self.head.data)
                queue.append(rightChild)
                self.head = self.head.next

            # Assign the left and right children of parent
            parent.left = leftChild
            parent.right = rightChild
#给出一个i，to find the node of index
    def find(self, i):
        node_f = self.root
        for k in range(i):
            node_f = node_f.next
            return node_f
#给三个赋值
    def parent(i) :

        return (i - 1) // 2

    def leftChild(i) :

        return ((2 * i) + 1)

    def rightChild(i) :

        return ((2 * i) + 2)

    def exchange(self, j,k):
        node_1 = self.find(j)
        node_2 = self.find(k)
#第二问 
#creat a class
class priorityqueue:
    def __init__(self):
        self.heap = BinaryTreeNode()
        self.size = 0

#remove up function to fit the heap property
    def remove(self, i):
        parent_index = self.heap.parent(i)
        if parent_index < 0:
            return
        parent_node = self.heap.find(parent_index)
        if parent_node.data > self.heap.find(i).data:
            self.heap.exchange(parent_index,i)
            self.remove(parent_index)
    #exchange and remove the parent
    def shift_down(self, i):
#remove down function to fit the heap property
        left_child_idx = self.heap.leftChild(i)
        right_child_idx = self.heap.rightChild(i)
        if left_child_idx >= self.size:
            return
        if right_child_idx >= self.size:
            min_idx = left_child_idx
        else:
            left_child = self.heap.find(left_child_idx)
            right_child = self.heap.find(right_child_idx)
        # exchange the left and right with mini
        if left_child.data < right_child.data:
            min_idx = left_child_idx
        else:
            min_idx = right_child_idx
        if self.heap.find(i).data > self.heap.find(min_idx).data:
            self.heap.exchange(i, min_idx)
            self.shift_down(min_idx)
  #Time Complexity O(log n) , 
  #Function to insert a  new element into the priority queue  
  #Insert a new element at the end of the tree.
  #If there is no node, a new node is created. 
  # Otherwise (a node already exists) insert a new node at the end (the last node from left to right.
    def insert(self,key):
        node = ListNode(key)
        parent_index = self.heap.parent(self.size)
        parent_node = self.heap.find(parent_index)
        if (parent_node.next):
            parent_node.next.next = node
        else:
            parent_node.next = node
            self.size += 1

            self.remove(self.size)
#Time Complexity: O(log n) the same
#Remove the smallest element in the priority queue
#Select the element you want to delete, swap it with the last element, and delete the last element
    def del_min(self):
        mini = self.heap.root.data
        thelastnode = self.heap.find(self.size - 1)
        self.heap.root.data = thelastnode.data
        if (thelastnode.next):
            thelastnode.next = None
        self.size -= 1
        self.shift_down(0)
        return mini
#第三问在def上

   

   
    
