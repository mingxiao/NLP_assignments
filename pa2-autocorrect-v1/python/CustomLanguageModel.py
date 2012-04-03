from LaplaceBigramLanguageModel import LaplaceBigramLanguageModel
from LaplaceUnigramLanguageModel import LaplaceUnigramLanguageModel
import math
class CustomLanguageModel:
#Bigram model with kneser-ney smoothing
  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.BLM = LaplaceBigramLanguageModel(corpus)
    self.ULM = LaplaceUnigramLanguageModel(corpus)
    self.discount = 0.75 
    self.ends_with = dict() #number of bigrams that ends with a particular word
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    self.BLM.train(corpus)
    self.ULM.train(corpus)
    for word in self.ULM.unigram.keys():
      count = 0
      for start_word in self.BLM.bigram.keys():
        if word in self.BLM.bigram[start_word]:
          count+=1 
      self.ends_with[word] = count
  def normalize(self, word):
    count_word = self.ULM.unigram.get(word,0)+1
    num_type_following_word = len(self.BLM.bigram.get(word,{})) 
    return (self.discount/count_word) * num_type_following_word
  
  def p_continuation(self,word):
    #word_hash = self.BLM.bigram.get(word,{})
    
    #number of word types followed by word
    return float(self.ends_with.get(word,0))/ self.BLM.num_types
  
  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # TODO your code here
    result = 0.0
    for i in range(len(sentence)-1):
      first = sentence[i]
      second = sentence[i+1]
      if first in self.BLM.bigram:
        denom = self.ULM.unigram.get(first)
        if second in self.BLM.bigram[first]:
          #the bigram is present
          numer = max(self.BLM.bigram[first].get(second)-self.discount, 0)
        else:
          numer = 0.0
      else:
        #first is not part of any bigram
        numer = 0.0
        denom = 1.0
      
      #numer = max(self.BLM.bigram[first].get(second)-self.discount, 0)
      #denom = self.ULM.unigram.get(first,0)
      l = self.normalize(first) #lambda weight
      pc = self.p_continuation(second) #continuation probability
      prob = (float(numer)/denom) + (pc * l)
      #print prob,numer, denom, pc, l
      if prob == 0:
        result += math.log(10e-15)
      else:
        result += math.log(prob)
    #print result
    return result
