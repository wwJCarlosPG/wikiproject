import functools
import os
from unidecode import unidecode
import pickle
from category import Category
from article import Article

Categories = []
"""Represents the list of categories"""
#autodocstring
def processTxt(path, isCategory, saveOrNot):
    """process the TXTs to get Categories and stores it to at .pkl file

    Args:
        path (string): path where the folder is
        isCategory (bool): if the decoding is for categories or articles
        saveOrNot (bool): indicates if an article whose category isn't will be saved or not
    """

    global Categories
    with open('categories.pkl','rb') as file:
        x = file.read()
        if not(file.read() == b''):   
            Categories = pickle.load(file)
        else: Categories = []
    if os.path.exists(path):
        txts = os.listdir(path)
        for i in range(len(txts)):
            completedPath = os.path.join(path,txts[i])
            text = open(completedPath,'r', encoding="utf-8")
            text = text.read()
            text = unidecode(text) #remove the tildes
            if isCategory:
                print(txts[i])
                decodeCategory(text)
            else:
                print(txts[i]) 
                decodeArticle(text)
        with open('categories.pkl', 'wb') as file: #esto no va dentro del for
                pickle.dump(Categories, file)
    else: 
        Exception("The path doesn't exist") 

    pass


def binarySearch(list, item):
    left = 0
    right = len(list) - 1
    while left<=right:
        middle = int((left + right)/2)
        if list[middle] == item:
            return middle
        elif list[middle] < item:
            left = middle + 1
        else: 
            right = middle - 1
    return -1
    pass

def insertion(list, item):
    for i in range(0, len(list)):
        if item < list[i]:
            list.insert(i, item)
            return (list, i)
    list.append(item)
    return (list, len(list)-1)


def binaryInsertion(list, item):
    """simulates insertion in Binary Search Tree

    Args:
        list (list): list where the insertion will be
        item (comparable): item to insert

    Returns:
        (list, int): returns the list after insertion and the index where insertion was
    """
    if list == []:
        list.append(item)
        return (list, 0)
    left = 0
    right = len(list)-1
    middle = int((right+left)/2)
    while left!=right:
        middle = int((left+right)/2)
        if item < list[middle]:
            right = middle-1
            if right<left:
                break
        elif item>list[middle]:
            left = middle+1
            if left>right:
                break
        else: insert(list, middle)

    index = -1
    
    if left!=right:
        if left>right:
            list.insert(left,item)
            return(list, left)
        else: 
            list.insert(right,item)
            return(list,item)
    else:
        if list[right] < item:
            index = right+1
            list.insert(index, item)
        else: 
            index = right
            list.insert(index, item)
    return list, index

def decodeCategory(text):
    """decodes text and insert data in Categories

    Args:
        text (string): extracted text from TXT
    """
    lines = text.split("\n")
    catName = lines[0].split(":")[1]
    daugtherCat = Category(catName)
    global Categories
    
    daugtherIndex = binarySearch(Categories, daugtherCat)
    if daugtherIndex == -1:
        (Categories, i) = binaryInsertion(Categories, daugtherCat)
        daugtherIndex = i
    count = 0
    index = len(lines)-1
    while index >= 0:
        if lines[index].find("[[Categoria:")!=-1:   
            catName = lines[index].split(":")[1].split("]]")[0].split("|")[0]   
            category = Category(catName)
            categoryIndex = binarySearch(Categories, category)
            if categoryIndex == -1:
                (Categories, categoryIndex) = binaryInsertion(Categories, category)
                daugtherIndex = Categories.index(daugtherCat)
            Categories[categoryIndex].DaugtherCategories.append(Categories[daugtherIndex])    
            Categories[daugtherIndex].MotherCategories.append(Categories[categoryIndex])
        else: 
            count+=1
            if count == 5:
                break
        index-=1
        pass
    pass

def decodeArticle(text):
    """decodes text and insert data in Categories

    Args:
        text (string): extracted text from TXT
    """
    global Categories
    lines = text.split("\n")
    articleName = lines[0] 
    article = Article(articleName,"") 
    count = 0           
    index = len(lines)-1  
    while index >= 0:
        if lines[index].find("[[Categoria:")!=-1:
            fullName = lines[index].split(":")[1]
            fullName = fullName.split("]]")[0]
            catName = fullName.split("|")[0]
            category = Category(catName)
            categoryIndex = binarySearch(Categories, category)
            if categoryIndex != -1:
                categoryIndex = Categories.index(category)
                Categories[categoryIndex].Articles.append(article)
                print(article,":::: ",catName)
            # else: Exception("This article has a no registered category.")
            pass
        else:
            count+=1
            if count==5:
                break
        index-=1
        pass
    pass

    pass

