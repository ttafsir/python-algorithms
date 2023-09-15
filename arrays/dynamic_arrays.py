"""
Given two strings, check to see if they are anagrams. An anagram is when 
the two string can be written using the exact same letters (so you can 
just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."
"clint eastwood" is an anagram of "old west action"
Note: Ignore spaces and capitalization. So "d go" is an anagram of "God"
and "dog" and "o d g".
"""


# quick and easy way to do it in Python. For an interview or 
# learning setting, it may not sufficiently help to explain 
# the process
def is_anagram_not_optimal(string1: str, string2: str) -> bool:
    string1 = string1.replace(" ", "").replace(".", "").lower()
    string2 = string2.replace(" ", "").replace(".", "").lower()
    if len(string1) != len(string2):
        return False
    return sorted(string1) == sorted(string2)


# The following version is an example that is more optimal for
# a conversation around how to achiveve the goal
def is_anagram_optimal(string1: str, string2: str) -> bool:
    string1 = string1.replace(" ", "").replace(".", "").lower()
    string2 = string2.replace(" ", "").replace(".", "").lower()

    # if the strings are not the same length, they're definitely 
    # not anagrams!
    if len(string1) != len(string2):
        return False

    # initialize a dict to keep count of letters
    count = {}

    # let's count our letters in the first string. This is much easier
    # with Counter, but again it's neat to show the process
    for letter in string1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # Not needed, but a sanity check to ensure the length or the string
    # equal the total count for the values
    if len(string1) != sum(count.values()):
        return False

    # if all is equal, we should be able to "deduct" every letter in 
    # string 2 from the "bank" we created using string 1
    for letter in string2:
        if letter in count:
            count[letter] -= 1
        else:
            return False

    # we should be left with 0
    return sum(count.values()) == 0


if __name__ == "__main__":
    string1 = input("First Phrase: ")
    string2 = input("Second Phrase: ")
    result = "are" if is_anagram_not_optimal(string1, string2) else "are NOT"
    print(f"the strings {result} anagrams!")

else:
    import pytest

    @pytest.mark.parametrize(
        ("string1", "string2", "expected"),
        [
            ("public relations", "crap built on lies.", True),
            ("clint eastwood", "old west action", True),
            ("d go", "God", True),
            ("dog", "o d g", True),
            ("dogg", "o d g", False),
            ("aaa", "bbb", False),
        ],
    )
    def test_anagrams(string1, string2, expected):
        assert is_anagram_not_optimal(string1, string2) == expected

    @pytest.mark.parametrize(
        ("string1", "string2", "expected"),
        [
            ("public relations", "crap built on lies.", True),
            ("clint eastwood", "old west action", True),
            ("d go", "God", True),
            ("dog", "o d g", True),
            ("dogg", "o d g", False),
            ("aaa", "bbb", False),
        ],
    )
    def test_anagrams_optimal(string1, string2, expected):
        assert is_anagram_optimal(string1, string2) == expected
