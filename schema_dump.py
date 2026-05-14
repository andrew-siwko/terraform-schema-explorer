import json
import sys  
from schema_explorer import limit_depth, trim_keys, scan_for_keys
schema_input=json.load(sys.stdin)
trimmed_schema=trim_keys(schema_input,['version','description','description_kind'])
print(json.dumps(trimmed_schema,indent=2))
