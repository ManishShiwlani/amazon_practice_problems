class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return num
        x = 0
        while num > 0:
            if num % 2 == 0:
                num = num/2
                x += 1
            else:
                num = num - 1
                x += 1
        return x
