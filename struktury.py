# coding: utf-8
'''_Node, Stack, LinkedQueue(linked node),CycleQueue,MaxPQ,MinPQ,BinarySearchTree,BinarySearchTreeNoNode,RBT (red-black-tree), HuffmanTree'''

class _Node:
    '''A (hopefully) universal node. Key, data(None)'''
    def __init__(self, data = None, key = None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'red'
        
    def __repr__(self):
        return repr(self.key)
        
    def __lt__(self, other):
        return self.key < other
    
    def __le__(self, other):
        return self.key <= other
    
    def __eq__(self, other):
        return self.key == other
    
    def __ne__(self, other):
        return self.key != other
    
    def __gt__(self, other):
        return self.key > other
    
    def __ge__(self, other):
        return self.key >= other


# In[117]:

class Stack():
    '''Linked structure. push(key,data), pop, top, isEmpty.'''
    def __init__(self):
        self.peak = None
        
    def push(self,key,data=None):
        new = _Node(key,data)
        if self.peak is not None:
            new.parent = self.peak
        self.peak = new
    
    def pop(self):
        rtrn = self.peak
        if rtrn is None:
            raise Exception('Stack is empty.')
        self.peak = self.peak.parent
        return rtrn
            
    def top(self):
        return self.peak
    
    def isEmpty(self):
        return self.peak is None

class LinkedQueue:
    '''enqueue(data, key), dequeue, isEmpty, first, length'''
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __len__(self):
        return self.length
        
    def enqueue(self, data, key=None):
        
        node = _Node(data, key)
        
        if self.head is None:
            self.head = node
        else:
            self.tail.parent = node
        self.tail = node
        self.length += 1
        
    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        rtrn = self.head
        self.head = self.head.parent
        self.length -= 1
        return rtrn
    
    def first(self):
        return self.head
    
    def isEmpty(self):
        return self.head == None

class DoubleLinkedList:
    '''Double linked list. insert(key,data)[sorts], peekLeft, peekRight, removeLeft, removeRight, remove(key)'''
    def __init__(self):
        self.left = None
        self.right = None
        self.length = 0
        
    def __iter__(self):
        left = self.left
        while left is not None:
            yield left
            left = left.right
        
    def _insertRight(self, key, data = None):
        self.length += 1
        if self.right is None:
            self.right = self.left = _Node(key,data)
        else:
            new = _Node(key,data)
            new.left = self.right
            self.right.right = new
            self.right = self.right.right

    def _insertLeft(self, key, data = None):
        self.length += 1
        if self.left is None:
            self.left = self.right = _Node(key,data)
        else:
            new = _Node(key,data)
            new.right = self.left
            self.left.left = new
            self.left = self.left.left
            
    def removeRight(self):
        if self.right is None:
            raise Exception('Error, no right side.')
        self.right = self.right.left
        if self.right is None:
            return
        self.right.right = None
        
    def removeLeft(self):
        if self.left is None:
            raise Exception('Error, no left side.')
        self.left = self.left.right
        if self.left is None:
            return
        self.left.left = None
        
    def insert(self,key,data=None):
        if self.right is None:
            self.left = self.right = _Node(key,data)
            self.left.right = self.right
            self.right.left = self.left
            self.length += 1
            return
        if key>self.right.key:
            self._insertRight(key,data)
            return
        elif key<self.left.key:
            self._insertLeft(key,data)
            return
        left = self.left #najmniejsza wartość
        leftright = self.left.right #kolejna po najmniejszej
        while leftright is not None and leftright.key < key:
            left = left.right
            leftright = leftright.right
        new = _Node(key,data)
        new.right = leftright
        new.left = left
        leftright.left = new
        left.right = new
        self.length += 1
        
    def peekRight(self):
        return self.right
    
    def peekLeft(self):
        return self.left
    
    def removeKey(self,key):
        if key == self.right:
            self.removeRight()
        elif key == self.left:
            self.removeLeft()
        else:
            left = self.left #najmniejsza wartość
            leftright = self.left.right #kolejna po najmniejszej
            while leftright is not None and leftright != key:
                left = left.right
                leftright = leftright.right
            if leftright is None:
                raise Exception('Error, no key')
            left.right = left.right.right
            leftright.right.left.left = left
    
    def __max__(self):
        m = self.left
        left = self.left.left
        while left.right is not None:
            if left > m:
                m = left
        return m
    
    def __min__(self):
        m = self.left
        left = self.left.left
        while left.right is not None:
            if left < m:
                m = left
        return m

class CycleQueue:
    '''CycleQueue. Initialisation requires a max number of items to be expected. isEmpty, enqueue(key,data), dequeue, first'''
    def __init__(self, n):  # zlozonosc O(n)
        """inicjalizacja"""
        self.items = n * [None]
        self.size = n
        self.head = 0
        self.tail = 0

    def isEmpty(self):  # zlozonosc O(1)
        """sprawdzenie czy kolejka FIFO jest pusta"""
        return self.head == self.tail

    def enqueue(self, item):  # zlozonosc O(1)
        """wstawienie elementu do kolejki FIFO"""
        if self.tail+1 == self.head or (self.head == 0 and self.tail == self.size-1): #sprawdzanie, czy kolejka nie jest pełna
            raise Exception('Queue is full.')
        self.items[self.tail] = item
        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):  # zlozonosc O(1)
        """usuniecie elementu z kolejki FIFO"""
        rtrn = self.items[self.head]
        if self.head == self.tail: #sprawdzanie, czy nie jest pusta:
            raise Exception('Queue is empty.')
        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1
        return rtrn

    def first(self):  # zlozonosc O(1)
        """zwrocenie pierwszegom elementu z kolejki FIFO"""
        if self.head == self.tail: #spr czy nie jest pusta:
            raise Exception('Queue is empty.')
        return self.items[self.head]

class PQ:
    def __init__(self,mode='max'):
        self.heap = []
        self.mode = mode
        
    def insert(self, data):
        self.heap.append(data)
        self._toTop(len(self.heap)-1)
        
    def __len__(self):
        return len(self.heap)
        
    def extract(self):
        if self.isEmpty():
            raise Exception('Empty heap')
        if len(self.heap) == 1:
            return self.heap.pop()
        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._toBottom(0)
        return top
        
    def _toTop(self,n): #n to miejsce, które porównujemy z rodzicem
        parent = self._parent(n)
        while n>0 and self._cmpr(n,parent):
            self.heap[parent],self.heap[n] = self.heap[n],self.heap[parent]
            n = parent
            parent = self._parent(parent)
            
    def _toBottom(self,n):
        left = self._leftchild(n)
        right = self._rightchild(n)
        target = n
        if left <= len(self.heap)-1 and self._cmpr(left,n):
            target = left
        if right <= len(self.heap)-1 and self._cmpr(right,target):
            target = right
        if target != n:
            self.heap[n],self.heap[target] = self.heap[target],self.heap[n]
            self._toBottom(target)
        
    def isEmpty(self):
        return self.heap == []
            
    def _parent(self,x):
        if x%2 == 0:
            return x//2-1
        return x//2
    
    def _leftchild(self,x):
        return x*2+1
    
    def _rightchild(self,x):
        return x*2+2
    
    def _cmpr(self,a,b):
        if self.mode == 'max':
            return self.heap[a]>self.heap[b]
        elif self.mode == 'min':
            return self.heap[a]<self.heap[b]
   
    def __repr__(self):
        return repr(self.heap)
    
def HeapSort(T):
    '''Sorts an input list using HeapSort method.'''
    _build(T)
    n = len(T)-1
    while n>=0:
        T[0],T[n] = T[n],T[0]
        _toBottom(T,n)
        n -= 1
    return T

def _build(T):
    for x in range(_parent(len(T)-1),-1,-1): #od ostatniego rodzica do początku
        _toBottom(T,x)
    return T

def _toBottom(T,n):
    left = _leftchild(n)
    right = _rightchild(n)
    smallest = n
    if left <= len(T)-1 and T[left] < T[smallest]:
        smallest = left
    if right <= len(T)-1 and T[right] < T[n]:
        smallest = right
    if smallest != n:
        T[n],T[smallest] = T[smallest],T[n]
        _toBottom(T,smallest)
        
def _leftchild(x):
    return x*2+1

def _rightchild(x):
    return x*2+2

def _parent(x):
    if x%2 == 0:
        return x//2-1
    return x//2


# In[290]:

class BinarySearchTree:
    '''Binary Search Tree made with nodes. insert(key,data), insert_iter(key,data),in/pre/postorder,delete(key), search(key), data(key), nodes'''
    def __init__(self):
        self.root = None

    def __repr__(self):
        return repr(self.root)
        
    def insert_iter(self, key, data = None):
        z = _Node(key,data)
        y = None
        x = self.root
        while (x is not None):
            y = x
            if (z < x):
                x = x.left
            else:
                x = x.right
        if (y is None):
            self.root = z
        elif (z < y):
            y.left = z
        else:
            y.right = z

    def _preorder(self,root):
        if root is not None:
            print (root)
            self._preorder(root.left)
            self._preorder(root.right)

    def preorder(self):
        self._preorder(self.root)

    def _inorder(self,root):
        if root is not None:
            self._inorder(root.left)
            print (root)
            self._inorder(root.right)

    def inorder(self):
        self._inorder(self.root)

    def _postorder(self,root):
        if root is not None:
            self._postorder(root.left)
            self._postorder(root.right)
            print (root)

    def postorder(self):
        self._postorder(self.root)
        
        
    def _insert(self,node,tree):
        if tree > node:
            if tree.left is not None:
                self._insert(node,tree.left)
            else:
                node.parent = tree
                tree.left = node
                return
        if tree <= node:
            if tree.right is not None:
                self._insert(node,tree.right)
            else:
                node.parent = tree
                tree.right = node
                return
            
    def insert(self,key,data=None):
        node = _Node(key,data)
        if self.root is None:
            self.root = node
            return
        self._insert(node,self.root)
    
    def _min(self,node): #wskazuje komórkę z najmniejszą wartością w podanym drzewie (by podało wartość, należy wpisać self._min.key)
        while node.left is not None:
            node = node.left
        return node
    
    def delete(self,key):
        self._delete(self.root,key)
        
    def _delete(self,root,key):
        if key < root.key:
            root.left = self._delete(root.left,key)
            return root
        elif key > root.key:
            root.right = self._delete(root.right,key)
            return root
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is not None and root.right is None:
                root.left.parent = root.parent
                return root.left
            elif root.right is not None and root.left is None:
                root.right.parent = root.parent
                return root.right
            else:
                successor = self._min(root.right)
                root.key = successor.key
                root.right = self._delete(root.right,successor.key)
                return root
            
    def _search(self,key): #zwraca node o podanej wartości
        x = self.root
        while x is not None:
            if key > x:
                x = x.right
            elif key < x:
                x = x.left
            else:
                return x
        return x
    
    def search(self,key):
        return self._search(key) is not None
        
    def nodes(self):
        return self._nodes(self.root)            

    def _nodes(self, drzewo):
        count = 0
        if self.root is not None:
            count += 1
        if drzewo.left is not None:
            count += self._nodes(drzewo.left)
        if drzewo.right is not None:
            count += self._nodes(drzewo.right)
        return count
    
    def data(self,key):
        return self._search(key).data


# In[99]:

class BinarySearchTreeNoNode:
    '''Binary Search Tree without additional Node class. insert_iter, insert, inorder, delete.'''
    def __init__(self,key=None,parent=None,data=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
        self.data = data

    def insert_iter(self, key, data=None):
        if self.key is None:
            self.key = klucz
        else:
            z = BinarySearchTreeNoNode(key,data)
            y = None
            x = self
            while (x is not None):
                y = x
                if (z.key < x.key):
                    x = x.left
                else:
                    x = x.right
            if (z.key < y.key):
                y.left = z
            else:
                y.right = z

    def inorder(self):
        if self.key is not None:
            if self.left is not None:
                self.left.inorder()
            print (self.key)
            if self.right is not None:
                self.right.inorder()
                
    def insert(self,key,data):
        if self.key is None:
            self.key = key
            return
        if self.key > key:
            if self.left is not None:
                self.left.insert(key,data)
            else:
                self.left = BinarySearchTreeNoNode(key,self,data)
        if self.key <= key:
            if self.right is not None:
                self.right.insert(key,self,data)
            else:
                self.right = BinarySearchTreeNoNode(key,data)

    def _min(self):
        if self.left is not None:
            return self.left._min()
        return self
    
    def delete(self,key):
        self = self._delete(key)
    
    
    def _delete(self,key):
        if key < self.key:
            self.left = self.left._delete(key)
            return self
        if key > self.key:
            self.right = self.right._delete(key)
            return self
        else:
            if self.left is None and self.right is None:
                self.key = None
                return self
            elif self.right is None and self.left is not None:
                self.left.parent = self.parent
                return self.left
            elif self.left is None and self.right is not None:
                self.right.parent = self.parent
                return self.right
            else:
                successor = self.right._min()
                self.key = successor.key
                self.right = self.right._delete(successor.key)
                return self

class RBT:
    '''Red-black tree. isEmpty, insert(key,data), delete(key), inorder, nodes, leaves, mini, maxi, data(key)'''
    def __init__(self):
        self.nill = _Node(None)
        self.nill.color = 'black'
        self.root = self.nill
        
    def isEmpty(self):
        return self.root is self.nill
    
    def insert(self,key,data=None):
        new = _Node(key = key, data = data)
        new.left = self.nill
        new.right = self.nill
        if self.root is self.nill:
            self.root = new
            self.root.parent = self.nill
            self.root.color = 'black'
        else:
            self._insert(new,self.root)
    
    def _insert(self,node,tree):
        if node >= tree:
            if tree.right is not self.nill:
                self._insert(node,tree.right)
            else:
                node.parent = tree
                tree.right = node
                self.fixup(tree.right)
                return
        elif node < tree:
            if tree.left is not self.nill:
                self._insert(node,tree.left)
            else:
                node.parent = tree
                tree.left = node
                self.fixup(tree.left)
                return
            
    def rotate_left(self,tree):
        #print(tree.data)
        y = tree.right
        tree.right = y.left
        if y.left != self.nill:
            y.left.parent = tree
        y.parent = tree.parent
        if tree.parent == self.nill:
            self.root = y
        elif tree == tree.parent.left:
            tree.parent.left = y
        else:
            tree.parent.right = y
        y.left = tree
        tree.parent = y
        
    def rotate_right(self,tree):
        #print(tree.data)
        y = tree.left
        tree.left = y.right
        if y.right != self.nill:
            y.right.parent = tree
        y.parent = tree.parent
        if tree.parent == self.nill:
            self.root = y
        elif tree == tree.parent.right:
            tree.parent.right = y
        else:
            tree.parent.left = y
        y.right = tree
        tree.parent = y
                
    def fixup(self,tree):
        while tree.parent.color == 'red':
            if tree.parent == tree.parent.parent.left:
                uncle = tree.parent.parent.right #ustalenie wujka
                if uncle.color == 'red': #jeśli wujek jest czerwony, wystarczy przekolorować
                    tree.parent.color = 'black'
                    uncle.color = 'black'
                    tree.parent.parent.color ='red'
                    tree = tree.parent.parent #powtarzamy pętlę while dla dziadka
                elif tree == tree.parent.right: #jeśli rozpatrujemy prawe dziecko, obracamy w lewo.
                    tree = tree.parent
                    self.rotate_left(tree)
                else:
                    tree.parent.color = 'black'
                    tree.parent.parent.color = 'red'
                    self.rotate_right(tree.parent.parent)
            else:
                uncle = tree.parent.parent.left
                if uncle.color == 'red':
                    tree.parent.color = 'black'
                    uncle.color = 'black'
                    tree.parent.parent.color ='red'
                    tree = tree.parent.parent
                elif tree == tree.parent.left:
                    tree = tree.parent
                    self.rotate_right(tree)
                else:
                    tree.parent.color = 'black'
                    tree.parent.parent.color = 'red'
                    self.rotate_left(tree.parent.parent)
        self.root.color = 'black'
        
    def transplant(self,u,v):
        if u.parent == self.nill:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:#if u == u.parent.right
            u.parent.right = v
        v.parent = u.parent
        
    def _search(self,key): #zwraca node o podanej wartości
        x = self.root
        while x is not self.nill:
            if key > x:
                x = x.right
            elif key < x:
                x = x.left
            else:
                return x
        return x
    
    def search(self,key):
        return self._search(key) is not self.nill
        
    def _min(self,node): #minimum z danego drzewa
        while node.left is not self.nill:
            node = node.left
        return node
    
    def _max(self,node):
        while node.right is not self.nill:
            node = node.right
        return node

    def delete(self,key):
        z = self._search(key)
        if z is self.nill:
            raise Exception('No such node found.')
        y = z
        oricol = y.color
        if z.left == self.nill:
            x = z.right
            self.transplant(z,z.right)
        elif z.right == self.nill:
            x = z.left
            self.transplant(z,z.left)
        else:
            y = self._min(z.right)
            oricol = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y,y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z,y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if oricol == 'black':
            self.del_fixup(x)
            
    def del_fixup(self,x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color =='black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color ='red'
                        self.rotate_right(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_right(x.parent)
                    w = x.parent.left
                if w.right.color =='black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.right.color = 'black'
                        w.color ='red'
                        self.rotate_left(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = 'black'
        
    def inorder(self):
        return self._inorder(self.root)
    
    def _inorder(self,root):
        if root is not self.nill:
            if root.left is not self.nill:
                self._inorder(root.left)
            print (root)
            if root.right is not self.nill:
                self._inorder(root.right)
                
    def preorder(self):
        return self._preorder(self.root)
    
    def _preorder(self,root):
        if root is not self.nill:
            print (root)
            if root.left is not self.nill:
                self._preorder(root.left)
            if root.right is not self.nill:
                self._preorder(root.right)
                
    def postorder(self):
        return self._postorder(self.root)
    
    def _postorder(self,root):
        if root is not self.nill:
            if root.left is not self.nill:
                self._postorder(root.left)
            if root.right is not self.nill:
                self._postorder(root.right)
            print (root)
            
    def leaves(self):
        self._leaves(self.root)
    
    def _leaves(self,root):
        if root.right is not self.nill:
            self._leaves(root.right)
        if root.left is not self.nill:
            self._leaves(root.left)
        if root.left is self.nill and root.right is self.nill:
            return root
            
    def mini(self):
        return self._min(self.root)
    
    def maxi(self):
        return self._max(self.root)
    
    def nodes(self):
        return self._nodes(self.root)            

    def _nodes(self, root):
        count = 0
        if root is not self.nill:
            if root.left is not self.nill:
                count += self._nodes(root.left)
            if root.right is not self.nill:
                count += self._nodes(root.right)
        count += 1
        return count
    
    def data(self,key):
        return self._search(key).data
    
    def inorder_gen(self):
        return self._inorder_gen(self.root)
    
    def _inorder_gen(self,node):
        if node is not self.nill:
            if node.left is not self.nill:
                yield from self._inorder_gen(node.left)
            yield node
            if node.right is not self.nill:
                yield from self._inorder_gen(node.right)

class HuffmanTree:
    def __init__(self,key,data=None,path = ''):
        self.root = None
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.path = path
    
    def __add__(self,other):
        new = HuffmanTree(self.key + other.key)
        new.left = self
        new.left.path += '0'
        new.right = other
        new.right.path += '1'
        return new
    
    def inorder(self):
        if self.key is not None:
            if self.left is not None:
                self.left.inorder()
            print (self.data,self.key)
            if self.right is not None:
                self.right.inorder()
                
    def paths(self,path=''):
        if self.key is not None:
            if self.left is not None:
                lpath = path + '0'
                self.left.paths(lpath)
            if self.right is not None:
                rpath = path + '1'
                self.right.paths(rpath)
            if self.right is None and self.left is None:
                print ('{}: ID:{}, Vol:{}, Code:{}'.format(chr(self.data),self.data,self.key,path))
    
    def __lt__(self, other):
        return self.key < other
    
    def __le__(self, other):
        return self.key <= other
    
    def __eq__(self, other):
        return self.key == other
    
    def __ne__(self, other):
        return self.key != other
    
    def __gt__(self, other):
        return self.key > other
    
    def __ge__(self, other):
        return self.key >= other