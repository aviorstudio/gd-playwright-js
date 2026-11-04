#!/usr/bin/env python3
"""Verify exported functions from the actual packed library."""
import json
from pathlib import Path
import subprocess
import tarfile
import tempfile
meta=json.loads(Path('dist/package.json').read_text())
with tempfile.TemporaryDirectory() as directory:
    root=Path(directory)
    with tarfile.open(Path('dist')/meta['filename']) as archive:
        expected={'package/package.json','package/src/index.js','package/README.md','package/LICENSE','package/SOURCE.json'}
        assert {entry.name for entry in archive.getmembers()}==expected
        archive.extractall(root,filter='data')
    module=(root/'package/src/index.js').as_uri()
    code="const m=await import(process.argv[1]);for(const name of ['resolveElement','clickElement','dragElement','waitForGodotEvent']){if(typeof m[name]!=='function')throw Error(name)}"
    subprocess.run(['node','--input-type=module','-e',code,module],check=True)
print('Packed public library exports verified.')
