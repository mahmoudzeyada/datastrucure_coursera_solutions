# python3
class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.__max = []
        self.__max_value = 0

    def Push(self, a):
        self.__stack.append(a)
        self.__max_value = max(self.__max_value, a)
        self.__max.append(self.__max_value)

    def Pop(self):
        assert(len(self.__stack))
        a = self.__stack.pop()
        self.__max.pop()
        if len(self.__max) == 0:
            self.__max_value = 0
        else:
            self.__max_value = self.__max[-1]
        return a

    def Max(self):
        if len(self.__stack) == 0:
            return 0
        return self.__max[-1]

    def __len__(self):
        return len(self.__stack)


class Queue:
    def __init__(self):
        self.__stack1 = StackWithMax()
        self.__stack2 = StackWithMax()

    def enqueue(self, a):
        self.__stack1.Push(a)

    def dequeue(self):
        if len(self.__stack1) == 0:
            if len(self.__stack2) == 0:
                return False

        if len(self.__stack2) == 0:
            while(len(self.__stack1) != 0):
                a = self.__stack1.Pop()
                self.__stack2.Push(a)
        return self.__stack2.Pop()

    def max(self):
        return max(self.__stack1.Max(), self.__stack2.Max())


def max_sliding_window_naive(sequence, m):
    maximums = []
    q = Queue()
    for index, val in enumerate(sequence, start=1):
        q.enqueue(val)
        if index >= m:
            maximums.append(q.max())
            q.dequeue()

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(" ".join(map(str, max_sliding_window_naive(input_sequence, window_size))))
