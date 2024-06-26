'''
You are given two strings s and t.
String t is generated by random shuffling string s and then add one more letter at a random position.
Return the letter that was added to t.

Example 1:
Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

Example 2:
Input: s = "", t = "y"
Output: "y"
 
Constraints:
0 <= s.length <= 1000
t.length == s.length + 1
s and t consist of lowercase English letters.
'''


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = {}
        # Count the occurrences of characters in s.
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        # Subtract the occurrences of characters in t.
        for char in t:
            if char in count and count[char] > 0:
                count[char] -= 1
            # If the character is not in count or its count is already 0, it's the extra character.
            else:
                return char


s = "abcd"
t = "abcde"
solution = Solution()
print(solution.findTheDifference(s, t))
