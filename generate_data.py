#! /usr/bin/env python

import numpy as np

from optparse import OptionParser

parser = OptionParser()
parser.add_option('-a', '--ammount', dest='ammount', metavar='AMMOUNT', default=10, help='Quantidade de vetores gerados')
parser.add_option('-s', '--size', dest='size', metavar='SIZE', default=8, help='Tamanho dos vetores')

(options, args) = parser.parse_args()

ammount = int(options.ammount)
size = int(options.size)
filename = str(ammount) + '_data'

f = open(filename, 'w')

for i in xrange(ammount):
    x = np.random.uniform(low=-100.00, high=100.00, size=(size,))
#    x[0] = np.random.uniform(low=0.99999, high=1.0)
    f.write(str(i) + ' ')
    f.write(' '.join(str(j) for j in x) + '\n')
