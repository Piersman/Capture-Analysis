import glob
import h5py
import numpy

for f in glob.glob("compare/*.h5"):
    count = 0
    good_enough = 0
    d = h5py.File(f, 'r')
    a_group_key = list(d.keys())[0]
    n0 = numpy.array(d[a_group_key])
    stack = numpy.zeros((263, 16, 4104))
    for dim in range(stack.shape[0]):
        stack[dim] = n0[:, (dim * 16):(dim * 16) + 16, 0:4104]
        d = 0
    for i in range(len(stack)):
        if numpy.mean(stack[i]) == 909.7777777777778 and numpy.mean(stack[i, :, 0]) == 0 and numpy.mean(stack[i, :, 1]) == 2047:
            count = count + 1
        elif numpy.mean(stack[i]) == 0:
            d = d + 1
    print(f + ": " + str(count) + " / 255 perfect data channels")
