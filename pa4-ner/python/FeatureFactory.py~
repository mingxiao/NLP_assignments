import json, sys
import base64
from Datum import Datum
import re

class FeatureFactory:
    """
    Add any necessary initialization steps for your features here
    Using this constructor is optional. Depending on your
    features, you may not need to intialize anything.
    """
    def __init__(self):
        pass


    """
    Words is a list of the words in the entire corpus, previousLabel is the label
    for position-1 (or O if it's the start of a new sentence), and position
    is the word you are adding features for. PreviousLabel must be the
    only label that is visible to this method. 
    """

    def computeFeatures(self, words, previousLabel, position):
        features = []
        currentWord = words[position]
        #print words[0],words[1],words[2]
        """ Baseline Features """
        features.append("word=" + currentWord)
        features.append("prevLabel=" + previousLabel)
        features.append("word=" + currentWord + ", prevLabel=" + previousLabel)
        verb_pattern = '.*ing|.*ed]' #ends in -ing or -ed
        pronoun_pattern = 'who|whose|she|he'
	"""
        Warning: If you encounter "line search failure" error when
        running the program, considering putting the baseline features
	back. It occurs when the features are too sparse. Once you have
        added enough features, take out the features that you don't need. 
	"""


	""" TODO: Add your features here """
	      # current word is upper case and it is NOT the first word in the sentence
        if (currentWord[0].isupper() and position != 0):
          features.append("case=Title")
          if(position < len(words)-1): #.73
            #if the word said appeared before or after
            if(words[position+1] == 'said' or words[position+1]=='says'): #.737
              features.append('case=Title'+',saidAppearedWithinOne=True')
            #if next word is 's or '
            if(words[position+1]=='\'s' or words[position+1]=='\''):
              features.append('case=Title'+',possessive=True')
            #if the next word is a comma
            if(words[position+1]==','): #.74
              features.append('case=Title'+',nextWordComma=True')
            #if the next word is a verb .741
            if(re.match(verb_pattern, words[position+1])):
              features.append('case=Title'+',nextWordVerb=True')
          if(position > 0):
            if(words[position-1] == 'said' or words[position-1]=='says'):
              features.append('case=Title'+',saidAppearedWithinOne=True')
          # if there was a pronoun (who,he,she) within 2 words
          #if(position < len(words)-2): 
          #  if(re.match(pronoun_pattern, words[position+1]) or re.match(pronoun_pattern, words[position+2])):
          #    features.append('case=Title'+',pronounWithinTwo=True')
        
        
          
          
        #if(position > 0):
          #previous word is upper case. lowered F
        #  if(words[position-1][0].isupper()):
        #    features.append('prevCase=Title')
            
        # the next word is upper case. Lowered F
        #if(position < len(words)-1):
        #  if(words[position+1][0].isupper()):
        #    features.append('nextCase=Title')
        return features

    """ Do not modify this method """
    def readData(self, filename):
        data = [] 
        
        for line in open(filename, 'r'):
            line_split = line.split()
            # remove emtpy lines
            if len(line_split) < 2:
                continue
            word = line_split[0]
            label = line_split[1]

            datum = Datum(word, label)
            data.append(datum)

        return data

    """ Do not modify this method """
    def readTestData(self, ch_aux):
        data = [] 
        
        for line in ch_aux.splitlines():
            line_split = line.split()
            # remove emtpy lines
            if len(line_split) < 2:
                continue
            word = line_split[0]
            label = line_split[1]

            datum = Datum(word, label)
            data.append(datum)

        return data


    """ Do not modify this method """
    def setFeaturesTrain(self, data):
        newData = []
        words = []

        for datum in data:
            words.append(datum.word)

        ## This is so that the feature factory code doesn't
        ## accidentally use the true label info
        previousLabel = "O"
        for i in range(0, len(data)):
            datum = data[i]

            newDatum = Datum(datum.word, datum.label)
            newDatum.features = self.computeFeatures(words, previousLabel, i)
            newDatum.previousLabel = previousLabel
            newData.append(newDatum)

            previousLabel = datum.label

        return newData

    """
    Compute the features for all possible previous labels
    for Viterbi algorithm. Do not modify this method
    """
    def setFeaturesTest(self, data):
        newData = []
        words = []
        labels = []
        labelIndex = {}

        for datum in data:
            words.append(datum.word)
            if not labelIndex.has_key(datum.label):
                labelIndex[datum.label] = len(labels)
                labels.append(datum.label)
        
        ## This is so that the feature factory code doesn't
        ## accidentally use the true label info
        for i in range(0, len(data)):
            datum = data[i]

            if i == 0:
                previousLabel = "O"
                datum.features = self.computeFeatures(words, previousLabel, i)

                newDatum = Datum(datum.word, datum.label)
                newDatum.features = self.computeFeatures(words, previousLabel, i)
                newDatum.previousLabel = previousLabel
                newData.append(newDatum)
            else:
                for previousLabel in labels:
                    datum.features = self.computeFeatures(words, previousLabel, i)

                    newDatum = Datum(datum.word, datum.label)
                    newDatum.features = self.computeFeatures(words, previousLabel, i)
                    newDatum.previousLabel = previousLabel
                    newData.append(newDatum)

        return newData

    """
    write words, labels, and features into a json file
    Do not modify this method
    """
    def writeData(self, data, filename):
        outFile = open(filename + '.json', 'w')
        for i in range(0, len(data)):
            datum = data[i]
            jsonObj = {}
            jsonObj['_label'] = datum.label
            jsonObj['_word']= base64.b64encode(datum.word)
            jsonObj['_prevLabel'] = datum.previousLabel

            featureObj = {}
            features = datum.features
            for j in range(0, len(features)):
                feature = features[j]
                featureObj['_'+feature] = feature
            jsonObj['_features'] = featureObj
            
            outFile.write(json.dumps(jsonObj) + '\n')
            
        outFile.close()

