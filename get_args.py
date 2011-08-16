#!/usr/bin/python

import sys

def get_args(oper='EXACTLY', num=1):

    comps = {'EXACTLY': '!=', 'AT_LEAST': '<'}
    if oper not in comps:
        print('Bad comparison keyword -> {0}'.format(oper))
        return
    if eval('len(sys.argv) {0} num + 1'.format(comps[oper])):
        print('Bad number of args ->', sys.argv[1:])
        return
    return sys.argv[1:]  # Returns [] when len(sys.argv) < 2
