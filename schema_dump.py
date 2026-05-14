import json
import sys  
from schema_explorer import limit_depth, trim_keys, scan_for_keys

try:
    with open('schema.json', 'r') as f:
        schema_input = json.load(f)
    print("Successfully loaded via file open")
except Exception as e:
    print(f"File open failed: {e}")


# schema_input=json.load(sys.stdin)
trimmed_schema=trim_keys(schema_input,['version','description','description_kind'])
print(json.dumps(trimmed_schema,indent=2))
