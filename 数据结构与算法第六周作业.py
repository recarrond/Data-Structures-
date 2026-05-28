#优化快速排序
from collections.abc import Sequence
import random

class QuickSortRandomPivot:
    """
    随机轴快速排序类
    """

    def __init__(self, arr: Sequence[int | float]):
        """
        初始化随机轴快速排序器
        :param arr: 待排序序列，支持整数、浮点数
        """
        self.arr: list[int | float] = list(arr)
        self.length: int = len(arr)

    def partition(self, left_index: int, right_index: int) -> int:
        """
        分区操作：随机选取基准元素，将数组划分为小于、大于基准两部分
        :param left_index: 分区范围左边界索引
        :param right_index: 分区范围右边界索引
        :return: 基准元素最终所在索引
        """
        # 随机选取一个位置，与最右侧元素交换，实现随机选轴
        rand_idx = random.randint(left_index, right_index)
        self.arr[rand_idx], self.arr[right_index] = self.arr[right_index], self.arr[rand_idx]

        pivot_index: int = right_index
        pivot: int | float = self.arr[pivot_index]
        right_pointer: int = right_index - 1
        left_pointer: int = left_index
        # 双指针遍历分区
        while True:
            # 左指针右移，找到大于等于基准的元素
            while left_pointer <= right_pointer and self.arr[left_pointer] < pivot:
                left_pointer += 1
            # 右指针左移，找到小于等于基准的元素
            while left_pointer <= right_pointer and self.arr[right_pointer] > pivot:
                right_pointer -= 1
            # 指针相遇/交叉，分区结束
            if left_pointer >= right_pointer:
                break
            # 交换左右指针元素
            self.arr[left_pointer], self.arr[right_pointer] = (
                self.arr[right_pointer],
                self.arr[left_pointer],
            )
        # 将基准元素交换到中间正确位置
        self.arr[left_pointer], self.arr[pivot_index] = (
            self.arr[pivot_index],
            self.arr[left_pointer],
        )
        return left_pointer

    def sort(self, left_index: int | None = None, right_index: int | None = None) -> list[int | float]:
        """
        递归执行快速排序
        :param left_index: 排序范围左边界，默认为数组起始位置
        :param right_index: 排序范围右边界，默认为数组末尾位置
        :return: 排序完成后的数组
        """
        # 初始化左右边界
        if left_index is None:
            left_index = 0
        if right_index is None:
            right_index = self.length - 1
        # 递归终止条件：子数组长度小于等于1，无需排序
        if right_index - left_index <= 0:
            return self.arr
        # 分区并获取基准位置
        pivot_position: int = self.partition(left_index, right_index)
        # 递归排序基准左侧子数组
        self.sort(left_index, pivot_position - 1)
        # 递归排序基准右侧子数组
        self.sort(pivot_position + 1, right_index)
        return self.arr


#三路快速排序
class QuickSort3Way:
    """
    三路快速排序类
    """

    def __init__(self, arr: Sequence[int | float]):
        """
        初始化三路快速排序器
        :param arr: 待排序序列，支持整数、浮点数
        """
        self.arr: list[int | float] = list(arr)
        self.length: int = len(arr)

    def sort(self, left_index: int | None = None, right_index: int | None = None) -> list[int | float]:
        """
        递归执行三路快速排序
        :param left_index: 排序范围左边界，默认为数组起始位置
        :param right_index: 排序范围右边界，默认为数组末尾位置
        :return: 排序完成后的数组
        """
        # 初始化左右边界
        if left_index is None:
            left_index = 0
        if right_index is None:
            right_index = self.length - 1
        # 递归终止条件：子数组长度小于等于1，天然有序
        if right_index <= left_index:
            return self.arr
        # 随机选取基准元素
        rand_idx = random.randint(left_index, right_index)
        self.arr[left_index], self.arr[rand_idx] = self.arr[rand_idx], self.arr[left_index]
        pivot = self.arr[left_index]
        # 分区标记：lt=小于区右边界，gt=大于区左边界，i=当前遍历指针
        lt = left_index
        gt = right_index
        i = left_index + 1
        # 三路分区核心逻辑
        while i <= gt:
            if self.arr[i] < pivot:
                # 当前元素小于基准，划入左侧小于区
                self.arr[i], self.arr[lt] = self.arr[lt], self.arr[i]
                lt += 1
                i += 1
            elif self.arr[i] > pivot:
                # 当前元素大于基准，划入右侧大于区
                self.arr[i], self.arr[gt] = self.arr[gt], self.arr[i]
                gt -= 1
            else:
                # 当前元素等于基准，留在中间区域，直接向后遍历
                i += 1
        # 仅递归排序 小于区 和 大于区，等于区无需处理
        self.sort(left_index, lt - 1)
        self.sort(gt + 1, right_index)
        return self.arr
#测试
if __name__ == "__main__":
    # 测试随机轴快速排序
    arr1 = [3, 6, 8, 10, 1, 2, 1]
    qs_rand = QuickSortRandomPivot(arr1)
    print("随机轴快速排序结果:", qs_rand.sort())

    # 测试含大量重复元素的数组
    arr2 = [2, 2, 1, 3, 2, 2, 1, 1, 2, 3, 2, 2, 1]
    qs_3way = QuickSort3Way(arr2)
    print("三路快速排序结果:", qs_3way.sort())

