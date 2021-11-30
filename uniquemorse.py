class Solution:
	def morsify(self, s: str):
		__eng_to_morse = {
						'a' : '.-', 'b' : '-...', 'c' : '-.-.',
						'd' : '-..', 'e' : '.', 'f' : '..-.',
						'g' : '--.', 'h' : '....', 'i' : '..',
						'j' : '.---', 'k' : '-.-', 'l' : '.-..',
						'm' : '--', 'n' : '-.', 'o' : '---',
						'p' : '.--.', 'q' : '--.-', 'r' : '.-.',
						's' : '...', 't' : '-', 'u' : '..-',
						'v' : '...-', 'w' : '.--', 'x' : '-..-',
						'y' : '-.--', 'z' : '--..'
						}
		out = ""
		for i in s:
			out += __eng_to_morse.get(i)
		return out

	def uniqueMorseRepresentations(self, words: List[str]) -> int:
		return len(set([self.morsify(s) for s in words]))