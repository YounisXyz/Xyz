import os, sys
os.system("git pull")
try:
    __import__("YounisXyz").XYZ()
except Exception as e:
    exit(str(e))
 
 
 
