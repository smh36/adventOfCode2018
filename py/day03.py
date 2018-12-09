#!/usr/bin/env python

import numpy as np

def read_tiles( fn='input.03' ):
 
  maxx, maxy = 0, 0

  tiles = {}

  with open( fn, 'r' ) as fp:
    for line in fp:
      d = line.strip().split()
      claim = int( d[0][1:] )
      x, y = d[2].split(','); x = int(x); y = int(y[:-1])
      w, d = d[3].split('x'); w = int(w); d = int(d)

      tiles[claim] = [ x, y, w, d ]
      if x+w > maxx: maxx = x+w
      if y+d > maxy: maxy = y+d

  return tiles, maxx, maxy

if __name__ == '__main__':

  tiles, big_x, big_y = read_tiles()

  c = np.zeros( ( big_x, big_y ), dtype=np.int32 )

  for tile in tiles:
    x, y, w, d = tiles[tile]

    for i in range(x, x+w):
      for j in range(y, y+d):
        if c[i,j] == 0:
          c[i,j] = 1
        else:
          c[i,j] = -1

  print( np.sum( c < 0 ) )

  for tile in tiles:
    x, y, w, d = tiles[tile]

    if np.sum( c[x:x+w, y:y+d] ) == w*d:
      print( tile )

