import math
class LaplaceBigramLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.bigram = dict()
    self.N = 0 #number of tokens
    self.words = []
    self.V = 0 #vocabulary size
    self.num_types = 0 #the number of unique bigrams
    self.train(corpus)
    

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    for sentence in corpus.corpus:
      for i in range(len(sentence)-1): #go up to the last word b.c we want every pair of words
        first = sentence.data[i].word
        second = sentence.data[i+1].word
        second_hash = self.bigram.get(first,{})
        second_hash[second] = second_hash.get(second,0)+1
        self.bigram[first] = second_hash
        if(first not in self.words):
          self.words.append(first)
        if(second not in self.words):
          self.words.append(second)
      self.N += len(sentence)  
    self.V = len(self.words) 
    for k in self.bigram.keys():
      self.num_types += len(self.bigram[k])
    

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    result = 0.0
    #numer = 0.0
    #denom = 0.0
    for i in range(len(sentence)-1):
      first = sentence[i]
      second = sentence[i+1]
      if(first in self.bigram):
        #print 'here'
        denom = sum(self.bigram[first].values()) # no. of times (first, <other word>) appeared
        numer = self.bigram[first].get(second,0) 
        #if the second word appears in the first word's hash, get count. otherwise 0
      else:
        #print 'thereeeeeee'
        denom = 0
        numer = 0
        
      prob = float(numer+1)/(denom + self.V)
      result += math.log(prob)
      
   
    # TODO your code here
    return result
