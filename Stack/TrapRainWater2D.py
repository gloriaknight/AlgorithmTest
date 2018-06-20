# -*- coding:UTF-8 -*
'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0

        l = 0
        r = len(height) - 1
        lmax = 0
        rmax = 0
        ret = 0

        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])

            if lmax < rmax:
                ret = ret + (lmax - height[l])
                l = l + 1
            else:
                ret = ret + (rmax - height[r])
                r = r - 1

        return ret


if __name__ == "__main__":
    print("Hello World!")
    test = Solution()
    print test.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
