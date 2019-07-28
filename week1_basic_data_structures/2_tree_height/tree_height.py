# python3
import sys
import threading

# this my solution


def compute_height(n, parents):
    # funny thoughts
    # return len(list(dict.fromkeys(parents)))

    hights = [0] * n
    for index in range(n):
        current_node_index = index
        hight = 0
        while current_node_index != -1:
            if hights[current_node_index] != 0:
                hight += hights[current_node_index]
                break
            hight += 1
            current_node_index = parents[current_node_index]

        current_node_index = index
        while current_node_index != -1:
            if hights[current_node_index] != 0:
                break
            hights[current_node_index] = hight
            hight -= 1
            current_node_index = parents[current_node_index]
    return max(hights)

    # maxHeight = 0
    # heights = [0] * len(parents)
    # for vertex in range(n):
    #     height = 0
    #     i = vertex
    #     while i != -1:
    #         if (heights[i] != 0):
    #             height += heights[i]
    #             break
    #         height += 1
    #         i = parents[i]
    #     maxHeight = max(maxHeight, height)
    #     i = vertex
    #     while (i != -1):
    #         if (heights[i] != 0):
    #             break
    #         heights[i] = height
    #         height -= 1
    #         i = parents[i]
    # return maxHeight


# trying to make to recursive function
# def compute_height(n, parentss, index=0, hight=0, current_parents=0):

#     if index == n-1:
#         return 0
#     if l[index] != -1:
#         return 1

#     if current_parents == -1:
#         l[index] = l[current_parents] + 1

#     else:
#         l[index] = compute_height(n, parentss, index, hight,
#                                   parentss[current_parents]) + 1

#     compute_height(n, parentss, index+1, 0, index+1)

#     return l[index]


# def compute_height(n, parentss):
#     # We make a list to keep track of which nodes have already been visited
#     heights = [-1 for x in range(n)]

#     # Make sure you visit every node if it is not already visited
#     for i, val in enumerate(heights):
#         if (val == -1):
#             recurse_compute_height(n, parentss, i, heights)

#     return(max(heights))

# # Recursively computes the height for the current node


# def recurse_compute_height(n, parentss, index, heights):
#     parents = parentss[index]

#     # Base case for when you reach the root
#     if parents == -1:
#         return 1

#     # Leverage the parents's height, if already computed
#     if (heights[parents] != -1):
#         heights[index] = heights[parents] + 1
#     # Or compute the node's and its parentss's height
#     else:
#         heights[index] = recurse_compute_height(
#             n, parentss, parents, heights) + 1

#     return heights[index]


# my bad code
# l = []
# def compute_height(n, parentss, postion=0, hight=0, max_hight=0, current=0):

#     if postion == n-1:
#         return

#     if current != -1:
#         compute_height(n, parentss, postion, hight+1,
#                        max_hight, parentss[current])
#     max_hight = max(max_hight, hight)
#     l.append(max(max_hight, hight))

#     compute_height(n, parentss, postion+1, 0, max_hight, postion+1)

    # # Replace this code with a faster implementation
    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         # this is bad code because it might cause errors i
    #         # f current > len(parentss) and it will cause infinite
    #         # loop if index = current
    #         current = parentss[current]
    #         # this is my bullshit code it desnot mean anything but i get it
    #         # current = parentss[random.randint(0, n-1)]
    #     max_height = max(max_height, height)
    # return max_height
# with open('tests/01', 'r') as f:
#     lines = f.readlines()


# def data():
#     return lines.pop(0)


# input = data


def main():

    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(3**27)   # new thread will get stack of such size
    thread = threading.Thread(target=main)
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))
