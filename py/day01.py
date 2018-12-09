#!/usr/bin/env python

from __future__ import print_function

def get_list( fn='input.01' ):
  retval = []
  with open( fn, 'r' ) as fp:
    for line in fp:
      d = int( line.strip().split()[0] )
      retval.append( d )
  return retval

if __name__ == '__main__':

  sum = 0

  q = get_list()

  s = 0
  for qq in q:
    s += qq

  print( s )

  freqs = {}
  sum = 0

  done = False

  while not done:

    for qq in q:

      sum += qq

      if sum in freqs:

	if not done: print( sum ) 
        done = True

      else:
        freqs[sum] = 1


