#!/usr/bin/python
def verbose(myFunction, prt_able_i, do=False):
    if do:
        print(f'{myFunction.__name__} --> {prt_able_i}')
import sys

def rock_paper_scissors(n):
  # Your code here

  for i in n:
    print(i)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')