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


# Direct conflicts between files

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


# Direct conflicts between file and directory

# add file || add directory
create_file(
    "add-file-add-directory/add-file-add-directory",
    "Parent folder added by site 2.",
)

# add file || rename directory
src_path = ROOT / "add-file-rename-directory-setup"
dst_path = ROOT / "add-file-rename-directory"
src_path.rename(dst_path)

# add directory || rename file
src_path = (ROOT / "add-directory-rename-file-setup").with_suffix(".txt")
dst_path = ROOT / "add-directory-rename-file"
src_path.rename(dst_path)

# rename file || rename directory to same name
src_path = ROOT / "rename-file-rename-directory-to-same-setup-directory"
dst_path = ROOT / "rename-file-rename-directory-to-same"
src_path.rename(dst_path)


# Direct conflicts between directories

# add || add directories
create_file(
    "add-add-directories/add-add-directories-site-2",
    "Parent directory added by site 2.",
)

# add || rename directories
src_path = ROOT / "add-rename-directories-setup"
dst_path = ROOT / "add-rename-directories"
src_path.rename(dst_path)

# rename || rename directories to same name
src_path = ROOT / "rename-rename-directories-to-same-setup-2"
dst_path = ROOT / "rename-rename-directories-to-same"
src_path.rename(dst_path)

# rename || rename directories to different names
src_path = ROOT / "rename-rename-directories-to-different"
dst_path = ROOT / "rename-rename-directories-to-different-site-2"
src_path.rename(dst_path)


# Indirect conflicts

# update file || remove parent folder
path = ROOT / "indirect-update-remove-directory"
shutil.rmtree(path)

# cycle
path = ROOT / "cycle-2-directory"
path.rename(ROOT / "cycle-1-directory/cycle-2-directory")
