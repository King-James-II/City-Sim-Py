# Program: City Simulator
# Description: This Python program simulates a city management game where the player manages various aspects of a city such as population growth, economy, and infrastructure.

import random

# Define the City class to represent the city and manage its properties
class City:
    def __init__(self, name, population, economy, infrastructure):
        self.name = name
        self.population = population
        self.economy = economy
        self.infrastructure = infrastructure

    def grow_population(self):
        growth_rate = random.uniform(0.01, 0.05)
        growth_amount = int(self.population * growth_rate)
        self.population += growth_amount
        print(f"The population of {self.name} has grown by {growth_amount}.")

    def improve_economy(self):
        improvement_rate = random.uniform(0.01, 0.03)
        improvement_amount = int(self.economy * improvement_rate)
        self.economy += improvement_amount
        print(f"The economy of {self.name} has improved by {improvement_amount}.")

    def develop_infrastructure(self):
        development_rate = random.uniform(0.01, 0.02)
        development_amount = int(self.infrastructure * development_rate)
        self.infrastructure += development_amount
        print(f"The infrastructure of {self.name} has developed by {development_amount}.")

    def display_status(self):
        print(f"City: {self.name}")
        print(f"Population: {self.population}")
        print(f"Economy: {self.economy}")
        print(f"Infrastructure: {self.infrastructure}")

# Define the Game class to manage the city simulation
class Game:
    def __init__(self):
        self.city = None

    def create_city(self, name, population, economy, infrastructure):
        self.city = City(name, population, economy, infrastructure)

    def simulate_year(self):
        print("Simulating one year...")
        self.city.grow_population()
        self.city.improve_economy()
        self.city.develop_infrastructure()

# Main program
if __name__ == "__main__":
    print("Welcome to City Simulator!")
    game = Game()
    city_name = input("Enter the name of your city: ")
    population = int(input("Enter the initial population of the city: "))
    economy = int(input("Enter the initial economy of the city: "))
    infrastructure = int(input("Enter the initial infrastructure of the city: "))
    game.create_city(city_name, population, economy, infrastructure)

    # Simulate multiple years
    num_years = int(input("Enter the number of years to simulate: "))
    for year in range(1, num_years + 1):
        print(f"\nYear {year}:")
        game.simulate_year()
        game.city.display_status()
