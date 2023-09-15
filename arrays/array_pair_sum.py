"""
Array Pair sum
Given an integer array, output all the unique pairs that sum up to a specific value k.

Example:
pair_sum([1,2,3,2], 4) would return 2 pairs
(1, 3)
(2, 2)
"""
import typing as t


def pair_sum(lst: t.List, target_sum: int) -> t.List[t.Tuple]:
    if len(lst) < 2:
        return set()

    pairs = set()
    seen = set()

    for element in lst:
        # calculate the complement to add up to the sum
        complement = target_sum - element

        # if we have a compliment already found, then we're ready
        # to build the pair
        if complement in seen:
            pairs.add((min(element, complement), max(element, complement)))

        # let's add our element to the set and wait for a complement to match
        seen.add(element)
    return pairs


if __name__ == "__main__":
    list1 = [1, 3, 2, 2]
    list2 = [1, 2, 3, 4, 5]

    list1_result = " ".join(map(str, list(pair_sum(list1, 4))))
    list2_result = " ".join(map(str, list(pair_sum(list2, 2))))

    # print list and right-adjusted result
    print(f"{str(list1):<20} --> {list1_result:>20}")
    print(f"{str(list2):<20} --> {list2_result:>20}")
else:
    import pytest

    @pytest.mark.parametrize(
        ("lst", "target_sum", "expected"),
        [
            pytest.param([2], 4, set(), id="empty list"),
            pytest.param(
                [1, 3, 2, 2, 2, 2],
                4,
                {(1, 3), (2, 2)},
                id="multiple pairs - with duplicates",
            ),
            pytest.param([1, 2, 3, 1], 3, {(1, 2)}, id="single matching pair"),
            pytest.param(
                [1, 4, 3, 4, 5],
                8,
                {(3, 5), (4, 4)},
                id="multiple pairs - no duplicates",
            ),
            pytest.param([1, 2, 3, 4, 5], 2, set(), id="no matching pairs"),  # no pairs
            pytest.param(
                [6, 4, 5], 3, set(), id="no matching pair uneven list"
            ),  # no pairs
        ],
    )
    def test_pair_sum(lst, target_sum, expected):
        assert pair_sum(lst, target_sum) == expected
