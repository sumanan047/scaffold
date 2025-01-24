import os

class ContexDirectory:
    def __init__(self, path):
        self.path = path
        self.original = os.getcwd()

    def __enter__(self):
        os.chdir(self.path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original)
        return False