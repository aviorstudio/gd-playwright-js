#!/usr/bin/env python3
"""Build the public npm tarball from the reviewed source package."""
import json
from pathlib import Path
import subprocess
Path('dist').mkdir(exist_ok=True)
packed=json.loads(subprocess.check_output(['npm','pack','--json','--pack-destination','dist','--ignore-scripts'],text=True))
assert len(packed)==1, packed
result=packed[0] if isinstance(packed,list) else next(iter(packed.values()))
Path('dist/package.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['filename'])
