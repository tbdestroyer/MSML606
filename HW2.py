import csv
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class HomeWork2:

    # Problem 1: Construct an expression tree (Binary Tree) from a postfix expression
    # input -> list of strings (e.g., [3,4,+,2,*])
    # this is parsed from p1_construct_tree.csv (check it out for clarification)

    # there are no duplicate numeric values in the input
    # support basic operators: +, -, *, /

    # output -> the root node of the expression tree. Here: [*,+,2,3,4,None,None]
    # Tree Node with * as root node, the tree should be as follows
    #         *
    #        / \
    #       +   2
    #      / \
    #     3   4

    def constructBinaryTree(self, input) -> TreeNode:
        # We can use a stack for constructing a BT from a postfix expression.
        # iterate through the passed imput strings/chracters
        stack = []  # create an empty list for stack
        for val in input:
            # if we have an operator, we need two nodes one to the left and right
            # because *, /, + and - are binary operators
            if val in ['+', '-', '*', '/']:
                right = stack.pop()
                left = stack.pop()
                node = TreeNode(val, left, right)
                stack.append(node)
            else:  
                # if we have just a value (not operator), 
                # we just insert TreeNode with value to the stack, left and right becomes none
                stack.append(TreeNode(val))
        return stack[0]  # return root node

    # Problem 2.1: Use pre-order traversal (root, left, right) to generate prefix notation
    # return an array of elements of a prefix expression
    # expected output for the tree from problem 1 is [*,+,3,4,2]
    # you can see the examples in p2_traversals.csv

    def prefixNotationPrint(self, head: TreeNode) -> list:
        prefixList = []
        if head is None: # if root is empty, return empty list
            return []
        # add the root of subtree
        prefixList.append(head.val)
        # add the left sub tree
        prefixList.extend(self.prefixNotationPrint(head.left))
        # add the right sub tree
        prefixList.extend(self.prefixNotationPrint(head.right))
        # return the tree in pre order
        # print(postfixList)
        return prefixList

    # Problem 2.2: Use in-order traversal (left, root, right) for infix notation with appropriate parentheses.
    # return an array of elements of an infix expression
    # expected output for the tree from problem 1 is [(,(,3,+,4,),*,2,)]
    # you can see the examples in p2_traversals.csv

    # don't forget to add parentheses to maintain correct sequence
    # even the outermost expression should be wrapped
    # treat parentheses as individual elements in the returned list (see output)

    def infixNotationPrint(self, head: TreeNode) -> list:
        infixList = []
        if head is None: # if root is empty, return empty list
            return []
        # add opening parenthesis if not a leaf node
        if head.left is not None:
            infixList.append('(')
        # add the left sub tree
        infixList.extend(self.infixNotationPrint(head.left))
        # add the root of subtree
        infixList.append(head.val)
        # add the right sub tree
        infixList.extend(self.infixNotationPrint(head.right))
        # add closing parenthesis if not a leaf node
        if head.right is not None:
            infixList.append(')')
        # return the tree in in-order
        return infixList

    # Problem 2.3: Use post-order traversal (left, right, root) to generate postfix notation.
    # return an array of elements of a postfix expression
    # expected output for the tree from problem 1 is [3,4,+,2,*]
    # you can see the examples in p2_traversals.csv

    def postfixNotationPrint(self, head: TreeNode) -> list:
        postfixList = []
        if head is None: # if root is empty, return empty list
            return []
        # add the left sub tree
        postfixList.extend(self.postfixNotationPrint(head.left))
        # add the right sub tree
        postfixList.extend(self.postfixNotationPrint(head.right))
        # add the root of subtree
        postfixList.append(head.val)
        # return the tree in post order
        # print(postfixList)
        return postfixList
    

class Stack:
    # Implement your stack using either an array or a list
    # (i.e., implement the functions based on the Stack ADT we covered in class)
    # You may use Python's list structure as the underlying storage.
    # While you can use .append() to add elements, please ensure the implementation strictly follows the logic we discussed in class
    # (e.g., manually managing the "top" of the stack
    
    # Use your own stack implementation to solve problem 3

    def __init__(self):
        self.items = []  # use a list

    # add item to the top of stack
    def push(self, item):
        self.items.append(item)
        
    # return true if stack is empty, false otherwise
    def isEmpty(self):
        return len(self.items) == 0

    # return the top item and remove from stack
    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    # return the top item without removing
    def top(self):
        if self.isEmpty():
            raise IndexError("top from empty stack")
        return self.items[-1]
    
    # return the size of stack
    def size(self):
        return len(self.items)

    # Problem 3: Write code to evaluate a postfix expression using stack and return the integer value
    # Use stack which you implemented above for this problem

    # input -> a postfix expression string. E.g.: "5 1 2 + 4 * + 3 -"
    # see the examples of test entries in p3_eval_postfix.csv
    # output -> integer value after evaluating the string. Here: 14

    # integers are positive and negative
    # support basic operators: +, -, *, /
    # handle division by zero appropriately

    # DO NOT USE EVAL function for evaluating the expression

    def evaluatePostfix(self, exp: str) -> int:
        tokens = exp.strip().split()
        if not tokens:
            raise ValueError("Empty postfix expression")
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                # Check for insufficient operands, need at least 2
                if self.size() < 2:
                    raise ValueError("Malformed postfix expression:insufficient operands for operation")
                right = self.pop()
                left = self.pop()
                if token == '+':
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left * right
                elif token == '/':
                    if right == 0:
                        raise ZeroDivisionError("division by zero")
                    result = int(left / right)
                self.push(result)
            else:
                # check the item is a valid integer
                # this also checks an invalid operaion (i.e. not +,-,*,/)
                try:
                    num = int(token)
                except ValueError:
                    raise ValueError(f"Invalid token in postfix expression: {token}")
                self.push(num)
        # check for errors after evaluating the expression
        if self.size() > 1:
            raise ValueError("Malformed postfix expression: too many operands")
        # there should be one item (result) left on the top of the stack
        if self.size() == 0:
            raise ValueError("Malformed postfix expression: no result on stack")
        
        return self.pop()

# Main Function. Do not edit the code below
if __name__ == "__main__":
    homework2 = HomeWork2()

    print("\nRUNNING TEST CASES FOR PROBLEM 1")
    testcases = []
    try:
        with open('p1_construct_tree.csv', 'r') as f:
            testcases = list(csv.reader(f))
    except FileNotFoundError:
        print("p1_construct_tree.csv not found")

    for i, (postfix_input,) in enumerate(testcases, 1):
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)
        output = homework2.postfixNotationPrint(root)

        assert output == postfix, f"P1 Test {i} failed: tree structure incorrect"
        print(f"P1 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 2")
    testcases = []
    with open('p2_traversals.csv', 'r') as f:
        testcases = list(csv.reader(f))

    for i, row in enumerate(testcases, 1):
        postfix_input, exp_pre, exp_in, exp_post = row
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)

        assert homework2.prefixNotationPrint(root) == exp_pre.split(","), f"P2-{i} prefix failed"
        assert homework2.infixNotationPrint(root) == exp_in.split(","), f"P2-{i} infix failed"
        assert homework2.postfixNotationPrint(root) == exp_post.split(","), f"P2-{i} postfix failed"

        print(f"P2 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 3")
    testcases = []
    try:
        with open('p3_eval_postfix.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                testcases.append(row)
    except FileNotFoundError:
        print("p3_eval_postfix.csv not found")

    for idx, row in enumerate(testcases, start=1):
        expr, expected = row

        try:
            s = Stack()
            result = s.evaluatePostfix(expr)
            if expected == "DIVZERO":
                print(f"Test {idx} failed (expected division by zero)")
            else:
                expected = int(expected)
                assert result == expected, f"Test {idx} failed: {result} != {expected}"
                print(f"Test case {idx} passed")

        except ZeroDivisionError:
            assert expected == "DIVZERO", f"Test {idx} unexpected division by zero"
            print(f"Test case {idx} passed (division by zero handled)")