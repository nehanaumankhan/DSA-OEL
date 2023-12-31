class LRU_Cache:
    '''LRU_CACHE is a data structure in Python that follows the constraints of a Least Recently Used (LRU) cache'''
    def __init__(self, capacity):
        # LRU Cache class Constructor with added constraints
        if not (1 <= capacity <= 50):
            raise ValueError("📌The capacity of LRU Cache must be greater than 0 and less than 51")
        self.capacity = capacity    # Size of cache list cannot exceed the capacity
        self.cache_list = []        # Cache list keeps track of recently used key, the most recently used key is at -1 index and the least recently used key is at 0th index 
        self.dict = {}              # Keeps the key-value pairs of the items present in the cache list

    def put(self, key, value):
        '''put(self, key, value) function updates the value of the key if the key exists. Otherwise, adds the key-value pair
        to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key. Each call
        to put and get functions is counted a reference.'''
        if not (0 <= key <= 100 and 0 <= value <= 100):
            raise ValueError("📌The Key and value must be greater equal to 0 and less than equal to 100")
        
        if len(self.cache_list) != self.capacity:
            # If the cache list is not full, update the list without removing the least recently used item. The dictionary remains the same.  
            self.dict[key] = value                  # Set or update the key-value pair in the dictionary
            self.update_cache_list(key)             # Update the cache list with the most recently used key
            self.cache_list += [key]                # Append the most recently used key to the cache list
        
        else:
            # If the cache list is full, evict the least recently used item, update the dictionary and cache list with the new key-value pair.
            self.delete(self.cache_list[0])         # Evict the least recently used item from the cache list and dictionary
            self.update_cache_list(key)             # Update the cache list with the most recently used key
            self.dict[key] = value                  # Set or update the key-value pair in the dictionary
            self.cache_list += [key]                # Append the most recently used key to the cache list

    def get(self, key):                             # Get the value associated with the given key. If the key is not present, return -1.
        if not (0 <= key <= 100):
            raise ValueError("📌The Key must be greater equal to 0 and less than equal to 100")
            
        if len(self.cache_list) == 0:               #if list is empty then there is no key-value in the dictinary as well
            return -1
        
        
        else : 
            if key in self.dict:                    # If the key is in the dictionary, update the cache list and return the value associated with the key.
                self.update_cache_list(key)
                self.cache_list += [key]
                return self.dict[key]
            else:
                return -1
            
    def delete(self, key):                          # Function to delete a key from the dictionary.
        temp_dict = {}
        for i in self.dict:
            if i != key:
                temp_dict[i] = self.dict[i]
        self.dict = temp_dict
    
    def update_cache_list(self, key):              # Function to update the cache list with the most recently used key.
        if key in self.cache_list:
            i = 0                                  # Find the index of the key in the cache list and remove it.
            while self.cache_list[i] != key:
                i += 1
            self.cache_list.pop(i)
        elif len(self.cache_list) == self.capacity and key not in self.cache_list:
            self.cache_list.pop(0)                 # If the cache list is full and the key is not in the cache list, remove the least recently used item.
            
    
    def __str__(self):
    cache = '{'
    for i in range(len(self.cache_list)):
        key = self.cache_list[i]
        value = self.dict.get(key, 'Key not found')
        if i == len(self.cache_list) - 1:
            cache += f"{key} = {value}}}"
        else:
            cache += f"{key} = {value}, "
    return cache
