import os, sys
os.system("git pull")
try:
    __import__("John").XYZ()
except Exception as e:
    exit(str(e))
