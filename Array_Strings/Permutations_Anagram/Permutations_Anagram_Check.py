from nose.tools import assert_equal,assert_raises


class Permutation(object):
    def checkPermutation(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        if len(str1) != len(str2):
            return False
        return sorted(str1) == sorted(str2)
class PermutationAlt(object):
    def checkPermutationAlt(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        if len(str1) != len(str2):
            return False
        count = {}
        for char in str1:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in str2:
            if char in count:
                count[char] -= 1
            else:
                count[char] = 1
        for k in count:
            if count[k] != 0:
                return False
        return True
class TestPermutation(object):
    def test_Permutation(self, func):
        assert_equal(func(None, 'foo'), False)
        assert_equal(func('', 'foo'), False)
        assert_equal(func('Nib', 'bin'), False)
        assert_equal(func('act', 'cat'), True)
        assert_equal(func('a ct', 'ca t'), True)
        assert_equal(func('dog', 'doggo'), False)
        print("Success: Permutation/Anagram Test")
def main():
    test = TestPermutation()
    permutation = Permutation()
    permutation2 = PermutationAlt()
    test.test_Permutation(permutation.checkPermutation)
    test.test_Permutation(permutation2.checkPermutationAlt)
if __name__ == "__main__":
    main()