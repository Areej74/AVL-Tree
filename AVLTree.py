#18B-097-CS
#18B-066-CS
#18B-126-CS
"""AVL TREE"""



class Node:
    
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
        self.height=1
        
class AVL:
    
    def __init__(self):
        self.root=None
        
#Inserting values in AVL Tree
        
    def Insert(self,value):   
        self.root = self.__Insert(value,self.root)
        
    def __Insert(self,value,node):
        if node==None:
            node=Node(value)
        elif value < node.value:
            node.left= self.__Insert(value,node.left)
        else:
            node.right= self.__Insert(value,node.right)
        node.height=1+max(self.__height(node.left),self.__height(node.right))
        balance=self.__Balance(node)
        if balance>1 and value<node.left.value:
            return self.RRotate(node)
        if balance<-1 and value>node.right.value:
            return self.LRotate(node)
        if balance>1 and value>node.left.value:
            node.left=self.LRotate(node.left)
            return self.RRotate(node)
        if balance<-1 and value<node.right.value:
            node.right=self.RRotate(node.right)
            return self.LRotate(node)
            
        return node

#Performing Rotations on AVL Tree
    
    def LRotate(self,node):
        y=node.right
        T=y.left
        y.left=node
        node.right=T
        node.height=1+max(self.__height(node.left),self.__height(node.right))
        y.height=1+max(self.__height(y.left),self.__height(y.right))
        return y
    
    def RRotate(self,node):
        y=node.left
        T=y.right
        y.right=node
        node.left=T
        node.height=1+max(self.__height(node.left),self.__height(node.right))
        y.height=1+max(self.__height(y.left),self.__height(y.right))
        return y

#Height of an AVL Tree
    
    def height(self):
        x=self.__height(self.root)
        return x
    
    def __height(self,root):
        if root==None:
            return -1
        else:
            l=self.__height(root.left)
            r=self.__height(root.right)
        return 1+max(l,r)

#checking for Minimum value in an AVL Tree
    
    def FindMin(self):
        x=self.__FindMin(root)
        return x
    
    def __FindMin(self,root):
        if root==None:
            return None
        if root.left==None:
            return root
        return self.__FindMin(root.left)
    
#Balancing an AVL Tree

    def Balance(self):
        x=self.__Balance(root)
        return x
    
    def __Balance(self,root):
        if root==None:
            return None
        return self.__height(root.left)-self.__height(root.right)
    
    def PreOrder(self):
        return self.__PreOrder(self.root)
    
    def __PreOrder(self, root): 
        if not root: 
            return
        print(root.value) 
        self.__PreOrder(root.left) 
        self.__PreOrder(root.right)
    def Successor(self):
        x=self.__Successor(self.root)
        return x.data
    def __Successor(self,node):
        if node and node.right:
            return self.__FindMin(node.right)
        return None

#Deletion of a selected Node value in AVL

    def Delete(self,value):
        self.root=self.__Delete(value,self.root)    

    def __Delete(self,value,root):
        if not root:
            return root
        elif value<root.value:
            root.left=self.__Delete(value,root.left)
        elif value>root.value:
            root.right=self.__Delete(value,root.right)
        else:
            if root.left==None:
                x=root.right
                root=None
                return x
            elif root.right==None:
                x=root.left
                root=None
                return x
            y=self.__FindMin(root.right)
            root.value=y.value
            root.right=self.__Delete(y.value,root.right)
        if root==None:
            return root
        root.height=1+max(self.__height(root.left),self.__height(root.right))
        balance=self.__Balance(root)
        if balance>1 and self.__Balance(root.left)>=0:
            return self.RRotate(root)
        if balance<-1 and self.__Balance(root.right)<=0:
            return self.LRotate(root)
        if balance > 1 and self.__Balance(root.left) < 0: 
            root.left = self.LRotate(root.left) 
            return self.rightRotate(root)  
        if balance < -1 and self.__Balance(root.right) > 0: 
            root.right = self.RRotate(root.right) 
            return self.LRotate(root) 
        return root

#to search a node with its value in an AVL Tree

    def Search(self,value):
        x= self.__Search(self.root,value)
        return x
    def __Search(self,root,value):
        if root==None:
            return False
        if root.value==value:
            return True
        if root.value<value:
            return self.__Search(root.right,value)
        elif root.value >value:
            return self.__Search(root.left,value)
        else:
            return False

    
