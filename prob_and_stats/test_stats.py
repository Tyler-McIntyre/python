from .stats import *

test_dataset = [10, 1, 25, 19, 40]

def test_mean():
    result = mean(test_dataset)
    assert result == 19.0

def test_variance_population_data():
    population_variance = variance(test_dataset, sample=True)
    assert  population_variance == 220.5

def test_variance_sampe_data():
    sample_variance = variance(test_dataset)
    assert  sample_variance == 176.4

def test_standard_deviation():
    population_variance = variance(test_dataset)
    stdev = standard_deviation(population_variance)
    assert round(stdev, 2) == 13.28