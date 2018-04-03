from scipy.stats import poisson


def mean(a):
    return sum(a) / len(a)


N = 10**6
T = 50

taus = [poisson.rvs(T, size=N) for _ in range(7)]
gammas = [
    min(taus[0][i], max(taus[2][i], min(taus[3][i], taus[5][i])), taus[6][i])
    for i in range(N)
]
print(
    "{} - mean value of system uptime over {} experiments "
    "with mean node uptime equal {}.".format(
        mean(gammas), N, T
    )
)
