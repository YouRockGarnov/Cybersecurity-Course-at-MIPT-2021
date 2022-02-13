import os
import sys

data = sys.stdin.buffer.read()

data = data.replace(b'\xd9\x45\x08\xd9', b'\x90\xd9\xeb\xd9')
data = data.replace(b'\xd8\xc1', b'\xde\xc9')

sys.stdout.buffer.write(data)
