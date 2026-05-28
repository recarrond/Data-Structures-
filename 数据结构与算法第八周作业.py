class Node:
    def __init__(self, data: str | int | float):
        self.data = data
        self.next_node: Node | None = None

    def __repr__(self) -> str:
        return f"Node({self.data!r})"


class LinkedList:
    def __init__(self):
        self.first_node: Node | None = None

    def __repr__(self) -> str:
        if not self.first_node:
            return "LinkedList([])"

        nodes = []
        current = self.first_node
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return f"LinkedList([{', '.join(nodes)}])"

    def read(self, index: int):
        current_node = self.first_node
        current_index = 0
        while current_index < index:
            if not current_node:
                return None
            current_node = current_node.next_node
            current_index += 1
        return current_node.data if current_node else None

    def index_of(self, value):
        current_node = self.first_node
        current_index = 0
        while current_node:
            if current_node.data == value:
                return current_index
            current_node = current_node.next_node
            current_index += 1
        return None

    def insert_at_index(self, index: int, value):
        new_node = Node(value)
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return True

        current_node = self.first_node
        current_index = 0
        while current_index < index - 1:
            if not current_node:
                return False
            current_node = current_node.next_node
            current_index += 1

        if not current_node:
            return False

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        return True

    #1. 链表反转
    def reverse(self):
        """
        反转单向链表
        """
        prev = None       # 前一个结点
        current = self.first_node  # 当前结点

        while current:
            next_node = current.next_node  # 先保存下一个结点
            current.next_node = prev       # 反转指针
            prev = current                 # prev 前进
            current = next_node            # current 前进

        self.first_node = prev  # 最后头结点指向原尾结点

    #2. 环检测
    def has_cycle(self) -> bool:
        """
        判断链表是否存在环
        使用快慢指针
        """
        if not self.first_node:
            return False

        slow = self.first_node   # 慢指针，每次走1步
        fast = self.first_node   # 快指针，每次走2步

        while fast and fast.next_node:
            slow = slow.next_node
            fast = fast.next_node.next_node

            if slow == fast:    # 相遇 → 有环
                return True

        return False            # 快指针走到末尾 → 无环


#测试
if __name__ == '__main__':
    print("===== 链表反转测试 =====")
    ll = LinkedList()
    ll.insert_at_index(0, "a")
    ll.insert_at_index(1, "b")
    ll.insert_at_index(2, "c")
    print("反转前:", ll)

    ll.reverse()
    print("反转后:", ll)  # 输出 LinkedList([c, b, a])
    print("\n")

    print("===== 环检测测试 =====")
    # 测试 2.1：无环链表
    ll1 = LinkedList()
    ll1.insert_at_index(0, 1)
    ll1.insert_at_index(1, 2)
    ll1.insert_at_index(2, 3)
    print("链表是否有环？", ll1.has_cycle())  # False

    # 测试 2.2：构造有环链表
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node1.next_node = node2
    node2.next_node = node3
    node3.next_node = node1  # 环：30 → 10

    ll2 = LinkedList()
    ll2.first_node = node1
    print("环链表是否有环？", ll2.has_cycle())  # True

