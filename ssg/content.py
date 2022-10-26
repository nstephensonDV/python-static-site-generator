from importlib.metadata import metadata
import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimeter = r'"^(?:-|\+){3}\s*$"'
    __regex = re.compile(__delimeter, re.MULTILINE)

    def load(self, cls, string):
        _, fm, content = self.__regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data = {"content" : content}

    

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        pass

    def __len(self):
        pass

    def __repr__(self):
        pass