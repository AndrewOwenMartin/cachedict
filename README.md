# A super simple expiring dictionary in python.

This package contains the class `LRU`, a dictionary which contains only the N most recently added or accessed keys.

# Dependencies

None, imports collections from the standard library.

# Example

```python
>>> from cachedict import LRU

>>> lru = LRU(maxsize=3) # Make an LRU (least recently used) dict with a max size of 3.

>>> lru['foo'] = 1

>>> lru['bar'] = 2

>>> lru['baz'] = 3

>>> print(lru) # All three keys are present.
LRU([('foo', 1), ('bar', 2), ('baz', 3)])

>>> lru['qux'] = 4 # Adding the fourth key expires the oldest key 'foo'.

>>> lru # 'foo' has gone.
LRU([('bar', 2), ('baz', 3), ('qux', 4)])

>>> print(lru['baz']) # Accessing 'baz' refreshes its lifetime
3

>>> lru['qox'] = 5

>>> print(lru) # Adding the fifth key expires the oldest remaining key 'bar'
LRU([('qux', 4), ('baz', 3), ('qox', 5)])

>>> lru['quz'] = 6 # Adding the sixth key expires 'qux', as 'baz' was recently accessed.

>>> lru
LRU([('baz', 3), ('qox', 5), ('quz', 6)])
```
