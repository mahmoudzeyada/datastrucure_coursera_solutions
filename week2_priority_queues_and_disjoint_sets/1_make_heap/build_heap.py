# python3
def parent(i):
    return int((i-1)/2)


def left(i):
    return 2*i+1


def right(i):
    return 2*i+2


swaps = []


def heapify(a, i):
    ''' function for mantaing max heap property time-complexity = O(log n) but that it is that is optimized version  '''
    l = left(i)
    r = right(i)

    if l <= len(a)-1 and a[i] > a[l]:
        smallest = l
    else:
        smallest = i

    if r <= len(a)-1 and a[smallest] > a[r]:
        smallest = r

    if smallest != i:
        a[i], a[smallest] = a[smallest], a[i]
        swaps.append((i, smallest))
        heapify(a, smallest)


def build_heap(data):
    for i in range(int(len(data)/2), -1, -1):
        heapify(data, i)
    return swaps

    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    # return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
