import re

class Solution:
	def reverseVowels(self, s: str) -> str:
		ll = [[m.group() for m in re.finditer(r"[EAOUIeaoui]", s)],
			[m.start(0) for m in re.finditer(r"[EAOUIeaoui]", s)]]
		sl = list(s)

		for i in range(len(ll[1])):
			sl[ll[1][i]] = ll[0][len(ll[1])-i-1]

		return("".join(sl))