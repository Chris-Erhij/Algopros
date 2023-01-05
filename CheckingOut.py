from typing import List


def anagram_solution(s1: str, s2: str) -> bool:

    """ Takes two strings and returns True if anagram, False otherwise
    """

    list_s2: List[str] = list(s2)
    s1_index: int = 0
    is_this_anagram: bool = True

    # Accessing s1 using its length iteratively
    while is_this_anagram and s1_index < len(s1):
        s2_index: int = 0
        found: bool = False

        # Accessing s2 list using its length in a nested iteration
        while not found and s2_index < len(list_s2):
            if s1[s1_index] == s2[s2_index]:
                found: bool = True
            else:
                s2_index += 1

        # Check-out found char in list_s2 (i.e. replace with None)
        if found:
            # noinspection PyTypeChecker
            list_s2[s2_index]: List[str] = None
        else:
            is_this_anagram: bool = False
        s1_index: int = s1_index + 1
    return is_this_anagram


if __name__ == '__main__':
    answer: bool = anagram_solution('abcd', 'dcba')
    if answer:
        print("{}:: they are anagrams of each other.". format(answer))
    else:
        print(F"{answer}:: The two strings are not anagrams of each other.")
