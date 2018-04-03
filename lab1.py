from math import sqrt, log2, floor
from random import expovariate, normalvariate
from statistics import mean, variance, stdev

from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import chi2


N = 22547
LAMBDA = 0.05
MU = 10
SIGMA = 2.5
# 1
populations = {
    'exponential': [expovariate(LAMBDA) for _ in range(N)],
    'normal': [normalvariate(MU, SIGMA) for _ in range(N)]
}
# 2
means = {k: mean(v) for k, v in populations.items()}
print("Means: {exponential}(exponential), {normal}(normal)".format_map(means))
variances = {k: variance(v) for k, v in populations.items()}
print("Unbiased variances: {exponential}(exponential), {normal}(normal)".format_map(variances))
stdevs = {k: stdev(v) for k, v in populations.items()}
print("Unbiased standard deviations: {exponential}(exponential), {normal}(normal)".format_map(stdevs))
# 3
gamma = 0.95
alpha = 1 - gamma
mu_delta = np.percentile(populations['normal'], 1-alpha/2) * SIGMA / sqrt(N)
mu_estimate = [MU - mu_delta, MU + mu_delta]
print("According to interval estimations of normal distribution: {} < mₓ < {}".format(*mu_estimate))
sigma_estimate = [
    (N - 1) * variances['normal'] / chi2.ppf(1-alpha/2, N-1),
    (N - 1) * variances['normal'] / chi2.ppf(alpha/2, N-1)
]
print("According to interval estimations of normal distribution: {} < σₓ² < {}".format(*sigma_estimate))
# 4
r = 1 + floor(log2(N))
xmax = {k: max(v) for k, v in populations.items()}
xmin = {k: min(v) for k, v in populations.items()}
h = {k: (xmax[k] - xmin[k]) / r for k in populations}
xl = {k: [] for k in populations}
xr = {k: [] for k in populations}
freq = {k: [] for k in populations}
rel_freq = {k: [] for k in populations}
acc_rel_freq = {k: [] for k in populations}
for k in populations:
    print(
        """
    Interval series of {} distribution
 ______________________________________________________
| № |     Xₗ    |     Xᵣ    |  ν  |    ω    |    Σω    |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
        """.format(k), end=''
    )
    for i in range(r):
        xl[k].append(xmin[k] - h[k]/2 + i*h[k])
        xr[k].append(xl[k][i] + h[k])
        freq[k].append(0)
        for x in populations[k]:
            freq[k][i] += xl[k][i] <= x < xr[k][i]
        rel_freq[k].append(freq[k][i]/N)
        acc_rel_freq[k].append(rel_freq[k][i] + (acc_rel_freq[k][i-1] if i > 0 else 0))
        print(
            """
|{:>3}|{:>11.4f}|{:>11.4f}|{:>5}|{:>9.6f}|{:>10.6f}|
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
            """.format(
                i+1, xl[k][i], xr[k][i], freq[k][i], rel_freq[k][i], acc_rel_freq[k][i]
            ), end=''
        )
# 5
for k in populations:
    # plt.gcf().canvas.set_window_title('New window title')
    plt.hist(
        populations[k], bins=xl[k]+xr[k][-1:],
        density=False, cumulative=False
    )
    plt.title("Density of {} distribution".format(k))
    plt.show()
