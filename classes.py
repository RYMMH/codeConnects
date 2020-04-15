class Virus:
	def __init__(self, name, infection_rate):
		self.name = name
		self.infection_rate = infection_rate
		self.infected = 0 # this is another type that can be updated later

	def infect(self):
		self.infected = self.infected + 1

corona = Virus("corona", .5)
print(corona.name)
corona.infect()
print(corona.infected)
