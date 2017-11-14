#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spelling Recommender: Provides spelling suggestions comparing an input word
against words in a dictionary using,
  1 - Jaccard distance (with character bigrams and trigrams)
  2 - Damerau–Levenshtein distance
  
Note: as-is, it assumes the first letter in input word is correct. This can be 
  adjusted by redefining 'correct_list = dictionary' in lines 59 and 79
  
After running the script, use the function 'suggestions()' to generate
sugestions with a word (a string) as param. Can adjust number of suggestions
with param k

Created on Mon Nov 13 20:32:23 2017
@author: Reynaldo Vazquez
"""

import numpy as np
import nltk
from nltk.corpus import words
dictionary = words.words()

def create_ngram(input_word, n = 2):
  # Creates a set n-character grams from an input word
  #
  # In: input_word, a string
  #       n, as in n for ngram, an integer
  # Out: a list of n-character ngrams, list of strings
  #
  ngram_set = [input_word[i:i+n] for i in range(len(input_word)-n+1)]
  return ngram_set

def Jaccard_dist(input_ngrams, correct_ngrams):
  # Calculates the Jaccard distance (a measure of disimilarity) between two sets
  #  of ngrams (one ngram set for each of the 2 words to be compared)
  #
  # In: input_ngrams, a list or a set of n-character grams 
  #       ncorrect_ngrams, a list or a set of n-character grams 
  # Out: Jaccard distance, a float
  #
  intersec = set(input_ngrams) & set(correct_ngrams)
  union = set(input_ngrams) | set(correct_ngrams)
  Jaccard = 1 - len(intersec)/len(union)
  return Jaccard

def JD_suggestions(word, n = 2, k = 3):
  # Provides a spelling recommendation by minimizing Jaccard distance as 
  # described in  https://en.wikipedia.org/wiki/Jaccard_dist
  #
  # In: word, a word, string
  #     n, n as in ngram, an integer
  #     k, number of suggestions, integer
  # Out: k spelling suggestions, a list of strings
  #
  first_letter = word.lower()[0]
  input_ngram_set = create_ngram(word, n)
  correct_list = [w for w in dictionary if w.startswith(first_letter)]
  correct_ngram_list = [create_ngram(w, n) for w in correct_list]
  J_indexes = [Jaccard_dist(input_ngram_set, g) for g in correct_ngram_list]
  J_match = np.argpartition(J_indexes, k)
  suggestion_list = [correct_list[J_match[i]] for i in range(0,k)]
  return suggestion_list
  
  #J_match = np.argmax(J_indexes)
  #return correct_list[J_match]

def DLD_suggestions(word, k = 3):
  # Provides a spelling recommendation by minimizing Damerau–Levenshtein edit-
  # distance with adjacent transpositions as provided by nltk.edit_distance()
  # see https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
  #
  # In: word, a string
  #     k, number of suggestions, integer
  # Out: k spelling suggestions, a list of strings
  #
  first_letter = word.lower()[0]
  correct_list = [w for w in dictionary if w.startswith(first_letter)]
  DL_indexes = [nltk.edit_distance(word, w) for w in correct_list]
  DL_match = np.argpartition(DL_indexes, k)
  suggestion_list = [correct_list[DL_match[i]] for i in range(0,k)]
  return suggestion_list

# EXAMPLES
  
def suggestions(word, k = 3):
  print('Suggestions using DLD are:', DLD_suggestions(word, k))
  for n in range(2,4):
    print('Suggestions using JD w/ n =', n, 'are:', JD_suggestions(word, n, k))
  
suggestions('valiable')
JD_suggestions('fedeartion', n = 3)
DLD_suggestions('majic')


















