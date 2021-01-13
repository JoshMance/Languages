import numpy as np
import linguistics as ling
import csv
import nltk 
import itertools as it
from guibible.net import Bible as bible
import math as m

# Returns an ordered list of all the words in a text
def tokenize(text):
    return ling.tokenize(text)


# For a list of texts, returns a list of these texts in vector form using 
# the union of all the text's words to form a basis vector.
def vectorizeTexts(textList):
    # Make all texts lower case
    for ii in range(len(textList)):
        textList[ii] = textList[ii].lower()  
    # The list of all words across all texts
    wordList = []
    # The list of all the texts in tokenised form
    tokenTextList = []
    # For each text
    for ii in range(len(textList)):
        # An ordered list of all the words in the ii'th text in 
        # in the order they appear
        words = tokenize(textList[ii])
        tokenTextList.append(words)
        # Append each word on the wordList
        for jj in range(len(words)):
            wordList.append(words[jj]) 
    # Remove all duplications in the wordList
    wordList = list(dict.fromkeys(wordList))
    
    # The list of the text vectors
    vectorList = []
    # For all texts
    for ii in range(len(textList)):
        # Set up (0, 0, 0, 0 ..... 0) vector
        vector = [0]*len(wordList)
        # For all words in the wordList
        for jj in range(len(wordList)):
            word = wordList[jj]
            count = 0
            # For all words in the text, if the current dict. word is found 
            # update the count
            for tt in range(len(tokenTextList[ii])):
                if tokenTextList[ii][tt] == word:
                    count += 1
            # Add the count to the location in the vector corresponding to 
            # that word
            vector[jj] = count
        # Append the vectorized text to the vectorList
        vectorList.append(vector)
        
    # Return a list of these texts in vector form
    return vectorList, wordList

def length(vector):
    total = 0
    for ii in range(len(vector)):
        total += (vector[ii])**2
    total = total**0.5
    return total

def distance(vector1, vector2):
    total = 0
    for ii in range(len(vector1)):
        total += (vector1[ii] - vector2[ii])**2
    total = total**0.5
    return total
        
def similarity(textList, error):
    vectors, words = vectorizeTexts(textList)
    arr = []
    for ii in range(len(vectors)):
        arr.append(ii)
    arr = list(it.combinations(arr, 2))
        
    for ii in range(len(arr)):
        print("Texts " + str(arr[ii][0]+1), "and " + str(arr[ii][1]+1) 
              ,".........." , round(distance(vectors[arr[ii][0]], vectors[arr[ii][1]]), error))

def similarityAngle(textList, error):
    vectors, words = vectorizeTexts(textList)
    arr = []
    for ii in range(len(vectors)):
        arr.append(ii)
    arr = list(it.combinations(arr, 2))
        
    for ii in range(len(arr)):
        a = vectors[arr[ii][0]]
        b = vectors[arr[ii][1]]
        cosTheta = (np.dot(a,b))/(length(a)*length(b))
        theta = (m.acos(cosTheta))*(180/m.pi)
        
        print("Texts " + str(arr[ii][0]+1), "and " + str(arr[ii][1]+1) 
              ,".........." , round(theta, error))
  
    
textList = []

f = open(r"C:\Users\joshj\Desktop\Langauge\Matthew.txt", "r")
textList.append(f.read())
f = open(r"C:\Users\joshj\Desktop\Langauge\Mark.txt", "r")
textList.append(f.read())
f = open(r"C:\Users\joshj\Desktop\Langauge\Luke.txt", "r")
textList.append(f.read())
f = open(r"C:\Users\joshj\Desktop\Langauge\John.txt", "r")
textList.append(f.read())


error = 10
similarityAngle(textList, error)



    
    
        

