# Leetcode problem solving using python3
---
## Contents

1. [1748. Sum of Unique Elements](#sum-of-unique-elements) \
	1.1. [Description](#soue-description) \
	1.2. [Solution](#soue-solution) \
	1.3. [Submission Details](#soue-subdetails) \


<h2 id="chapter-i" >Chapter I</h2>
<h3 id="soue-description" >Description</h3>

- You are given an integer array <code>nums</code>. The unique elements of an array are the elements that appear <strong>exactly once</strong> in the array.

- Return <em>the <strong>sum</strong> of all the unique elements of </em><code>nums</code>.

- Example 1:
```
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
```
- Example 2:
```
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.
```

- Example 3:
```
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
```

- Constraints:

```
	1 <= nums.length <= 100
	1 <= nums[i] <= 100
```

<h3 id="soue-description" >Solution</h3>

[sumofunique.py](./sumofunique.py)
```
class Solution:
	def sumOfUnique(self, nums: List[int]) -> int:
		d = {x:nums.count(x) for x in nums}
		return(sum([i for i in d if d[i] == 1]))
```

<h3 id="soue-subdetails" >Submission Details</h3>

- **73 / 73** test cases passed.
- Status: Accepted
- Runtime: **24 ms** (faster than 99.01% of submissions)
- Memory Usage: **14.2 MB** (less than 73.99% of submissions)