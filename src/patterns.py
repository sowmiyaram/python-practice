import sys

class Patterns(object):
    def __init__(self):
        pass

    def pattern1(self, n, c='*', end=' '):
        """
        Given an integer n, implement a function that prints a right triangle
        consisting of that many rows. For example, given an input of 4, print
        *
        * *
        * * *
        * * * *
        """
        for x in range(n+1):
            for _ in range(x):
                print(c, end = end)
            print()

    def pattern2(self, n, c='*', end=' '):
        """
        Given an integer n, implement a function that prints an inverted
        triangle consisting of that many rows. For example, given an input
        of 4, print
        * * * *
        * * *
        * *
        *
        """
        for i in range(n, 0, -1):
            for _ in range(i):
                print(c, end = end)
            print()

    def pattern3(self, n, c='*', end=' '):
        """
        Combining the two patterns above, print two triangles. For example,
        given an input of 3, print
        *
        * *
        * * *
        * *
        *
        """
        self.pattern1(n, c, end)
        self.pattern2(n-1, c, end)

    def pattern4(self, n):
        """
        Similar to the above. Print a full diamond, with the longest row
        having '2*n-1' stars. for example, given an input of 3, print
            *
          * * *
        * * * * *
          * * *
            *
        """
        result = []
        for i in range(1, n+1):
            row = ' ' * abs(n-i) + c * (2*i - 1)
            result.append(row)
        result += list(reversed(result[:-1]))
        print('\n'.join(result))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Not enough arguments.")
        print("Usage: patterns.py <num>\n to execute pattern no. <num> (1-3)")
        sys.exit(1)
    else:
        p = Patterns()
        num = sys.argv[1]
        fun = "pattern" + num
        try:
            print(fun, 3)
            getattr(p, fun)(3)
        except Exception as e:
            print(str(e))
        try:
            print(fun, 6)
            getattr(p, fun)(6)
        except Exception as e:
            print(str(e))
        try:
            print(fun, 9)
            getattr(p, fun)(9)
        except Exception as e:
            print(str(e))
