'''
Number of distinct subsequences
Given a string consisting of lower case English alphabets, the task is to find the number of distinct subsequences of the string.
Input: 
s = "ggg"
Output: 
4
Explanation: 
The four distinct subsequences are "", "g", "gg", "ggg".
'''

class Solution:
	def distinctSubsequences(self, S):
		n = len(S)
        ans = set()
        st = ""
        ans.add(" ")
        ans.add(S)
        for i in range(n):
            ans.add(S[i])
            for j in range(i+1,n):
                st += S[j]
                st += S[i]
                ans.add(st)
                st = ""

        return len(ans)
if _name_ == '_main_':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.distinctSubsequences(s)
		print(answer)
