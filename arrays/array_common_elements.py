"""
Common Elements in Two Sorted Arrays
Given two sorted arrays (ascending), find the number of elements in common. 
Example: [1,3,4,6,7,9] and [1,2,4,5,9,10] => 3 (1,4,9)
"""
import typing as t


def common_elements(arr1: t.Sequence, arr2: t.Sequence):
    pos1 = 0
    pos2 = 0
    results = []

    arr1.sort()
    arr2.sort()

    while pos1 < len(arr1) and pos2 < len(arr2):
        if arr1[pos1] == arr2[pos2]:
            results.append(arr1[pos1])
            pos1 += 1
            pos2 += 1
        elif arr1[pos1] > arr2[pos2]:
            pos2 += 1
        else:
            pos1 += 1
    return results


if __name__ == "__main__":
    print(common_elements([1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10]))
else:
    import pytest

    @pytest.mark.parametrize(
        "arr1, arr2, expected",
        [
            pytest.param(
                [1, 3, 4, 6, 7, 9],
                [1, 2, 4, 5, 9, 10],
                [1, 4, 9],
                id="some common elements",
            ),
            pytest.param(
                [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [], id="no common elements"
            ),
            pytest.param(
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                id="all common elements",
            ),
            pytest.param(
                [1, 2, 3, 4, 5],
                [3, 4, 5, 1, 2],
                [1, 2, 3, 4, 5],
                id="common elements, not sorted",
            ),
        ],
    )
    def test_common_elements(arr1, arr2, expected):
        assert common_elements(arr1, arr2) == expected
