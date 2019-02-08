# CSC499
# Assignment 2
# Ethan Pellittiere
# Purpose: Remove duplicates from linked list
#

def main():

    # worst case list: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    # expected output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    # create linked list
    worst = []
    for i in range(0, 10):
        worst.append(Node(i))
        worst[i].set_head(worst[0])
        if i > 0:
            worst[i-1].set_next(worst[i])

    # random list (6, 0, 4, 7, 7, 1, 3, 0, 7, 1)
    # expected output: (6, 0, 4, 7, 1, 3)
    rand_v = [6, 0, 4, 7, 7, 1, 3, 0, 7, 1]

    # create linked list
    rand = []
    for i in range(0, 10):
        rand.append(Node(rand_v[i]))
        rand[i].set_head(rand[0])
        if i > 0:
            worst[i - 1].set_next(rand[i])

    # print before and after for lists
    print("Worst case start: ")
    print_list(worst)
    worst = remove_dupes(worst)
    print("Worst case end: ")
    print_list(worst)

    print("Random case start: ")
    print_list(rand)
    rand = remove_dupes(rand)
    print("Random case end: ")
    print_list(rand)


def print_list(l_list):
    current = l_list[0]
    while current:
        print(current.datum, end=" ")
        # if not current.next:
        #     break
        current = current.next
    print()


def remove_dupes(l_list):
    current = l_list[0]
    last = ""
    while current:
        inner = current.head
        while inner != current:
            if inner.datum == current.datum:
                last.next = current.next
            inner = inner.next
        last = current
        current = current.next
    return list


class Node:
    def __init__(self, value):
        self.datum = value
        self.next = None
        self.head = None

    def set_next(self, next_node):
        self.next = next_node

    def set_head(self, head_node):
        self.head = head_node


main()
