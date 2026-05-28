#定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 节点值
        self.left = left  # 左孩子指针（引用）
        self.right = right  # 右孩子指针（引用）

#数组转链表结构二叉树
def array_to_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])  # 根节点
    queue = [root]  # 队列：用来按层构建节点
    index = 1  # 从数组第2个元素开始

    while queue and index < len(arr):
        current_node = queue.pop(0)  # 取出队首节点

        # 左孩子
        if index < len(arr) and arr[index] is not None:
            current_node.left = TreeNode(arr[index])
            queue.append(current_node.left)
        index += 1

        # 右孩子
        if index < len(arr) and arr[index] is not None:
            current_node.right = TreeNode(arr[index])
            queue.append(current_node.right)
        index += 1

    return root


#按层打印二叉树
def print_tree(root):
    if not root:
        return
    queue = [root]
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(current_level)


#测试
if __name__ == "__main__":
    arr = [10, 5, 15, 3, 7, None, 20]
    root = array_to_tree(arr)
    print("二叉树 层序遍历结果：")
    print_tree(root)

    print("\n手动验证节点结构：")
    print("根节点：", root.val)
    print("根左孩子：", root.left.val)
    print("根右孩子：", root.right.val)
    print("节点5的左孩子：", root.left.left.val)
    print("节点15的左孩子：", root.right.left)  # None
    print("节点15的右孩子：", root.right.right.val)