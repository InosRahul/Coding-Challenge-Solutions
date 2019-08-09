from nose.tools import assert_equal,assert_raises


class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
    def _hash_function(self, key):
        return key % self.size
    def set(self, key, value):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
        return self.table[hash_index].append(Item(key,value))
    def get(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError('Not Found')
    def remove(self, key):
        hash_index = self._hash_function(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        raise KeyError('Not Found')
class TestHashTable(object):
    def test_hash_table(self):
        hash_table = HashTable(10)
        print("Test : get on an empty hash table index")
        assert_raises(KeyError, hash_table.get, 0)

        print("Tst: set on an empty hash table index")
        hash_table.set(0, 'foo')
        assert_equal(hash_table.get(0), 'foo')
        hash_table.set(1, 'bar')
        assert_equal(hash_table.get(1), 'bar')

        print("Test: Set on a key that already exists")
        hash_table.set(0,'foo2')
        assert_equal(hash_table.get(0), 'foo2')

        print("Test: set on a non empty hash table index")
        hash_table.set(10, 'foo3')
        assert_equal(hash_table.get(10), 'foo3')

        print("Test: remove a key that already exists")
        hash_table.remove(10)
        assert_equal(hash_table.get(0), 'foo2')
        assert_raises(KeyError, hash_table.get, 10)

        print("Test: remove a key that doesn't exist")
        assert_raises(KeyError, hash_table.remove, -1)

        print("Test Success")
def main():
    test = TestHashTable()
    test.test_hash_table()
if __name__ == "__main__":
    main()

