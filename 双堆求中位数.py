import heapq

class MedianFinder:
    def __init__(self):
        self.left = []  # 大顶堆
        self.right = []  # 小顶堆

    def addNum(self, num: int) -> None:
        #选择插入堆
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        #平衡两堆大小，差值不能超过1
        #左堆过多，移最大值到右堆
        if len(self.left) - len(self.right) > 1:
            max_left = -heapq.heappop(self.left)
            heapq.heappush(self.right, max_left)
        #右堆过多，移最小值到左堆
        elif len(self.right) - len(self.left) > 0:
            min_right = heapq.heappop(self.right)
            heapq.heappush(self.left, -min_right)

    def findMedian(self) -> float:
        total = len(self.left) + len(self.right)
        #奇数个元素，左堆多一个，中位数是左堆顶
        if total % 2 == 1:
            return -self.left[0]
        #偶数个，取两堆顶平均值
        else:
            return (-self.left[0] + self.right[0]) / 2

if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(3)
    print(mf.findMedian())  #3
    mf.addNum(1)
    print(mf.findMedian())  #2
    mf.addNum(4)
    print(mf.findMedian())  #3
    mf.addNum(1)
    print(mf.findMedian())  #2
    mf.addNum(5)
    print(mf.findMedian())  #3