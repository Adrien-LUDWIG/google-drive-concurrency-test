import os

from pathlib import Path

root = Path(os.environ["GOOGLE_DRIVE_FOLDER_PATH"])


def create_file(relative_path: Path, content: str = None):
    path = (root / relative_path).with_suffix(".txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as new_file:
        if content:
            new_file.write(content)


# Direct

# update || remove
path = (root / "update-remove").with_suffix(".txt")
path.unlink()

# update || update
path = (root / "update-update").with_suffix(".txt")
with path.open("a") as file:
    file.write("Content updated by site 2.")

# add || add
create_file("add-add", "File added by site 2.")

# add || rename
path = (root / "add-rename-setup").with_suffix(".txt")
path.rename(path.with_stem("add-rename"))

# rename || rename to same name
path = (root / "rename-rename-to-same-setup2").with_suffix(".txt")
path.rename(path.with_stem("rename-rename-to-same"))

# rename || rename to different names
path = (root / "rename-rename-to-different").with_suffix(".txt")
path.rename(path.with_stem("rename-rename-to-different-site2"))
