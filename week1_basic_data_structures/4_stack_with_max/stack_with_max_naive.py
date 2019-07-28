import sys


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
        self.__stack.pop()
        self.__max.pop()
        self.__max_value = self.__max[-1]
        return self.__max[-1]

    def Max(self):
        assert(len(self.__stack))
        return self.__max[-1]

    def __len__(self):
        return len(self.__stack)


def Main():
    stack = StackWithMax()
    output = []

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            output.append(stack.Max())
        else:
            assert(0)
    return output


print(Main())
