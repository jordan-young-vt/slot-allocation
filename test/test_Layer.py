import pytest
from slotallocation.Layer import Layer

class TestClass:

	def test_initialization(self):
		assert Layer('myLayer').remaining_slots()==1000

	def test_allocation(self):
		l = Layer('myLayer')
		l.allocate_slots_to_arm(100)
		assert l.remaining_slots()==900
		l.allocate_slots_to_arm(250)
		assert l.remaining_slots()==650

	def test_deallocation(self):
		l= Layer('myLayer')
		s1 = l.allocate_slots_to_arm(100)
		s2 = l.allocate_slots_to_arm(150)
		l.deallocate_slots(s2)
		assert l.remaining_slots()==900

	def test_overallocation_error(self):
		l= Layer('myLayer')
		with pytest.raises(ValueError, match="There are not enough slots remaining"):
			s1 = l.allocate_slots_to_arm(1100)		
