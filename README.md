# slot-allocation
A toy example of a layer slot allocator.

To use this run the cli class in the slotallocation folder as such:

python3 slotallocator/cli.py

Next, you can set up a new layer using the following command:

**createLayer <name of the layer>**

you can then create experiments in this layer with the following command:

**createExperiment <experiment name> <layer name> <arms>**

  where arms is in the format {"arm1":num_slots,"arm2":num_slots,...} with no spaces.  There are only 1000 slots available, each representing 0.1% of total traffic.  You can continue adding experiments to a layer as long as there are still available slots.

to remove an experiment from a layer:

**remove experiment <experiment name>**

This will deallocate all of that experiments slots.

You can also see the details of experiments or layers with the following commands:

**print layers**

**print experiments**

Finally, you can see how an individual subject evaluates against an experiment or all experiments in a layer with the following:

**evaluate <experiment/layer> <experiment/layer name> <subject>**

For example, if you wanted to evaluate subject 123 against experiment exp1 you would use:

evaluate experiment exp1 123

if instead you wanted to evaluate the same subject against all experiments in layer layer1 you would use:

evaluate layer layer1 123.
