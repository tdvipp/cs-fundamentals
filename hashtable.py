# Hashtable for int -> int
class MyHashTable:
    def __init__(self, cap: int):
        self.cap = cap
        self.container = [[] for _ in range(self.cap)]
        self.total = 0
        
    def _hash(self, k: int):
        return (k**3 - k**2 + k)
    
    def _get_bucket(self, key: int):
        index = self._hash(key) % self.cap
        return self.container[index]
        
    def insert(self, key: int, value: int):
        # Worst Time O(N)
        bucket = self._get_bucket(key)
        
        # check exists
        for idx, (k, v) in enumerate(bucket):
            if key == k:
                bucket[idx] = (key, value)
                return
            
        bucket.append((key, value))
        
        self.total += 1
        
        if self.total > 2/3 * self.cap:
            new_cap = self.cap * 2
            new_container = [[] for _ in range(new_cap)]
            
            for bucket in self.container:
                for (k, v) in bucket:
                    index = self._hash(k) % new_cap
                    new_bucket = new_container[index]
                    k_existed = False
                    for idx, (_k, _v) in enumerate(new_bucket):
                        if k == _k:
                            k_existed = True
                            bucket[idx] = (k, v)
                            break
                            
                    if not k_existed:
                        new_bucket.append((k, v))
                        
            self.cap = new_cap
            self.container = new_container
        
    
    def get(self, key: int) -> int:
        # Worst Time O(N)
        bucket = self._get_bucket(key)
        for (k, v) in bucket:
            if key == k:
                return v
        
        # when to raise ? when to return None ?
        raise Exception("no element with this key")
    
    def remove(self, key: int):
        # Worst Time O(N)
        bucket = self._get_bucket(key)
        for (k, v) in bucket:
            if key == k:
                bucket.remove((k, v))
                return

        # when to raise ? when to return None ?
        raise Exception("no element with this key")
        
    def print_out(self):
        print('*' * 20)
        for bucket in self.container:
            print(bucket)
        # print(self.container)
        
        
if __name__ == '__main__':
    cap = 4
    hashtable = MyHashTable(cap)
    hashtable.print_out()
    hashtable.insert(10, 100)
    hashtable.print_out()
    hashtable.insert(11, 21)
    hashtable.insert(50, 1)
    hashtable.print_out()
    hashtable.insert(10, 5)
    hashtable.print_out()
    hashtable.remove(11)
    hashtable.print_out()
    print(hashtable.get(50))
