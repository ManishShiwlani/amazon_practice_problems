## Solution - 1
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        num = 0
        for i in J:
            x = i
            for j in S:
                y = j
                if x == y:
                    num += 1
        return num

# Solution - 2


class Solution(object):
    def numJewelsInStones(self, J, S):
        jewel_set = set(J)
        return sum(s in jewel_set for s in S)
