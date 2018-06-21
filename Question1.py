"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring
of s. For example: if s = "udacity" and t = "ad", then the function returns
True. Your function definition should look like: question1(s, t) and return a
boolean True or False.
"""
import unittest
# Find out if s1 and s2 strings are anagrams
# @param {string, string} input strings
# @return {bool} answer, True if are anagrams


def is_anagram(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    # Sort a string and then compare with each other
    s1.sort()
    s2.sort()
    return s1 == s2
# Determine whether some anagram of t is a substring of s.
# @param {string, string} input strings
# @return {bool}  answer, True if some angram of t is found in s


def question01(s, t):
    if len(t) > len(s):
        return False
    pattern_length = len(t)
    text_length = len(s)
    # s2[start:end] represents the substring in s2
    start = 0
    end = pattern_length

    while(end <= text_length):
        sub = s[start:end]
        if is_anagram(sub, t):
            return True
        else:
            start += 1
            end += 1
    return False


class Q1Test(unittest.TestCase):
    def test01(self):
        self.assertEqual(question01("udacity", "ad"), True)
        self.assertEqual(question01("roma", "or"), True)
        self.assertEqual(question01("udacity", "udo"), False)
        self.assertEqual(question01("udacity", "citi"), False)

if __name__ == '__main__':
    unittest.main()
