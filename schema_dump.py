import json
import sys  

print(json.dumps(json.load(sys.stdin),indent=2))
