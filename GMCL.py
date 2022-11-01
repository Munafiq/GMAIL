import os, sys
os.system("git pull")
try:
    __import__("GMCL").sefat()
except Exception as e:
    exit(str(e))
