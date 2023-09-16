""" 
Given 2 arrays (assume no duplicates), is one array a rotation of another
same size and elements but start index is different

BigO(n) we are going through each element in each array 2x but O(2n) is O(n) since we drop the constant

select an indexed position in list1 and get its value. Find same element in list2 and check index for index from there.
if any variation then we know its false. if we get through list then its true
"""
import typing as t


def is_rotation(arr1: t.Sequence, arr2: t.Sequence, arr1_index: int = 0):
    if len(arr1) != len(arr2):
        raise ValueError("Sequences must be of equal lengths")

    offset = None
    start_element = arr1[arr1_index]

    # find corresponding element in arr2 and calculate offset
    for counter in range(len(arr2)):
        if arr2[counter] == start_element:
            offset = counter - arr1_index
            break
        counter += 1

    # if offset is None then we did not find the starting element in arr2
    if offset == None:
        raise ValueError("Starting value was not found")

    # check if all elements are the same. The % len(arr2) is to handle the case where
    # the offset is greater than the length of arr2. we want to wrap around to the beginning
    # of arr2.
    for _ in range(len(arr2)):
        arr2_index = (arr1_index + offset) % len(arr2)
        if arr1[arr1_index % len(arr1)] != arr2[arr2_index]:
            return False
        arr1_index += 1

    return True


if __name__ == "__main__":
    print(is_rotation([1, 2, 3, 4, 5], [2, 3, 4, 5, 1]))
    print(is_rotation([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
else:
    import pytest

    @pytest.mark.parametrize(
        "arr1, arr2, start, expected",
        [
            ([1, 2, 3, 4, 5], [4, 5, 1, 2, 3], 0, True),
            ([1, 2, 3, 4, 5], [4, 5, 1, 3, 2], 0, False),
            ([1, 2, 3, 4, 5], [4, 6, 1, 2, 3], 0, False),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 0, True),
            ([1, 2, 3, 4, 5], [5, 1, 2, 3, 4], 0, True),
            ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 0, True),
            ([1, 2, 3, 4, 5], [2, 3, 4, 5, 1], 0, True),
            ([1, 2, 3, 4, 5], [4, 6, 1, 2, 3], 2, False),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 2, True),
            ([1, 2, 3, 4, 5], [5, 1, 2, 3, 4], 2, True),
        ],
    )
    def test_is_rotation(arr1, arr2, start, expected):
        assert is_rotation(arr1, arr2, arr1_index=start) == expected
