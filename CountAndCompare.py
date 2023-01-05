from typing import List
# ## An anagram solution: "count and compare" algorithm ##


def anagram_solution_3(s1: str, s2: str) -> bool:

    """ Returns true if two strings are anagrams, false otherwise
    """

    c1: List[int] = [0] * 26
    c2: List[int] = [0] * 26

    for s1_index in range(0, len(s1), 1):
        pos: int = ord(s1[s1_index]) - ord('a')
        c1[pos] += 1

    for s2_index in range(0, len(s2), 1):
        pos: int = ord(s2[s2_index]) - ord('a')
        c2[pos] += 1

    found: bool = True
    j: int = 0

    while found and j < 26:
        if c1[j] == c2[j]:

            found: bool = True
            j += 1
        else:
            found: bool = False
    return found
