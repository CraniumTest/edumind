class ContentRepository:
    def __init__(self):
        self.contents = []

    def add_content(self, content):
        self.contents.append(content)

    def get_contents(self):
        return self.contents
