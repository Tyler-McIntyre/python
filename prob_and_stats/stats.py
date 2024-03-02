import math

def mean(data_list):
    '''
    Calculates the mean of a dataset

    Args:
        data_list: A list of numeric values

    Return:
        float: The mean of the dataset
    '''
    return sum(data_list) / len(data_list)

def variance(data_list, sample=False):
    '''
    Calculates the variance of a dataset

    Args:
        data_list: A list of values to derive the variance
        sample: A boolean indicating sample or population data
    
    Returns:
        float: The calculated variance of the dataset
    '''
    # Calculate the mean of the data.
    mean = sum(data_list) / len(data_list)

    sum_of_squared_values = 0
    for num in data_list:
        # Find each data point's difference from the mean value.
        difference = num - mean

        # Square each of these values.
        diff_squared = difference ** 2

        # Add up all of the squared values.
        sum_of_squared_values += diff_squared

    # Divide this sum of squares by n – 1 (for a sample) or N (for the population).
    if sample:
        return sum_of_squared_values / (len(data_list) - 1)
    else:
        return sum_of_squared_values / len(data_list)

def standard_deviation(variance):
    '''
    Calculates the standard deviation of the variance

    Args:
        variance: The squared deviation from the mean of a random variable

    Returns:
        float: The standard deviation which is the square root of the variance
    '''
    return math.sqrt(variance)
