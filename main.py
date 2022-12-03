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
#


from random_number_generator import RandomNumberGenerator

from numpy import random as r
import numpy as np
import matplotlib.pyplot as plt


def histogram(data, data_label, nbins=30):
    # Create a histogram with the data provided.
    plt.clf()
    plt.style.use('ggplot')
    plt.hist(data, nbins, rwidth=0.85, color='cornflowerblue')
    plt.title(data_label)
    plt.xlabel('Linear Congruential Random Number Generation')
    plt.ylabel('Occurence')
    plt.savefig(data_label + '.svg')


def mean(data):
    # Calculate the mean for the list of numbers.
    return np.mean(data)


def variance(data):
    # Calculate the variance for the list of numbers.
    return np.var(data)


def stdev(data):
    # Calculate the standard deviation for the list of numbers.
    return np.std(data)


def main():
    rng = RandomNumberGenerator()
    random_numbers = rng.linear_congruential(
        size=102_400,
        seed=7,
        increment=0,
        multiplier=25_214_903_917,
        modulus=2**48
    )
    histogram(data=random_numbers, data_label="Random Numbers")


# Runs the code.
if __name__ == '__main__':
    main()