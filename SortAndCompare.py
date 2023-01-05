from typing import List;

def anagram_solution_2(s3: str, s4: str) -> bool:

    """
        Returns true if strings are anagrams, false otherwise

    """
    s3_con: List[str] = list(s3);
    s4_con: List[str] = list(s4);

    s3_con: List[str].sort();
    s4_con: List[str].sort();

    str_index: int = 0;
    detected: bool = True;

    while str_index < len(s4_con) and detected:
        if s3_con[str_index] == s4_con[str_index]:

            detected = True;
            str_index += 1;

        else:
            detected = False;
    return detected;


def main(s1: str, s2: str) -> bool:
    if s1 and s2:
        output: bool = anagram_solution_2(s1, s2);
    return F" The output of the function is:: {output}";

if __name__== '__main__':
    pass
