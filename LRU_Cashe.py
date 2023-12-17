class LRU_Cache:                    # Class Least Recently Used Cache
    def __init__(self, capacity):   # LRU Cache class Constructor
        self.capacity = capacity    # Size of cache list cannot exceed the capacity
        self.cache_list = []        # Cache list keeps track of recently used key, the most recently used key is at -1 index and the least recently used key is at 0th index 
        self.dict = {}              # Keeps the key value pairs of the items present in cache list

    def put(self, key, value):
        '''put(self, key, value) function updates the value of the key if the key exists. Otherwise, adds the key-value pair
        to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key. Each call
        to put and get functions is counted a reference.'''
        
        if len(self.cache_list) != self.capacity:   # If cache list is not full  
            self.dict[key] = value                  # setting/updating value in dictionary 
            self.update_cache_list(key)
            self.cache_list += [key]
        
        else:
            self.delete(self.cache_list[0])
            self.update_cache_list(key)
            self.dict[key] = value
            self.cache_list+=[key]   

    def get(self, key):
        if len(self.cache_list) == 0:
            return -1
        elif len(self.cache_list) != self.capacity:
            if key in self.dict:
                self.update_cache_list(key)
                self.cache_list += [key]
                return self.dict[key]
            else:
                return -1
        else:
            if key in self.dict:
                self.update_cache_list(key)
                self.cache_list += [key]
                return self.dict[key]
            else:
                return -1
            
    def delete(self,key):
        temp_dict = {}
        for i in self.dict:
            if i != key:
                temp_dict[i]= self.dict[i]
        self.dict = temp_dict
    
    def update_cache_list(self,key):
        if key in self.cache_list:
            i = 0
            while self.cache_list[i] != key:i += 1
            self.cache_list.pop(i)
        elif len(self.cache_list) == self.capacity and key not in self.cache_list:
            self.cache_list.pop(0)

L = LRU_Cache(4)
