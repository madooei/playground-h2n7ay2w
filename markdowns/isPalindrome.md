# Palindrome

A palindrome is a word that is spelled the same forward and backward. 
For example, `rotor` and `redder` are palindromes, but `motor` is not.

How can you use recursion to determine whether a word is a palindrome? 

?[What would be the base case?]
-[ ] A string with two identical letters
-[ ] A string with one character
-[x] An empty string


::: What would be the recursive case? 

Think of converting the original problem to a sub-problem of smaller size.

:::

@[Implement your recursive solution.]({"stubs": ["isPalindrome.py"], "command": "python3 test_isPalindrome.py"})


---


@[Implement your recursive solution.]({"stubs": ["exp.py"], "command": "python3 test_exp.py"})


---


@[Implement your recursive solution.]({"stubs": ["count_paths.py"], "command": "python3 test_count_paths.py"})


---

```python runnable
# REQUIRES: n >= 1
# EFFECTS: prints numbers from n to 1
def count(n):
    for k in range(n, 0, -1):
        print(k)


count(5)
```
