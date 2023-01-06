# How to write self-producing program in Python 3

1. write something like this. The comment in the second line can be any comment
```python
s = ''
# some comments
print("s = " + s.__repr__() + s, end="")
```

2. run the `generate_s.py` to generate the content for `s`, and copy the content to the `s`

```python
s = '\n# some comments\nprint("s = " + s.__repr__() + s, end="")'
# some comments
print("s = " + s.__repr__() + s, end="")
```

3. Enjoy!

## How does it work?
We want to have a string `s` that we can control that will contain the source code **starting from just after the string itself to the end of the program source code**.

This way, when we print `s` in the end of the program, it will print the entire program source code. Note that **the logic pring string `s` does not depend on the content of string `s` itself**.

We also need a way to reproduce the content of string `s` in the output.
This is not easy in other programing langauges as we will need to deal with escape characters. Luckily, we have `__repr__()` builtin function python, which handles escaping for us. 

In the final print statements, we need to print 3 things sequentially.
1. Everything from the beginning of the program source code to just before the content of string `s` (`__repr__()` already include single quote, so we only need to print up to `s = `).
2. The content of string `s`.
3. `s` (consists of everything else all the way to the end).

The final problem is to produce the content of `s`. This step must be done **after the comments and all the other code has been written** because the content of `s` depends on the source code. `generate_s.py` read through the partial source code and compute the content for `s` using `__repr__`, which handles the escape characters.