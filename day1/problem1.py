import sys
from typing import List


def compute_distance(l1: List[int], l2: List[int]) -> int:
    dist = 0
    for v1, v2 in zip(l1, l2):
        dist += max(v1 - v2, v2 - v1)
    return dist


def test_compute_distance():
    assert compute_distance([0], [1]) == 1
    assert compute_distance([1], [0]) == 1
    assert compute_distance([1, 2], [0, 4]) == 3


def solution(fname: str)->int:
    l1, l2 = [], [] 
    with open(fname) as f:
        for line in f:
            v1, v2 = line.split()
            l1.append(int(v1))
            l2.append(int(v2))
    l1.sort()
    l2.sort()
    return compute_distance(l1, l2)


if __name__ == "__main__":
    fname = "test.txt"
    if len(sys.argv) == 2:
        fname = sys.argv[1]
    print(solution(fname))
