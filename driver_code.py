from LRU_Cache import LRU_Cache
# Driver code to test LRU Cache class
#Test 1:
lru_cache1 = LRU_Cache(2)
lru_cache1.put(1, 1)   # cache is {1=1}
print('LRU Cache after putting 1,1 :',lru_cache1)
lru_cache1.put(2, 2)   # cache is {1=1, 2=2}
print('LRU Cache after putting 2,2 :',lru_cache1)
print('Get 1 :',lru_cache1.get(1))      # return 1
print('LRU Cache after getting 1 :',lru_cache1)
lru_cache1.put(3, 3)   # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print('LRU Cache after putting 3,3 :',lru_cache1)
print('Get 2 :',lru_cache1.get(2))      # returns -1 (not found)
print('LRU Cache after getting 2 :',lru_cache1)
lru_cache1.put(4, 4)   # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print('LRU Cache after putting 4,4 :',lru_cache1)
print('Get 1 :',lru_cache1.get(1))      # return -1 (not found)
print('Get 3 :',lru_cache1.get(3))      # return 3
print('Get 4 :',lru_cache1.get(4))      # return 4
print('LRU Cache at last :',lru_cache1)

#Test 2:
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

print(f'Total miss rate: {lru_cache2.cache_missed/100 * 100}%')
