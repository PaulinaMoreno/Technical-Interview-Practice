import unittest
'''
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
'''
# We can see that a palindrome mirrors around its center.
# Therefore, a palindrome can be expanded from its center.

# Find the longest palindromic substring in s
# @param {string} input string
# @return {string} answer, longest substring


def question2(s):
    start = 0
    end = 0
    n = len(s)
    for i in range(0, n):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        l = max(len1, len2)
        if l > end - start:
            start = i - (l - 1) / 2
            end = i + l / 2
    return s[start: end + 1]

# Expan around center
# @param {string, int , int}
# @return {int} answer, substring length


def expandAroundCenter(s, left, right):
    L = left
    R = right
    while (L >= 0 and R < len(s) and s[L] == s[R]):
        L -= 1
        R += 1
    return R - L - 1


class Q2Test(unittest.TestCase):
    def test(self):
        self.assertEqual(question2("banana"), "anana")
        self.assertEqual(question2("forgeeksskeegfor"), "geeksskeeg")
        self.assertNotEqual(question2("dabcba"), "aba")

if __name__ == '__main__':
    unittest.main()
