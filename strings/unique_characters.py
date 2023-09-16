"""
Given a string, are all characters unique?
"""

def all_unique(a_string: str):
    seen = set()
    for c in a_string:
        if c in seen:
            return False 
        seen.add(c)
    return True

def all_unique2(a_string: str):
    a_string.replace(" ", "").lower()
    return len(set(a_string)) == len(a_string)

def all_unique3(a_string: str):
    char_counts = [0] * 128  # Assuming ASCII character set
    for c in a_string:
        # get the ASCII code for the character
        char_code = ord(c)
        # if we have seen this character before, then we have a duplicate
        if char_counts[char_code] > 0:
            return False
        char_counts[char_code] += 1
    return True

if __name__ == "__main__":
    print(all_unique("abcdefg"))
    print(all_unique("abcdefga"))

    print(all_unique2("abcdefg"))
    print(all_unique2("abc def ga"))

    print(all_unique3("abcdefg"))
    print(all_unique3("ab cdef ga"))
else:
    import pytest 

    @pytest.mark.parametrize(
        "a_string, expected",
        [
            pytest.param("abcdefg", True, id="unique"),
            pytest.param("abcdefga", False, id="not unique"),
        ],
    )
    def test_unique(a_string, expected):
        assert all_unique(a_string) == expected