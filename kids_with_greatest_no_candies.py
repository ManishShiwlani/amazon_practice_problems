class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        maxCandiesList = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                maxCandiesList.append(True)
            else:
                maxCandiesList.append(False)
        return maxCandiesList
