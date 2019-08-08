from nose.tools import assert_equal,assert_raises

class FizzBuzzSol(object):
    def FizzBuzz(self,num):
        if num is None:
            raise TypeError("Can't be None")
        if num < 1:
            raise ValueError("Can't be less than 1")
        result = []
        for i in range(1,num+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

class TestFizzBuzz(object):
    def test_fizz_buzz(self):
        solution = FizzBuzzSol()
        assert_raises(TypeError, solution.FizzBuzz, None)
        assert_raises(ValueError,solution.FizzBuzz, 0)
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        assert_equal(solution.FizzBuzz(15), expected)
        print('Success: test_fizz_buzz')
def main():
    test = TestFizzBuzz()
    test.test_fizz_buzz()
if __name__ == "__main__":
    main()