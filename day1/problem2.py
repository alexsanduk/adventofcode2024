import sys
from typing import List
from collections import Counter


def compute_similarity(l1: List[int], l2: List[int]) -> int:
    counter1 = Counter(l1)
    counter2 = Counter(l2)
    sim = 0
    for v1, c1 in counter1.items():
        c2 = counter2.get(v1, 0)
        sim += v1 * c1 * c2
    return sim


def test_compute_similarity():
    assert compute_similarity([0], [1]) == 0
    assert compute_similarity([1], [0]) == 0
    assert compute_similarity([1, 2], [0, 1]) == 1
    assert compute_similarity([3, 2], [0, 3]) == 3
    assert compute_similarity([3, 3], [0, 3]) == 6
    assert compute_similarity([3, 3, 2], [1, 3, 3]) == 12


def solution(fname: str) -> int:
    l1, l2 = [], []
    with open(fname) as f:
        for line in f:
            v1, v2 = line.split()
            l1.append(int(v1))
            l2.append(int(v2))
    return compute_similarity(l1, l2)


if __name__ == "__main__":
    fname = "test.txt"
    if len(sys.argv) == 2:
        fname = sys.argv[1]
    print(solution(fname))
