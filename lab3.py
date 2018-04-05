class Interval(object):

    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __pos__(self):
        return self

    def __neg__(self):
        return Interval(0, 0) - self

    def __add__(self, other):
        return Interval(self.l + other.l, self.r + other.r)

    def __sub__(self, other):
        return Interval(self.l - other.r, self.r - other.l)

    def __mul__(self, other):
        mults = [
            self.l * other.l, self.l * other.r,
            self.r * other.l, self.r * other.r
        ]
        return Interval(min(mults), max(mults))

    def __truediv__(self, other):
        assert 0 not in other, "Division by interval, which contains 0, isn't supported."
        divs = [
            self.l / other.l, self.l / other.r,
            self.r / other.l, self.r / other.r
        ]
        return Interval(min(divs), max(divs))

    def __abs__(self):
        return max(abs(self.l), abs(self.r))

    def __str__(self):
        return '[{}, {}]'.format(self.l, self.r)

    def __contains__(self, x):
        return self.l <= x <= self.r

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
        "Given interval properties:\n\tmiddle = {}\n\twidth = {}"
        "\n\tradius = {}\n\tabsolute value = {}".format(
            INTERVAL.middle, INTERVAL.width, INTERVAL.radius, abs(INTERVAL)
        )
    )
    [a, b], [c, d] = A
    b1, b2 = B
    det_a = a*d - b*c
    # A -> A^(-1)
    a, b, c, d = [
        d/det_a, -b/det_a,
        -c/det_a, a/det_a
    ]
    # X = A^(-1) * B
    x = [
        a*b1 + b*b2,
        c*b1 + d*b2
    ]
    print("Given equation solution:\n\tx₁={}\n\tx₂={}".format(x[0], x[1]))


if __name__ == '__main__':
    A[0][0] = Interval(3, 4)
    main()
