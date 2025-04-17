import os.path
import sys
import sqlite3


size = int(sys.argv[2])
out = sys.argv[1]

if os.path.exists(out):
    print(f"Error: There is already a file system at {out}.")
    return

db = sqlite3.connect(f"{out}/metadata.db")
