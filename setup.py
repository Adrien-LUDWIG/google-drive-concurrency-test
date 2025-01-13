import os

from pathlib import Path

FILE_CONTENT = "File added by setup."
ROOT = Path(os.environ["GOOGLE_DRIVE_FOLDER_PATH"])


def create_file(relative_path: Path, content: str = None):
    if not content:
        content = FILE_CONTENT
    path = (ROOT / relative_path).with_suffix(".txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as new_file:
        new_file.write(content)


# Direct conflicts between files

# update || remove
create_file("update-remove")

# update || update
create_file("update-update")

# add || add
# Nothing to do

# add || rename
create_file("add-rename-setup", "File added by setup and renamed by site 2.")

# rename || rename to same name
create_file(
    "rename-rename-to-same-setup1", "File added by setup and renamed by site 1."
)
create_file(
    "rename-rename-to-same-setup2", "File added by setup and renamed by site 2."
)

# rename || rename to different names
create_file(
    "rename-rename-to-different",
    "File added by setup and renamed by both site 1 and 2.",
)


# Direct conflicts between file and directory

# add file || add directory
# Nothing to do

# add file || rename directory
create_file(
    "add-file-rename-directory-setup/add-file-rename-directory-setup",
    "Parent directory added by setup and renamed by site 2.",
)

# add directory || rename file
create_file(
    "add-directory-rename-file-setup", "File added by setup and renamed by site 2."
)

# rename file || rename directory to same name
create_file(
    "rename-file-rename-directory-to-same-setup-file",
    "File added by setup and renamed by site 1.",
)
create_file(
    "rename-file-rename-directory-to-same-setup-directory/rename-file-rename-directory-to-same-setup",
    "Parent directory added by setup and renamed by site 2.",
)


# Indirect conflicts

# update file || remove parent folder
create_file("indirect-update-remove-directory/indirect-update-remove-file")

# cycle
create_file("cycle-1-directory/cycle-1-file")
create_file("cycle-2-directory/cycle-2-file")
