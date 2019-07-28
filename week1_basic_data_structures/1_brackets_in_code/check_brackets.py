# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        bracket = Bracket(next, i)
        if next in "([{":
            opening_brackets_stack.append(bracket)

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1
            else:
                if opening_brackets_stack[-1].char == "(" and bracket.char != ")":
                    return i+1
                elif opening_brackets_stack[-1].char == "{" and bracket.char != "}":
                    return i+1
                elif opening_brackets_stack[-1].char == "[" and bracket.char != "]":
                    return i+1
                else:
                    opening_brackets_stack.pop()
    if len(opening_brackets_stack) == 0:
        return "Success"
    return opening_brackets_stack[-1].position + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here

    print(mismatch)


if __name__ == "__main__":
    main()
