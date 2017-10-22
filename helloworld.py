import sys
from hello import hello

if (len(sys.argv) > 0):
  name = ' '.join(sys.argv)
else:
  name = 'World'

print (hello(name))