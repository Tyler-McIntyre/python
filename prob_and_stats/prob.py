import math

def binomial_pmf(n, p, k):
    '''
    Calculates the binomial distribution probability mass function

    Args:
        n: The number of trials
        p: Probability of success in each trial
        k: Number of successes
    
    Returns:
        float: Probability Mass Function value for the given params
    '''
    binomial_coefficient = math.comb(n, k)
    probability = binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))
    return probability

def poisson_pmf(lmbda, k):
    '''
    Calculates the Poisson Distribution Probability Mass Function (PMF)

    Args:
        lmbda: Average rate of occurance
        k: Number of events
    
    Returns:
        Probability mass function value for the given parameters
    '''
    numerator = math.exp(-lmbda) * (lmbda ** k)
    denominator = math.factorial(k)
    probability = numerator / denominator
    return probability
