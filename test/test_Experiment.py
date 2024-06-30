import pytest
from slotallocation.Experiment import Experiment
from slotallocation.Layer import Layer


class TestClass:

	def test_name(self):
		exp = Experiment('exp',Layer('l'),{"control":100,"treatment":100})
		assert exp.name=='exp'

	def test_layer(self):
		exp = Experiment('exp',Layer('l'),{"control":100,"treatment":100})
		assert exp.layer.name=='l'

	def test_slots(self):
		exp = Experiment('exp',Layer('l'),{"control":100,"treatment":100})
		assert exp.layer.remaining_slots()==800

	def test_deallocation(self):
		exp = Experiment('exp',Layer('l'),{"control":100,"treatment":100})
		exp.deallocate()
		assert exp.layer.remaining_slots()==1000

	def test_bitInSlots(self):
		slots='1'+'0'*249
		exp = Experiment('exp',Layer('l'),{"control":100,"treatment":100})
		assert exp.bitInSlots(slots,3)==True
		assert exp.bitInSlots(slots,4)==False

	def test_hash(self):
		exp = Experiment('exp',Layer('l'),{"control":100,"treatment":100})
		assert exp.hash_subject('al')==46

	def test_overallocation(self):
		with pytest.raises(ValueError, match="Bucket value 1200 exceeds remaining_buckets 1000 for Layer l."):
			Experiment('exp',Layer('l'),{"control":600,"treatment":600})
