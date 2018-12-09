#!/usr/bin/env python

def read_labels( fn='input.02' ):
  assets = []
  with open( fn, 'r' ) as fp:
    for line in fp:
      asset_id = line.strip().split()[0]
      assets.append( asset_id )
  return assets

def n_error( p, q ):
  errs = 0
  for a, b in zip( p, q ):
    if a != b:
      errs += 1
    if errs >= 2:
      return False
  return True

if __name__ == '__main__':

  labs = read_labels()

  twos, threes = 0, 0

  for lab in labs:
    chars = {}
    for a in lab:
      if a in chars:
        chars[a] += 1
      else:
        chars[a] = 1
    if 2 in chars.values(): twos +=1
    if 3 in chars.values(): threes += 1

  print( twos * threes )

  n_labs = len( labs )

  s = ''

  for i in range(n_labs):
    for j in range(i+1, n_labs):
      if n_error( labs[i], labs[j] ):

        for a, b in zip( labs[i], labs[j] ):
          if a==b: s+=a

  print( s )



