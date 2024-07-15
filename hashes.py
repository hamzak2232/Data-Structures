class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def delete(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

    def search(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

# Example usage:
hash_table = HashTable(10)
hash_table.insert("messi", 10)
hash_table.insert("ronaldo", 20)
hash_table.insert("neymar", 30)
hash_table.insert("mbappe", 40)
hash_table.display()

print("Search for 'ronaldo':", hash_table.search("ronaldo"))
print("Search for 'haaland':", hash_table.search("haaland"))

hash_table.delete("ronaldo")
hash_table.display()
print("Search for 'ronaldo':", hash_table.search("ronaldo"))
