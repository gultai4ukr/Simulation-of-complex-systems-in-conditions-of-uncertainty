class Interval(object):

    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __add__(self, other):
        return Interval(self.l + other.l, self.r + other.r)

    def __sub__(self, other):
        return Interval(self.l - other.l, self.r - other.r)

    def __mul__(self, other):
        return Interval(self.l * other.l, self.r * other.r)

    def __truediv__(self, other):
        return Interval(self.l / other.l, self.r / other.r)

    def __abs__(self):
        return max(abs(self.l), abs(self.r))

    @property
    def middle(self):
        return (self.l + self.r) / 2

    @property
    def width(self):
        return self.r - self.l

    @property
    def radius(self):
        return self.width / 2


INTERVAL = Interval(-18.7, 51.11)
A = [
    [Interval(1, 2), Interval(-1, 2)],
    [Interval(-1, 1), Interval(1, 3)]
]
B = [Interval(-1, 1), Interval(1, 2)]


def main():
    print(
        """\
Given interval properties:
    middle = {}
    width = {}
    radius = {}
    absolute value = {}\
        """.format(INTERVAL.middle, INTERVAL.width, INTERVAL.radius, abs(INTERVAL))
    )
    [a, b], [c, d] = A
    b1, b2 = B


if __name__ == '__main__':
    main()
