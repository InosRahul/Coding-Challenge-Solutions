from nose.tools import assert_equal


class UniqueSet(object):
    def unique_set(self, string):
        if string is None:
            return False
        return len(set(string)) == len(string)
class UniqueHashMap(object):
    def unique_hash(self, string):
        if string is None:
            return False
        chars = set()
        for letter in string:
            if letter in chars:
                return False
            else:
                chars.add(letter)
        return True
class UniqueInPlace(object):
    def unique_inplace(self, string):
        if string is None:
            return False
        for letter in string:
            if string.count(letter) > 1:
                return False
        return True
class TestUniqueAll(object):
    def test_unique_chars(self, func):
        assert_equal(func(None), False)
        assert_equal(func(''), True)
        assert_equal(func('foo'), False)
        assert_equal(func('bar'), True)
        print('Success: test_unique_chars')
def main():
    test = TestUniqueAll()
    uni = UniqueSet()
    uni1 = UniqueHashMap()
    uni2 = UniqueInPlace()
    test.test_unique_chars(uni.unique_set)
    test.test_unique_chars(uni1.unique_hash)
    test.test_unique_chars(uni2.unique_inplace)
if __name__ == "__main__":
    main()