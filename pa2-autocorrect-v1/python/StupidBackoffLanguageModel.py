import math
from LaplaceUnigramLanguageModel import LaplaceUnigramLanguageModel
from LaplaceBigramLanguageModel import LaplaceBigramLanguageModel
class StupidBackoffLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.ULM = LaplaceUnigramLanguageModel(corpus)
    self.BLM = LaplaceBigramLanguageModel(corpus)
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    self.ULM.train(corpus)
    self.BLM.train(corpus)
    pass

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    result = 0.0
    for i in range(len(sentence)-1):
      first = sentence[i]
      second = sentence[i+1]
      if(first in self.BLM.bigram):
        if(second in self.BLM.bigram[first]):
          #do not use backoff
          numer = self.BLM.bigram[first].get(second)
          denom = sum( self.BLM.bigram[first].values())
          result += math.log(float(numer)/denom )
        else:
          #use backoff
          result += self.ULM.score(second)
      else:
        #the first word does not appear
        result += self.ULM.score(first)
    # TODO your code here
    return result
