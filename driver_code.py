from LRU_Cache import LRU_Cache
# Driver code to test LRU Cache class
lru_cache1 = LRU_Cache(2)
lru_cache1.put(1, 1)   # cache is {1=1}
print(lru_cache1)
lru_cache1.put(2, 2)   # cache is {1=1, 2=2}
print(lru_cache1)
print(lru_cache1.get(1))      # return 1
lru_cache1.put(3, 3)   # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lru_cache1)
print(lru_cache1.get(2))      # returns -1 (not found)
lru_cache1.put(4, 4)   # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lru_cache1)
print(lru_cache1.get(1))      # return -1 (not found)
print(lru_cache1.get(3))      # return 3
print(lru_cache1.get(4))      # return 4

lru_cache2 = LRU_Cache(50)   # LRU Cache with a capacity of 50

for i in range(50):         # Filling cache with keys from 0-49
    lru_cache2.put(i, i)

print("\nLRU Cache after filling with keys from 0 to 49")
print(lru_cache2)

for i in range(1, 50, 2):   # Retrieving the odd number key-values
    lru_cache2.get(i)

print("\nLRU Cache after retrieving odd number key-values")
print(lru_cache2)

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for i in prime_numbers:     # Again filling the cache with prime number keys from 0-100
    lru_cache2.put(i,i)

print("\nLRU Cache after refilling it with prime number keys from 0 to 100")
print(lru_cache2)

total_requests = 0           # Now retrieving all key-values from LRU Cache and computing the final miss rate
cache_miss = 0
cache_hit = 0
#Retrieving values from range (0-49)
for i in range(50):
    total_requests += 1
    if lru_cache2.get(i) == -1:
        cache_miss += 1
    else:
        cache_hit += 1
#Retreiving remaining prime numbers from (50-100)
pn_50_100=[53, 59, 61, 67, 71, 73, 79, 83, 89, 97]        
for i in pn_50_100:
    total_requests += 1
    if lru_cache2.get(i) == -1:
        cache_miss += 1
    else:
        cache_hit += 1
        

miss_rate = cache_miss / total_requests
print(f"\nCache hit: {cache_hit}\nCache missed: {cache_miss}\nFinal Miss Rate: {miss_rate * 100:.2f}%")
