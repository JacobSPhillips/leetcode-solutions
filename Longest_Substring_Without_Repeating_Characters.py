'''
Problem statement

this is edited again

Given a string s, find the length of the longest substring that contains no repeating characters.

A substring is a contiguous sequence of characters within a string.
Examples
Example 1
Input:  s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring
             without repeating characters.


Example 2
Input:  s = "bbbbb"
Output: 1
Explanation: "b" is the longest valid substring.


Example 3
Input:  s = "pwwkew"
Output: 3
Explanation: "wke" is a valid longest substring.


Example 4
Input:  s = ""
Output: 0


Constraints
- 0 <= len(s) <= 50,000
- s may contain letters, digits, symbols, and spaces.
'''


def length_of_longest_substring(s: str) -> int:
    # see if character in seen
    # if seen, is the character in the window
    # add one to length
    # add the character and index to seen
    # compare length to max length
    left = 0
    max_length = 0
    seen = {}
    for index, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = index
        length = index - left + 1
        max_length = max(length, max_length)
    return max_length

s= "abba"
print(length_of_longest_substring(s))
