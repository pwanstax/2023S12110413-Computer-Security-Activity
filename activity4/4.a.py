import os


# Generate large file with random data
def generate_large_file(file_path: str, size: int):
    with open(file_path, "wb") as f:
        f.write(os.urandom(size))


# Generate large file
generate_large_file("assets/large-file", 1024 * 1024 * 1024)
