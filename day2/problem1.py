import sys
from typing import List

def is_safe(report: List[int])->bool:
    if len(report) == 1:
        return True
    def _is_safe(is_increasing: bool)->bool:
        for ix in range(1, len(report)):
            if report[ix] > report[ix - 1] and report[ix] - report[ix - 1] <= 3 and is_increasing:
                continue
            elif report[ix] < report[ix - 1] and report[ix - 1] - report[ix] <= 3 and not is_increasing:
                continue
            else:
                return False
        return True
    return _is_safe(True) or _is_safe(False)

def test_is_safe():
    assert is_safe([1])
    assert is_safe([1, 2])
    assert is_safe([1, 3])
    assert is_safe([1, 4])
    assert is_safe([1, 2, 4])
    assert is_safe([2, 1])
    assert is_safe([3, 1])
    assert is_safe([4, 1])
    assert is_safe([4, 2, 1])

def test_not_is_safe():
    assert not is_safe([1, 1])
    assert not is_safe([1, 5])
    assert not is_safe([1, 3, 2])
    assert not is_safe([1, 2, 6])

def solution(fname: str)->int:
    count_safe = 0
    with open(fname) as f:
        for line in f:
            report = list(map(int, line.split()))
            if is_safe(report):
                count_safe += 1
    return count_safe

if __name__ == '__main__':
    fname = 'test.txt'
    if len(sys.argv) == 2:
        fname = sys.argv[1]
    print(solution(fname))
