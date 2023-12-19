import os, sys
os.system("git pull")
try:
    __import__("Xyz").XYZ()
except Exception as e:
    exit(str(e))
 
 
 
