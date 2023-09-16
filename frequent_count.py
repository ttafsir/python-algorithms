"""
Given an array what is the most frequently occuring element
"""
import typing as t 


def frequent_count(arr1: t.List):
    counter = {}
    max_count = 0
    max_items = None

    for element in arr1:
        try:
            counter[element] += 1
        except KeyError:
            counter[element] = 1

    for element in counter:
        if counter[element] > max_count:
            max_count = counter[element]
            max_item = element
    return (max_item, max_count)


if __name__ == "__main__":
    print(frequent_count([1, 3, 4, 6, 7, 9, 1, 1, 1]))

else:
    import pytest

    @pytest.mark.parametrize(
        "arr1, expected",
        [
            pytest.param([1, 3, 4, 6, 7, 9, 1, 1, 1], (1, 4), id="one max element"),
            pytest.param([1, 1, 2, 2, 3, 4, 5], (1, 2), id="2-way tie"),
            pytest.param([1, 2, 3, 4, 5], (1, 1), id="all tied"),
        ],
    )
    def test_frequent_count(arr1, expected):
        assert frequent_count(arr1) == expected

