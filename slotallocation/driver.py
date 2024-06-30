#Driver Class for Slot Allocation

from slotallocation.Experiment import Experiment
from slotallocation.Layer import Layer


myLayer = Layer("myLayer")

exp1 = Experiment(myLayer, {"control":200,"treatment":200})
exp2 = Experiment(myLayer, {"control":200,"treatment":200})
exp2.printSlots()
exp2.deallocate()
exp3 = Experiment(myLayer, {"control":100,"treatment":100})
exp4 = Experiment(myLayer, {"control":100,"treatment":100})
exp5 = Experiment(myLayer, {"control":50,"treatment":50})


exp1.printSlots()
exp3.printSlots()


print(exp1.evaluateSubject('123'))
print(exp3.evaluateSubject('123'))
print(exp4.evaluateSubject('123'))
print(exp5.evaluateSubject('123'))
print('---')
print(exp1.evaluateSubject('1234'))
print(exp3.evaluateSubject('1234'))
print(exp4.evaluateSubject('1234'))
print(exp5.evaluateSubject('1234'))
print('---')
print(exp1.evaluateSubject('12345'))
print(exp3.evaluateSubject('12345'))
print(exp4.evaluateSubject('12345'))
print(exp5.evaluateSubject('12345'))
