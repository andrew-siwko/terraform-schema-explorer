import json
import sys  
from schema_explorer import limit_depth, trim_keys, scan_for_keys
print(json.dumps(trim_keys(json.load(sys.stdin),['version','description','description_kind']),indent=2))
