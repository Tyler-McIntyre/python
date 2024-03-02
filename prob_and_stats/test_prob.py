from .prob import *

def test_binomial_pmf():
    n = 5 # Trials
    p = 0.5 # Probability of success
    k = 3 # Actual number of successes
    probability = binomial_pmf(n, p, k)
    assert probability == 0.3125

def test_poisson_pmf():
    lmbda = 2.5
    k = 3
    probability = poisson_pmf(2.5, 3)
    assert round(probability, 2) == 0.21