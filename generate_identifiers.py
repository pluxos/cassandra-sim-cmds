#! /usr/bin/env python

#import random
import numpy as np
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-a', '--ammount', dest='ammount', metavar='AMMOUNT', default=8, help='Quantidade de vetores gerados')
parser.add_option('-s', '--size', dest='size', metavar='SIZE', default=8, help='Tamanho dos vetores')
parser.add_option('-m', '--min', dest='low_value', metavar='MIN_VALUE', default=-1.0, help='Valor minimo dos elementos dos vetores')
parser.add_option('-M', '--max', dest='high_value', metavar='MAX_VALUE', default=1.0, help='Valor maximo dos elementos dos vetores')

(options, args) = parser.parse_args()

ammount=int(options.ammount)
size=int(options.size)
low_value=float(options.low_value)
high_value=float(options.high_value)

class prettyfloat(float):
    def __repr__(self):
        return "%0.5f" % self

def random_vector(ammount, size, low_value, high_value):
    vector = [None] * ammount
    for i in range(ammount):
        vector = np.random.uniform(low=low_value, high=high_value, size=(size,))
        vector = map(prettyfloat, vector)
        print '    -',vector

if __name__ == "__main__":
    random_vector(ammount, size, low_value, high_value)

#x = [None] * 32;

#for i in range(32):
#    x[i] = [None] * 32;
#    for j in range(32):
#        if i == j:
#            x[i][j] = 1;
#        else:
#            x[i][j] = -1;
#    print '    -',x[i]

#for i in range(32):
#    x[i] = [None] * 32;
#    for j in range(32):
#        if i == j:
#            x[i][j] = 0.99;
#        else:
#            x[i][j] = 0.0;
#    print '    -',x[i]

#j = 0
#k = 0
#for i in range(32):
#    x = np.random.uniform(low=0.0, high=0.0, size=(8,))
#    if i == 16:
#        j = j + 7
#    x[j] = np.random.uniform(low=0.9999, high=1.0)
#    x = map(prettyfloat, x)
#    print '    -',x

#for i in range(32):
#    x = np.random.uniform(low=-1.0, high=1.0, size=(8,))
#    x = map(prettyfloat, x)
#    print '    -',x

