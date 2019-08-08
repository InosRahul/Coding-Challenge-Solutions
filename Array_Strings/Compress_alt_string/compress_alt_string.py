from nose.tools import assert_equal


class Compress_alt(object):
    def compress_alt_solution(self,string):
        if None or not string:
            return string
        result = ""
        i = 1
        count = 1
        length = len(string)
        while i < length:
            if string[i] == string[i-1]:
                count += 1
            elif count == 1:
                result = result + string[i-1] + ''
                count = 1
            else:
                result = result + string[i-1] + (str(count) if count > 2 else string[i-1])
                count = 1
            i += 1
        result = result + string[i-1] + (str(count) if count >  2 else string[i-1])
        return result if len(result) < len(string) else string
class TestCompressAlt(object):
    def test_compress_alt(self,func):
        assert_equal(func(None),None)
        assert_equal(func(''), '')
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDD'), 'A3BCCD4')
        assert_equal(func('aaBCCEFFFFKKMMMMMMP taaammanlaarrrr seeeeeeeeek tooo'), 'aaBCCEF4KKM6P ta3mmanlaar4 se9k to3')
        print('Success: test_compress')
def main():
    test = TestCompressAlt()
    compress_alt = Compress_alt()
    test.test_compress_alt(compress_alt.compress_alt_solution)

if __name__ == "__main__":
    main()

