import sys

if (len(sys.argv) > 0):
  name = ' '.join(sys.argv)
else:
  name = 'World'

print (f'Hello {name}')