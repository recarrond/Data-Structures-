class HashTable:
    def __init__(self, capacity: int = 8):
        """
        初始化哈希表
        :param capacity: 初始桶数量（默认8）
        """
        self.capacity = capacity  # 桶总数
        self.table = [[] for _ in range(capacity)]  # 桶：每个桶是链表

    def _hash_index(self, key: str) -> int:
        """
        1. 使用 Python 内置 hash() 函数
        2. 对容量取模，得到桶下标
        """
        return hash(key) % self.capacity

    def put(self, key: str, value: int) -> None:
        """添加 / 修改键值对"""
        index = self._hash_index(key)
        bucket = self.table[index]

        # 如果键已存在，更新值
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # 不存在则追加
        bucket.append((key, value))

    def get(self, key: str) -> int | None:
        """根据 key 获取值，不存在返回 None"""
        index = self._hash_index(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key: str) -> None:
        """删除键值对"""
        index = self._hash_index(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

    def __str__(self):
        """打印所有键值对"""
        items = {}
        for bucket in self.table:
            for k, v in bucket:
                items[k] = v
        return str(items)

if __name__ == '__main__':
    ht = HashTable(10)

    ht.put("apple", 10)
    ht.put("banana", 20)
    ht.put("cat", 30)
    ht.put("apple", 999)  # 覆盖

    print(ht)  # {'apple': 999, 'banana': 20, 'cat': 30}
    print(ht.get("banana"))  # 20

    ht.delete("cat")
    print(ht)  # {'apple': 999, 'banana': 20}