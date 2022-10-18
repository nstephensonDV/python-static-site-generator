from typing import List
from pathlib import Path
import shutil

class Parser:
    def __init__(self, extensions: List[str] = []):
        self.extensions = extensions

    def valid_extension(self, extension):
        for i in self.extensions:
            if extension == i:
                return True
        return False

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, 'rt', encoding='UTF-8') as file:
            return file.read()

    def write(self, path: Path, dest: Path, content, ext = ".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, 'rt', encoding='UTF-8') as file:
            file.write(content)

    def copy(self, path: Path, source: Path, dest: Path):
        shutil.copy2(path, dest / source)

class ResourceParser(Parser):
    def __init__(self):
        extensions = [".jpg", ".png", ".gif", ".css", ".html"]
        super().__init__(extensions)

    def parse(self, path: Path, source: Path, dest: Path):
        super().copy(path, source, dest)
        