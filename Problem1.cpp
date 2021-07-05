//T(n)= O(n)
//S(n)=O(h)
//did run on leetcode Leetcode = yes 
//inorder traversal should give elements in ascending order if  valid BST  recursively traverse  the treee and check if the cur node value is less than the previous value 

class Solution {
public:
    bool result=true;
    TreeNode * prev=nullptr;
    void  helper(TreeNode* root)
    {
        if(root==nullptr)
        {
            return;
        }
        
        helper(root->left);
        if(prev!=nullptr && (prev->val)>=(root->val))
        {
            result=false;
            return;
        }
        prev=root;
        helper(root->right);
    }
        
    bool isValidBST(TreeNode* root) {
         
         helper(root);
         return result;
    }
    
};
