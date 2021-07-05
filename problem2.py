'''
T(n)= O(n)
S(n)=O(n)
leetcode = yes
preorder traversal contains the root at the begining and inorder contains root at the midle b/w its left and right child  take each element in preorder and finds it index in inorder 
by this we will know the the no of elements that should be present in curent root left and its roght recursively build left and right subtree by passing corresponding inorder and perorder arrays ''' 

def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        
        root=TreeNode(preorder[0])
        print(root)
        mid = inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
            
