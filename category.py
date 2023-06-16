from article import Article
from queue import Queue
class Category:
    """class that represents a category"""
    
    def __init__(self, name):
        self.Name = name
        """name of category
        """
        self.MotherCategories = []
        """list of categories which self is subcategory
        """
        self.DaugtherCategories = []
        """list of self subcategories 
        """
        self.Articles = []
        """list of self articles
        """

    def __eq__(self, o):
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

    def getArticles(self):
        """Gets asociated articles to given category"""
        for article in self.Articles:
            yield article

    def getAllArticles(self):
        """Gets asociated articles to given category and its subcategories"""
        queue = Queue()
        queue.put(self)
        visited = set()
        visited.add(self)
        while not queue.empty():
            u = queue.get()
            for i in range(len(u.DaugtherCategories)):
                if u.DaugtherCategories[i] not in visited:
                    queue.put(u.DaugtherCategories[i])    
                    visited.add(u.DaugtherCategories[i])        
            yield u.getArticles()
        pass

    def getSubcategories(self):
        """Gets asociated subcategories"""
        queue = Queue()
        queue.put(self)
        visited = set()
        visited.add(self)
        while not queue.empty():
            u = queue.get()
            for i in range(0,len(u.DaugtherCategories)):
                if u.DaugtherCategories[i] not in visited:
                    queue.put(u.DaugtherCategories[i])    
                    visited.add(u.DaugtherCategories[i])        
                    pass
            yield u     
        pass

