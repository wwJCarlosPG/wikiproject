from category import Category
from queue import Queue
from article import Article
from processTxt import binarySearch
import pickle


def getSubcategories(categoryName):
    """
    Args:
        categoryName (string): name of category to search

    Returns:
        generator of cateogories: the subcategories of the given category
    """
    with open("Categories.pkl",'rb') as file:
        categories = pickle.load(file)
    category = category(categoryName)
    index = binarySearch(categories, category)
    if index >= 0:
        return categories[index].getSubcategories() 
    else: Exception("this category doesn't exist")
    pass

def getAllArticles(categoryName):
    """
    Args:
        categoryName (string): name of category to search

    Returns:
        generator of generator of articles: all articles of the given category and its subcategories
    """
    with open("Categories.pkl",'rb') as file:
        categories = pickle.load(file)
    category = category(categoryName)
    index = binarySearch(categories, category)
    if index>=0:
        return categories[index].getAllArticles()
    else: Exception("this category doesn't exist")
    pass

def getArticles(categoryName):
    """
    Args:
        categoryName (string): name of category to search
    Returns:
        generator of articles 
    """
    with open("Categories.pkl",'rb') as file:
        categories = pickle.load(file)
    category = category(categoryName)
    index = binarySearch(categories, category)
    if index>=0:
        return categories[index].getArticles()
    else: Exception("this category doesn't exist")
    pass

def contains(categoryName):
    """

    Args:
        categoryName (string): name of the catrgory to search
    Returns:
        bool: true if the category is in the set
    """
    with open("categories.pkl", 'rb') as file:
        categories = pickle.load(file)
    category = category(categoryName)
    index = binarySearch(cateogries, category)
    if index>=0:
        return True
    else: return False

