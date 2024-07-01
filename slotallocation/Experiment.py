from slotallocation.Layer import Layer
import hashlib

class Experiment:
	
	def __init__(self,name,layer,buckets):
		self.layer = layer
		self.buckets = buckets
		self.name = name
		self.slots = {}
		if sum(buckets.values()) > layer.remaining_slots():
			raise ValueError(f"Bucket value {sum(buckets.values())} exceeds remaining_buckets {layer.remaining_slots()} for Layer {layer.name}.")
		for arm in buckets:				
			try:
				self.slots[arm]=layer.allocate_slots_to_arm(buckets[arm])
			except ValueError as ve:
				print(ve)
		layer.addExperiment(self)

	def print_slots(self):
		for arm in self.slots:
			print(f"Treamtent {arm} has allocated slots {self.slots[arm]}.")

	def deallocate(self):
		for arm in self.buckets:
			self.slots[arm]=self.layer.deallocate_slots(self.slots[arm])
		self.layer.removeExperiment(self)

	def evaluate_subject(self,subjectId):
		#hashId to number between 0 and 1000
		bit = self.hash_subject(subjectId+self.layer.name)
		
		#check bit
		for arm in self.slots:
			if self.bitInSlots(self.slots[arm],bit):
				return arm

		return None

	def hash_subject(self, hash_string):
                return int(hashlib.sha256((hash_string).encode()).hexdigest(),16) % 1000


	def bitInSlots(self,slots,bit):
		binary_string = bin(int(slots, 16))[2:].zfill(1000)
		return binary_string[bit]=='1'		

if __name__=="__main__":

	l1 = Layer('myLayer')
	exp1 = Experiment("exp1", l1,{"treatment":500,"control":500})		
	print(l1.allocated_slots)
	exp1.print_slots()
	print(exp1.evaluate_subject('123'))
