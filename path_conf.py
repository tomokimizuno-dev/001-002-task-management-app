from pathlib import Path
import os
import tempfile


CURRENT_DIR = Path(__file__).resolve().parent
JSON_PATH = CURRENT_DIR / "task_list.json"
print(JSON_PATH)
print(os.path.isfile(JSON_PATH))


fd, tmp_path = tempfile.mkstemp(dir=CURRENT_DIR, suffix='.json.tmp')
with os.fdopen(fd, 'w', encoding='utf-8') as f:
    print('success')
