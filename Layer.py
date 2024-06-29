import random

class Layer:

	def __init__(self,name):
		self.num_slots = 1000
		self.allocated_slots = '0'*250
		self.name=name
		self.experiments = []

	def remaining_slots(self):
		bin_slots = bin(int(self.allocated_slots, 16))[2:].zfill(1000)
		return bin_slots.count('0')
		

	def allocate_slots_to_arm(self,arm_slots):

		#Set up string of 0s#
		zeros = list('0'*1000)

		# Convert hexadecimal string to binary string
		binary_string = bin(int(self.allocated_slots, 16))[2:].zfill(1000)
    
		# Find indices of '0' bits
		changeable_indices = [i for i, bit in enumerate(binary_string) if bit == '0']
    
		# Choose `num_bits` random indices from zero_indices to flip
		indices_to_flip = random.sample(changeable_indices, min(arm_slots, len(changeable_indices)))
    
		# Flip the selected bits
		flipped_binary_list = list(binary_string)
 
		for idx in indices_to_flip:
			flipped_binary_list[idx] = '1'
			zeros[idx] = '1'    

		flipped_binary_string = ''.join(flipped_binary_list)
    
		# Convert back to hexadecimal
		flipped_hex_string = hex(int(flipped_binary_string, 2))[2:].zfill(250)
    
		self.allocated_slots = flipped_hex_string.upper()

		return hex(int(''.join(zeros),2))[2:].zfill(250).upper()

	def deallocate_slots(self, slots):
		#Convert Existing slot string to binary
		binary_allocation = bin(int(self.allocated_slots, 16))[2:].zfill(1000)

		#Convert other slots string to binary	
		binary_slots = bin(int(slots, 16))[2:].zfill(1000)

		#subtract
		sub_string = bin(int(binary_allocation,2) - int(binary_slots,2))[2:]

		#convert and return
		self.allocated_slots=hex(int(sub_string,2))[2:].zfill(250).upper()

	def addExperiment(self, e):
		self.experiments.append(e)

	def removeExperiment(self, e):
		self.experiments.remove(e)

	def print_slots(self):
		print(self.allocated_slots)

	def print_details(self):
		print(f"This layer has {self.remaining_slots()} out of {self.num_slots} slots remaining for use")
		print("Those slots are allocated to the following Experiments:")
		for e in self.experiments:
			print(f"Experiment {e.name} is taking up {sum(e.buckets.values())} slots")
		print(f"The current allocation string for slots is {self.allocated_slots}")

if __name__=="__main__":
	l = Layer('myLayer')
	print(l.remaining_slots())
	l.print_slots()
	l.allocate_slots_to_arm(100)
	print(l.remaining_slots())
	l.print_slots()
	l.allocate_slots_to_arm(50)
	print(l.remaining_slots())
	l.print_details()
