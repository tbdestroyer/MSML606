# Spring 2026 MSML606 HW2

**Deadline:** 2/25 (Wednesday)

## Overview

This assignment focuses on expression trees, tree traversal algorithms, and stack-based expression evaluation. You will implement data structures and algorithms that demonstrate the relationship between tree representations of mathematical expressions and their evaluation.

Boilerplate code (`HW2.py`) and three test-case CSV files are provided on ELMS.

## General Instructions

- Do not directly copy content from textbooks, other individuals’ work, AI-generated outputs, online sources, or any material that is not your own.
- Collaboration and consulting resources are encouraged, but all written responses must reflect your own understanding.
- Add justifications/explanations to all answers (points are awarded for explanation quality).
- Include your GitHub repository link for this part.
- Commit history will be reviewed. Pushing the entire assignment in one commit may be treated as a red flag.
- Write code comments in your own words.

### External Source / AI Usage Policy

Before submitting, review the external-source policy in the syllabus. You must either:

1. Cite any external sources used (including AI tools), **or**
2. Explicitly state that no external sources were used.

Submissions without this statement receive **no points**.

## Part I (Programming): Stacks and Binary Trees

### Problem 1: Construct an Expression Tree from Postfix

Generate a binary expression tree from a postfix expression.

**Requirements**

- Input is a list of strings parsed from a comma-separated CSV.
- Example input format: `["3", "4", "+", "2", "*"]`
- Support operators: `+`, `-`, `*`, `/`
- Return the root node of the constructed expression tree.

**Example**

Input: `3, 4, +, 2, *`

Expected tree:

```text
		*
	 / \
	+   2
 / \
3   4
```

### Problem 2: Traversals (Prefix, Infix, Postfix)

Implement functions to print prefix, infix, and postfix expressions using tree traversal methods:

- Prefix: pre-order `(root, left, right)`
- Infix: in-order `(left, root, right)` with parentheses
- Postfix: post-order `(left, right, root)`

**Requirements**

- Return each expression as a list of elements.
- For infix, include parentheses to preserve operator precedence (including the outermost expression).
- Treat parentheses as individual elements in the returned list.
- Handle empty trees gracefully.

**Example** (using the tree from Problem 1)

- Prefix: `*, +, 3, 4, 2`
- Infix: `(, (, 3, +, 4, ), *, 2, )`
- Postfix: `3, 4, +, 2, *`

### Problem 3: Evaluate a Postfix Expression Using a Stack

Implement a function that evaluates postfix expressions **without constructing a tree**.

**Requirements**

- Accept postfix input as a **space-separated string** (unlike Problem 1’s comma-separated input).
- Implement your own Stack ADT using an array/list.
	- You may use Python list as storage.
	- Using `.append()` is allowed, but stack behavior must follow class logic discussed in class (including managing stack top behavior).
	- Use your own stack implementation for this problem.
- Support operators: `+`, `-`, `*`, `/`
- Return the numeric result.
- Handle division by zero appropriately (e.g., raise `ZeroDivisionError` or equivalent behavior expected by tests).

**Example**

Input: `5 1 2 + 4 * + 3 -`

Equivalent infix expression:

```text
5 + ((1 + 2) * 4) - 3 = 5 + 12 - 3 = 14
```

Expected output: `14`

### Problem 4: Explain Edge Case Handling

Describe and implement handling for the following edge cases:

- Empty postfix expressions
- Malformed postfix expressions (insufficient operands, too many operands)
- Division by zero
- Invalid tokens (non-numeric operands, unsupported operators)
- Very large numbers or results
- Negative numbers in expressions

**Requirements**

- Include code comments explaining edge case handling.
- Implement appropriate error handling (exceptions or return values).
- Provide test cases that demonstrate edge case handling.
- Document your approach in the report.

## Rubric for Part I (Max: 21 Marks)

| Problem | Criteria | Marks |
|---|---|---:|
| Problem 1: Construct expression tree | Correct tree construction (3), handling invalid sequences (3) | 6 |
| Problem 2: Print functions | Correct prefix (2), infix (2), postfix (2) | 6 |
| Problem 3: Postfix evaluation via stack | Correct expression evaluation (3), handling division by zero (3) | 6 |
| Problem 4: Edge case handling | Authenticity (1.5), clear explanation of all edge cases (1.5) | 3 |
