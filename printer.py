
class Printer:
	def __init__(self, name):
		print("Initializing Printer")
		self.name = name

	def printt(self):
		print("Hi {name}!".format(self.name))


