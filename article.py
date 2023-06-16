class Article:
    """class that represents an article
    """
    def __init__(self, name, path):
        self.Name = name
        """name of article
        """
        self.Path = path
        """path where the article is
        """
        pass    

    def __eq__(self, o):
        print(self.Name)
        if self.Name == o.Name:
            return True
        return False

    def __gt__(self, o):
        if self.Name > o.Name:
            return True
        return False

    def __lt__(self, o):
        if self.Name > o.Name:
            return False
        return True

    def __hash__(self):
        return hash(self.Name)

    def __str__(self):
        return self.Name
    