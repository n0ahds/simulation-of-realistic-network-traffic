#
#   PROJECT : Simulation of Realistic Network Traffic
# 
#   FILENAME : main.py
# 
#   DESCRIPTION :
#       Data traffic in computer networks is often generated at random times
#       by end users. More randomness in packet transmission times is also
#       introduced by the network nodes when they send/receive data. In order 
#       to simulate realistic traffic input to computer networks, we need to 
#       generate randomized test traffic similar to what is seen in reality.
# 
#   FUNCTIONS :
#       get_formatted_time()
#       write_to_file()
#       mean()
#       variance()
#       stdev()
#       plot_histrogram()
#       main()
# 
#   NOTES :
#       - ...
# 
#   AUTHOR(S) : Noah Arcand Da Silva    START DATE : 2022.12.02 (YYYY.MM.DD)
#
#   CHANGES :
#       - ...
# 
#   VERSION     DATE        WHO             DETAILS
#   0.0.1a      2022.12.02  Noah            Creation of project.
#   0.0.1b      2022.12.03  Noah            First implementation of linear congruential method and inverse transform technique.
#   0.0.1c      2022.12.03  Noah            Added numpy exponential distribution to compare with exponential inverse transform.
#


from random_generation import RandomNumberGenerator, RandomVariateGenerator

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# Get a formatted timestamp.
def get_formatted_time():
    return datetime.now().strftime("%Y-%m-%d_%H.%M.%S.%f")[:-3]

# Save the array of random numbers into a text file for viewing.
def write_to_file(filename, data):
    with open(f"{filename}.txt", 'w') as file:
        for i in data:
            file.write(str(i) + '\n')
        file.close()

# Get the mean for the list of numbers.
def mean(data):
    return np.mean(data)

# Get the variance for the list of numbers.
def variance(data):
    return np.var(data)

# Get the standard deviation for the list of numbers.
def stdev(data):
    return np.std(data)

# Create a histogram with the data provided.
def plot_histogram(data, title, filename, nbins=30):
    plt.clf()
    plt.style.use('ggplot')
    plt.hist(data, nbins, rwidth=0.85, color='cornflowerblue')
    plt.title(title)
    plt.xlabel('Numerical Value')
    plt.ylabel('Occurence')
    # Add dataset statistics as annotation on the graph.
    annotation_text = \
        f"Mean: {round(mean(data), 5)}\n" \
        f"Variance: {round(variance(data), 5)}\n" \
        f"St.d: {round(stdev(data), 5)}"
    plt.annotate(
        annotation_text,
        xy = (max(data),0),
        horizontalalignment='right',
        verticalalignment='bottom',
    ).set_bbox(dict(facecolor='white', alpha=0.85, edgecolor='gray'))
    # Save the graph as an SVG file.
    plt.savefig(filename + '.svg')


def main():
    # Instantiate both random generator objects.
    rng = RandomNumberGenerator()
    rvg = RandomVariateGenerator()

    # Generating and graphing sample of 1,024 random numbers.
    timestamp = get_formatted_time()
    random_numbers = rng.linear_congruential(
        size=1_024,
        seed=7,
        increment=0,
        multiplier=11,
        modulus=1_024
    )
    plot_histogram(
        data=random_numbers, 
        title="Linear Congruential Random Number Generation", 
        filename=f"{timestamp}"
    )
    write_to_file(f"{timestamp}", random_numbers)

    # Generating and graphing sample of 102,400 random numbers.
    timestamp = get_formatted_time()
    random_numbers = rng.linear_congruential(
        size=102_400,
        seed=7,
        increment=0,
        multiplier=11,
        modulus=1_024
    )
    plot_histogram(
        data=random_numbers, 
        title="Linear Congruential Random Number Generation", 
        filename=f"{timestamp}"
    )
    write_to_file(f"{timestamp}", random_numbers)

    # Generating and graphing sample of 1,240 random numbers.
    timestamp = get_formatted_time()
    random_numbers = rng.linear_congruential(
        size=1_024,
        seed=7,
        increment=11,
        multiplier=25_214_903_917,
        modulus=2**48
    )
    plot_histogram(
        data=random_numbers, 
        title="Linear Congruential Random Number Generation", 
        filename=f"{timestamp}"
    )
    write_to_file(f"{timestamp}", random_numbers)

    # Generating and graphing sample of 102,400 random numbers.
    timestamp = get_formatted_time()
    random_numbers = rng.linear_congruential(
        size=102_400,
        seed=7,
        increment=11,
        multiplier=25_214_903_917,
        modulus=2**48
    )
    plot_histogram(
        data=random_numbers, 
        title="Linear Congruential Random Number Generation", 
        filename=f"{timestamp}"
    )
    write_to_file(f"{timestamp}", random_numbers)

    # Generating and graphing random variate numbers following an exponential distribution
    # derived from our random number generator following a uniform distribution.
    timestamp = get_formatted_time()
    random_variates = rvg.inverse_transform_exponential(
        LAMBDA=3,
        random_numbers=random_numbers
    )
    plot_histogram(
        data=random_variates, 
        title="Inverse Transform Rand Variates (Exponential Distribution)", 
        filename=f"{timestamp}"
    )
    write_to_file(f"{timestamp}", random_numbers)

    # Generating and graphing sample of 102,400 random numbers using the exponential
    # function provided by numpy.
    timestamp = get_formatted_time()
    np.random.seed(5)
    random_numbers = np.random.exponential(scale=1/3, size=102_400)
    plot_histogram(
        data=random_numbers, 
        title="Exponential Distribution Using Numpy's Library", 
        filename=f"{timestamp}"
    )
    write_to_file(f"{timestamp}", random_numbers)


# Runs the code.
if __name__ == '__main__':
    main()
