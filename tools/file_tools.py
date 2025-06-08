import os


def create_file(path: str, content: str):
    full_path = os.path.join("project", path) # makes the path to the project folder

    # check if the file already exists
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w") as file:
        file.write(content)

    return f"File created at {full_path}"


def read_file(path: str):
    full_path = os.path.join("project", path)

    # check if the file exists
    if not os.path.exists(full_path):
        return f"File not found at {full_path}"

    with open(full_path, "r") as file:
        return file.read()
