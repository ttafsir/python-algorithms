"""
Given a string of words, reverse all of the words

start = "This is the best"
finish = "best the is This"

"""


def easy_reverse(words: str):
    return " ".join(words.split()[::-1])


def reverse_method(phrase: str):
    words = phrase.split()
    words.reverse()
    return " ".join(words)


def manual_reverse(phrase: str):
    length = len(phrase)
    idx = 0
    words = []
    spaces = [" ", "\t"]

    while idx < length:
        if phrase[idx] not in spaces:
            letter = phrase[idx]
            word_start = idx

            # while we have non-space characters
            while idx < length and phrase[idx] not in spaces:
                idx += 1

            words.append(phrase[word_start:idx])

        # if we hit a space just increment the idx to move to the
        # next letter
        idx += 1

    return " ".join(reversed(words))


if __name__ == "__main__":
    print(easy_reverse("This is the best"))
    print(reverse_method("This is the best"))
    print(manual_reverse("This is the best"))
else:
    import pytest

    @pytest.mark.parametrize(
        ("words", "expected"),
        [
            pytest.param("This is the best", "best the is This", id="basic"),
            pytest.param("  This is the best  ", "best the is This", id="with spaces"),
            pytest.param("This, is the best", "best the is This,", id="with comma"),
        ],
    )
    def test_easy_reverse(words, expected):
        assert easy_reverse(words) == expected
