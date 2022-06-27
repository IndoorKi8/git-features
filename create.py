import sys
import requests
import json
import time

n = len(sys.argv)
print(f"Received {n} arguments")
changed-files = sys.argv[1]

print(changed-files)
print(type(changed-files)
