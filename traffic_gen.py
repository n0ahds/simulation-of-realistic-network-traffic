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


class TrafficGen:
    def __init__(self, Xo=7, C=0, A=11, m=1_024):
        self.Xo = Xo
        self.C = C
        self.A = A
        self.m = m


    def simulation(self):
        pass