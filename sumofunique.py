class Solution:
	def sumOfUnique(self, nums: List[int]) -> int:
		d = {x:nums.count(x) for x in nums}
		return(sum([i for i in d if d[i] == 1]))