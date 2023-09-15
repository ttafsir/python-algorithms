"""
Take an array with positive and negative integers and find the 
maximum sum of that array
"""
import typing as t


def largest_sum(lst: t.List) -> int:
    if len(lst) == 0:
        raise ValueError("Need at least one element")

    # start from first element in the list as opposed to defaulting from 0
    # to account for negative numbers
    current_sum = total_sum = lst.pop()
    for item in lst:
        current_sum = max((current_sum + item), item)
        total_sum = max(current_sum, total_sum)
    return total_sum


if __name__ == "__main__":
    print(largest_sum([7, 1, 2, -1, 3, 4, 10, -12, 3, 21, -19]))
    print(largest_sum([-1, 1]))
else:
    import pytest

    @pytest.mark.parametrize(
        ("lst", "expected"),
        [
            pytest.param(
                [7, 1, 2, -1, 3, 4, 10, -12, 3, 21, -19],
                38,
                id="multiple positive and negative numbers",
            ),
            pytest.param([-1, 1], 1, id="two numbers"),
            pytest.param([1, 2, 3, 4, 5], 15, id="all positive numbers"),
            pytest.param([-1, -2, -3, -4, -5], -1, id="all negative numbers"),
            pytest.param([1, 2, 3, 4, -5], 10, id="positive and negative numbers"),
        ],
    )
    def test_largest_sum(lst, expected):
        assert largest_sum(lst) == expected
