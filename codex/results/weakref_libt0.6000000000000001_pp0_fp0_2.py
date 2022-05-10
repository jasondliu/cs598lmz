import weakref

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root == None:
            return []
        queue = [root]
        lists = []
        while len(queue) > 0:
            length = len(queue)
            list = []
            for i in range(length):
                node = queue.pop(0)
                list.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            lists.append(list)
        return lists
