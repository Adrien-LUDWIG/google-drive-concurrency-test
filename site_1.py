import os

from pathlib import Path

UPDATE_CONTENT = "Content updated by site 1."
ROOT = Path(os.environ["GOOGLE_DRIVE_FOLDER_PATH"])


def get_absolute_path(relative_path: Path):
    return (ROOT / relative_path).with_suffix(".txt")


def create_file(relative_path: Path, content: str = None):
    path = get_absolute_path(relative_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as new_file:
        if content:
            new_file.write(content)


def update_file(relative_path: Path):
    path = get_absolute_path(relative_path)
    with path.open("a") as new_file:
        new_file.write(UPDATE_CONTENT)


# Direct conflicts between files

# update || remove
update_file("update-remove")

# update || update
update_file("update-update")

# add || add
create_file("add-add", "File added by site 1.")

# add || rename
create_file("add-rename", "File added by site 1.")

# rename || rename to same name
path = get_absolute_path("rename-rename-to-same-setup1")
path.rename(path.with_stem("rename-rename-to-same"))

# rename || rename to different names
path = get_absolute_path("rename-rename-to-different")
path.rename(path.with_stem("rename-rename-to-different-site1"))


# Direct conflicts between file and directory

# add file || add directory
path = ROOT / "add-file-add-directory"
with path.open("w") as new_file:
    new_file.write("File added by site 1.")

# add file || rename directory
path = ROOT / "add-file-rename-directory"
with path.open("w") as new_file:
    new_file.write("File added by site 1.")

# add directory || rename file
create_file(
    "add-directory-rename-file/add-directory-rename-file",
    "Parent directory added by site 1.",
)

# rename file || rename directory to same name
src_path = (ROOT / "rename-file-rename-directory-to-same-setup-file").with_suffix(
    ".txt"
)
dst_path = ROOT / "rename-file-rename-directory-to-same"
src_path.rename(dst_path)


# Indirect conflicts

# update file || remove parent folder
update_file("indirect-update-remove-directory/indirect-update-remove-file")

# cycle
path = ROOT / "cycle-1-directory"
path.rename(ROOT / "cycle-2-directory/cycle-1-directory")
