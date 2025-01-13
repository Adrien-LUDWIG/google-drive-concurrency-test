import os
import shutil

from pathlib import Path

ROOT = Path(os.environ["GOOGLE_DRIVE_FOLDER_PATH"])


def create_file(relative_path: Path, content: str = None):
    path = (ROOT / relative_path).with_suffix(".txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as new_file:
        if content:
            new_file.write(content)


# Direct

# update || remove
path = (ROOT / "update-remove").with_suffix(".txt")
path.unlink()

# update || update
path = (ROOT / "update-update").with_suffix(".txt")
with path.open("a") as file:
    file.write("Content updated by site 2.")

# add || add
create_file("add-add", "File added by site 2.")

# add || rename
path = (ROOT / "add-rename-setup").with_suffix(".txt")
path.rename(path.with_stem("add-rename"))

# rename || rename to same name
path = (ROOT / "rename-rename-to-same-setup2").with_suffix(".txt")
path.rename(path.with_stem("rename-rename-to-same"))

# rename || rename to different names
path = (ROOT / "rename-rename-to-different").with_suffix(".txt")
path.rename(path.with_stem("rename-rename-to-different-site2"))

# Indirect conflicts

# update file || remove parent folder
path = ROOT / "indirect-update-remove-directory"
shutil.rmtree(path)

# cycle
path = ROOT / "cycle-2-directory"
path.rename(ROOT / "cycle-1-directory/cycle-2-directory")
