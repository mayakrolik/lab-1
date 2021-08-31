"""
Description: 

Author: Maya Krolik
August 19, 2021
Worksheet: https://docs.google.com/document/d/1FKt0ZGZyWoWqZ_sBXsLP527DLooXiNNauOJn39IXXiA/edit?usp=sharing
"""

from os import remove


#reviews = open("movieReviews.txt", "r+")
#stopWords = open("stopwords.txt", "r+")
filteredReviews = []

#------------------------------------------------------------------------------#
"""
Purpose: To remove the stop words from the movie reviews
Parameters: none
Return Value:
"""
def getStopWords():
    with open("movieReviews.txt", "r+") as reviews, open("stopwords.txt", "r+") as stopWords:
        for words in reviews:
            words.lower()
        reviews.filter(stopWords)
        for line in reviews:
            

    return



getStopWords()
print(filteredReviews)
    