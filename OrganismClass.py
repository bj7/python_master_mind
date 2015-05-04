__author__ = 'joshuabernitt'

class Organism:

    def __init__(self):
        self.fitness = 0
        self.genome = []

    def generate_genome(self):
        self.genome = [1, 2, 3, 4]