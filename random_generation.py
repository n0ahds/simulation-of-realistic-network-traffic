#
#   PROJECT : Simulation of Realistic Network Traffic
# 
#   FILENAME : traffic_gen.py
# 
#   DESCRIPTION :
#       Data traffic in computer networks is often generated at random times
#       by end users. More randomness in packet transmission times is also
#       introduced by the network nodes when they send/receive data. In order 
#       to simulate realistic traffic input to computer networks, we need to 
#       generate randomized test traffic similar to what is seen in reality.
# 
#   FUNCTIONS :
#       ...
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


import math


class RandomNumberGenerator:
    def __init__(self):
        self.random_variates = []
        self.random_numbers = []

    # Generate random numbers using the linear congruential method.
    def linear_congruential(self, 
                            size=10,
                            seed=7,         # X0
                            increment=0,    # c
                            multiplier=11,  # a
                            modulus=1_024): # m
        self.random_numbers = [0] * size
        for i in range(size):
            seed = ((multiplier * seed) + increment) % modulus
            self.random_numbers[i] = seed / modulus
        return self.random_numbers


class RandomVariateGenerator:
    def __init__(self):
        self.random_variates = []

    # Generate random variates using the inverse transform technique.
    def inverse_transform(self, LAMBDA=3, random_numbers=[]):
        self.random_variates = []
        for random_number in random_numbers:
            random_variate = (-1 / LAMBDA) * math.log(1 - random_number)
            self.random_variates.append(random_variate)
        return self.random_variates