from nose.tools import assert_equal


class Compress(object):
    def compress_solution(self, string):
        if string is None or not string:
            return string
        r = ""
        count = 1
        i = 1
        l = len(string)
        while i < l:
            if string[i] == string[i-1]:
                count += 1
            else:
                r = r + string[i-1] + (str(count) if count > 1 else '')
                count = 1
            i += 1
        r = r + string[i-1] + (str(count) if count > 1 else '')
        return r if len(r) < len(string) else string


class TestCompress(object):

    def test_compress(self, func):
        assert_equal(func(None), None)
        assert_equal(func(''), '')
        assert_equal(func('ABC'), 'ABC')
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDDE'), 'A3BC2D4E')
        assert_equal(func('BAAACCDDDD'), 'BA3C2D4')
        assert_equal(func('AAABAACCDDDD'), 'A3BA2C2D4')
        print('Success: test_compress')


def main():
    test = TestCompress()
    compress_string = Compress()
    test.test_compress(compress_string.compress_solution)


if __name__ == '__main__':
    main()
