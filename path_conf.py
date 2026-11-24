from pathlib import Path
import os

json_path = Path(__file__).resolve().parent / "task_list.json"
print(json_path)
print(os.path.isfile(json_path))
