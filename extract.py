import csv
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from pandas._libs import json
from tldextract import tldextract

ps = PorterStemmer()


def name(list):
    return ps.stem(list)


with open('C:/Users/upadh/Desktop/domains.txt', 'r') as csvFile,open('current.json', 'w') as f:
  csvReader = csv.DictReader(csvFile)
  string ={}
 # list1 = ["word"]
  count =0
  for row  in csvReader:
        for row in csvReader:
          #if row is 0 :
           for header, value in row.items():
              #print(tldextract.extract(value))
              ext = tldextract.extract(value)
              list = ext.domain
              list = name(list)
              #print(list)
              try:
                string[header].append("{0}".format(list))

              except KeyError:
                  string[header] = [list]

#for w in string:
 #     print(w, " : ", ps.stem(w))
  f.write(str(json.dump((string),f)))
 # json.dump(doubleQString, f)

    #fin = (string)


