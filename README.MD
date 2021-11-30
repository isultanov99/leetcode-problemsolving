# Leetcode problem solving using python3
---
## Contents

1. [1748. Sum of Unique Elements](#sum-of-unique-elements) \
	1.1. [Description](#soue-description) \
	1.2. [Solution](#soue-solution) \
	1.3. [Submission Details](#soue-subdetails)
2. [804. Unique Morse Code Words](#unique-morse) \
	2.1. [Description](#um-description) \
	2.2. [Solution](#um-solution) \
	2.3. [Submission Details](#um-subdetails)

<h2 id="sum-of-unique-elements" >1748. Sum of Unique Elements</h2>
<h3 id="soue-description" >Description</h3>

You are given an integer array `nums`. The unique elements of an array are the elements that appear **exactly once** in the array. \
Return *the ***sum*** of all the unique elements of* `nums`.

Example 1:

```
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
```

Example 2:

```
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.
```

Example 3:

```
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
```

Constraints:

```
	1 <= nums.length <= 100
	1 <= nums[i] <= 100
```

<h3 id="soue-solution" >Solution</h3>

<details>
<summary><a href="sumofunique.py">sumofunique.py</a></summary>

```
class Solution:
	def sumOfUnique(self, nums: List[int]) -> int:
		d = {x:nums.count(x) for x in nums}
		return(sum([i for i in d if d[i] == 1]))
```

</details>

<h3 id="soue-subdetails" >Submission Details</h3>

- **73 / 73** test cases passed.
- Status: **Accepted**
- Runtime: **24 ms** (faster than 99.01% of submissions)
- Memory Usage: **14.2 MB** (less than 73.99% of submissions)

---

<h2 id="unique-morse" >804. Unique Morse Code Words</h2>
<h3 id="um-description" >Description</h3>

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
- `'a'` maps to `".-"`,
- `'b'` maps to `"-..."`,
- `'c'` maps to `"-.-."`, and so on.

For convenience, the full table for the `26` letters of the English alphabet is given below:
```
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
```
Given an array of strings `words` where each word can be written as a concatenation of the Morse code of each letter.

- For example, `"cab"` can be written as `"-.-..--..."`, which is the concatenation of `"-.-."`, `".-"`, and `"-..."`. We will call such a concatenation the <strong>transformation</strong> of a word.

Return *the number of different ***transformations*** among all words we have.*

Example 1:

```
Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".
```

Example 2:

```
Input: words = ["a"]
Output: 1
```

Constraints:

```
1 <= words.length <= 100
1 <= words[i].length <= 12
words[i] consists of lowercase English letters.
```

<h3 id="um-solution" >Solution</h3>

<details>
<summary><a href="./uniquemorse.py">uniquemorse.py</a></summary>

```
class Solution:
	def morsify(self, s: str):
		__eng_to_morse = {
				'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..',
				'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....',
				'i' : '..','j' : '.---', 'k' : '-.-', 'l' : '.-..',
				'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.',
				'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-',
				'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-',
				'y' : '-.--', 'z' : '--..'
				}
		out = ""
		for i in s:
			out += __eng_to_morse.get(i)
		return out

	def uniqueMorseRepresentations(self, words: List[str]) -> int:
		return len(set([self.morsify(s) for s in words]))
```

</details>

<h3 id="um-subdetails" >Submission Details</h3>

- **82 / 82** test cases passed.
- Status: **Accepted**
- Runtime: **28 ms** (faster than 97.11% of submissions)
- Memory Usage: **14.3 MB** (less than 62.42% of submissions)
