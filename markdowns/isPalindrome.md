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


```python runnable
# REQUIRES: n >= 0
# EFFECTS: return value is the n!
def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod
  
# Print n! for n={0,1,2,3,4,5}
for n in range(6):
    print("{}! = {}".format(n,factorial(n)))
```

```python runnable
# REQUIRES: n >= 0
# EFFECTS: return value is the n!
def factorial(n):
    if n==0:  # Base case
        return 1
    else:     # Recursive case
        return factorial(n-1) * n
  
# Print n! for n={0,1,2,3,4,5}
for n in range(6):
    print("{}! = {}".format(n,factorial(n)))
```