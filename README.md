
## Spelling Recommender

Python script providing spelling suggestions comparing an input word
against words in a dictionary. 

To find spelling suggestions it minimizes the,

* Jaccard distance (with character bigrams and trigrams) as described in 
[https://en.wikipedia.org/wiki/Jaccard_dist](https://en.wikipedia.org/wiki/Jaccard_dist)
* Damerau–Levenshtein edit-distance with adjacent transpositions [https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)

of the input string, against words in an `nltk` dictionary

#### Contents 
* [spelling_recommender.py](spelling_recommender.py) python scrypt with 
spelling recommender functions
* [README.md](README.md) this file


#### Examples

```
In [1]: suggestions('valiable')
Suggestions using DLD are: ['valuable', 'variable', 'viable']
Suggestions using JD w/ n = 2 are: ['variable', 'valuable', 'viable']
Suggestions using JD w/ n = 3 are: ['viable', 'valiant', 'valiance']

In [2]: JD_suggestions('fedeartion', n = 3)
Out[2]: ['federation', 'federationist', 'federalization']

In [3]: DLD_suggestions('majic')
Out[3]: ['magic', 'mazic', 'manic']
```

