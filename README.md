Rudimentary spell-checker, based on words.txt and difflib.

Usage:

```python
In [1]: s = SpellChecker()

In [2]: s.find_near_matches('apples222')
Out[2]: "cutoff used: 0.5991422854295241\n['sapples', 'apple', 'happiless', 'dapple', 'capple', 'applesauce', 'scapple', 'sapless', 'pipless', 'papless']"
```

[end]
