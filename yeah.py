import sys
import os

cwd = os.getcwd() + "\\test"
print(cwd)
sys.path.append(cwd)
print(sys.path)

from hello import *
hello()