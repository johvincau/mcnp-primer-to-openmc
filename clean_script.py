from pathlib import Path

folder = Path(".")
for ext in ("*.xml","*.h5","*.png","*.out"):
    for file in folder.rglob(ext):
        file.unlink()