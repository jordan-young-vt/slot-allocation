import ast
from slotallocation.Layer import Layer
from slotallocation.Experiment import Experiment

class CLIDriver:
	def __init__(self):
		self.layers = {}
		self.experiments = {}

	def execute_command(self, command):
		try:
			if command.startswith("createExperiment"):
				_, name, layer, buckets = command.split()
				self.experiments[name]=Experiment(name, self.layers[layer],ast.literal_eval(buckets))
			if command.startswith("createLayer"):
				_, name = command.split()
				self.layers[name]=Layer(name)
			if command.startswith("remove"):
				_, type, name = command.split()
				if type=="experiment":
					self.experiments[name].deallocate()
					del self.experiments[name]
			if command.startswith("evaluate"):
				_, type, name, subject = command.split()
				if type=="experiment":
					print(f"Subject {subject} evaluates to arm {self.experiments[name].evaluate_subject(subject)} for experiment {name}")
				if type=="layer":
					print(f"Evaluating all experiments in layer {name}")
					for e in self.layers[name].experiments:
						print(f"Subject {subject} evaluates to arm {e.evaluate_subject(subject)} for experiment {e.name}")
			if command.startswith("print"):
				_, type = command.split()
				if type=="experiments":
					for e in self.experiments:
						print(e)
						self.experiments[e].print_slots()		
				if type=="layers":
					for l in self.layers:
						print(l)
						self.layers[l].print_details()
		except ValueError as e:
			print(f"Error: {e}")
		except SyntaxError as e:
			print(f"Error: {e}")
			

	def run_cli(self):
		while True:
			command = input("Enter command: ")
			if command == "exit":
				break
			self.execute_command(command)

if __name__ == "__main__":
	my_cli = CLIDriver()
	my_cli.run_cli()
