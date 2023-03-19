def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2, -1, -1):
        heapify(data, i, swaps)
    return swaps


def heapify(data, i, swaps):
    n = len(data)
    min_idx = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] < data[min_idx]:
        min_idx = left
    if right < n and data[right] < data[min_idx]:
        min_idx = right

    if i != min_idx:
        swaps.append((i, min_idx))
        data[i], data[min_idx] = data[min_idx], data[i]
        heapify(data, min_idx, swaps)


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    m = len(swaps)
    assert m <= 4 * n
    print(m)
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
