import sys
from typing import List
from copy import deepcopy

def is_safe_pair(report: List[int], ix: int, skip_ix: int)->bool:
    left_ix = ix
    right_ix = ix + 1
    val_left = report[left_ix]
    val_right = report[right_ix]
    if left_ix == skip_ix:
        if left_ix > 0:
            val_left = report[left_ix - 1]
        else:
            # condition definitely holds
            val_left = val_right - 1
    if right_ix == skip_ix:
        if right_ix < len(report) - 1:
            val_right = report[right_ix + 1]
        else:
            # condition definitely holds
            val_right = val_left + 1
    return 1 <= val_right - val_left <= 3

def test_is_safe_pair():
    report = [100, 3, 5]
    assert is_safe_pair(report, 0, 0)
    assert is_safe_pair(report, 1, 0)
    report = [3, 5, 100]
    assert is_safe_pair(report, 1, 2)
    report = [3, 100, 5]
    assert is_safe_pair(report, 0, 1)
    assert is_safe_pair(report, 1, 1)

def test_not_is_safe_pair():
    report = [100, 3, 5]
    assert not is_safe_pair(report, 0, 2)
    assert not is_safe_pair(report, 0, 1)
    report = [3, 5, 100]
    assert not is_safe_pair(report, 0, 1)
    assert not is_safe_pair(report, 1, 0)
    report = [3, 100, 5]
    assert not is_safe_pair(report, 1, 0)


def is_safe_increasing(report: List[int])->bool:
    for skip_ix in range(len(report)):
        all_safe = True
        for ix in range(len(report) - 1):
            if is_safe_pair(report, ix, skip_ix):
                continue
            else:
                all_safe = False
                break
        if all_safe:
            return True
    return False


def test_is_safe_increasing_no_bad_levels():
    assert is_safe_increasing([1])
    assert is_safe_increasing([1, 2])
    assert is_safe_increasing([1, 3])
    assert is_safe_increasing([1, 4])
    assert is_safe_increasing([1, 3, 5])
    assert is_safe_increasing([1, 1])
    assert is_safe_increasing([1, 5, 2])
    assert is_safe_increasing([1, 5, 7])

def test_not_is_safe_increasing():
    assert not is_safe_increasing([1, 1, 1])
    assert not is_safe_increasing([1, 1, 6])
    assert not is_safe_increasing([1, 0, -1])
    assert not is_safe_increasing([1, 100, 200])
    assert not is_safe_increasing([1,2,7,8,9])


def solution(fname: str)->int:
    count_safe = 0
    with open(fname) as f:
        for line in f:
            report = list(map(int, line.split()))
            report1 = deepcopy(report)
            report1.reverse()
            if is_safe_increasing(report) or is_safe_increasing(report1):
                count_safe += 1
    return count_safe

if __name__ == '__main__':
    fname = 'test.txt'
    if len(sys.argv) == 2:
        fname = sys.argv[1]
    print(solution(fname))
