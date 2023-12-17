LRUCache Project
This project implements an LRU (Least Recently Used) cache data structure in Python. The LRUCache class follows the LRU eviction policy, where the least recently used items are evicted when the cache reaches its capacity. It provides methods to initialize the cache, get the value of a key, and put a key-value pair into the cache.

Example
from lrucache import LRUCache
lru_cache = LRUCache(2)
lru_cache.put(1, 1)  # cache is {1=1}
lru_cache.put(2, 2)  # cache is {1=1, 2=2}
lru_cache.get(1)     # returns 1
lru_cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lru_cache.get(2)     # returns -1 (not found)
lru_cache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lru_cache.get(1)     # returns -1 (not found)
lru_cache.get(3)     # returns 3
lru_cache.get(4)     # returns 4

Constraints
1 <= capacity <= 50
0 <= key <= 100
0 <= value <= 100

Instructions
Implement the LRUCache class by highlighting the data structures and algorithms used in the project report.
Work in groups of up to three students.
Deliver the Python project and a project report (maximum 4 pages) discussing the data structures and algorithms used.
Submit before 12th Jan 2023.
Submit the report via Google Classroom.
The student making the submission is Neha Nauman Khan (Roll Number: XYZ). Collaborators: Manahil Ejaz (Roll Number: XYZ), Ayesha Ahmed (Roll Number: XYZ).
Feel free to check out the GitHub repositories of the collaborators:

Neha Nauman Khan
Manahil Ejaz
Ayesha Ahmed
