__author__ = 'joshuabernitt'

import OrganismClass as Organism


def main():
    test = Organism.Organism()

    print test.fitness

    test.fitness = 3
    print test.fitness
    test.generate_genome()
    print test.genome



main()