import requests#this library runs just by pip installation, I'm using a virtual enviroment
import json
import hashlib
from os import listdir#importing library to list files


def getRequest(url):#getting the request of the url api and turn it into a json
    response = requests.get(url)
    return response.json()  

def postRequest():
    file = {'answer': open('answer.json', 'rb')}
    url = ''#url from api(post)
    response = requests.post(url, files = file)
    print(response.status_code)
    return response

def writeJson(file):
    with open('answer.json', 'w') as json_file:
        json.dump(file, json_file)

def readJson():
    with open('answer.json', 'r') as json_file:
        obj = json.load(json_file)
        return obj

def ceasarCipher(crypt, shift):
    cipher = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    decript = ''
    for w in crypt:
        if w.isalnum():
            for c in cipher:
                if c == w:
                    index_cipher = cipher.index(c)
                    if index_cipher - shift < 0:
                        index_cipher += 26
                        index_cipher -= shift
                        decript += cipher[index_cipher]
                        break
                    else:
                        index_cipher -= shift
                        decript += cipher[index_cipher]
                        break
        else:
            decript += w

    return decript

n = 9#shift number
url = ''#url to get api

api = getRequest(url)
jsonfiles = [f for f in listdir('')"""directory where the code is located""" if f.endswith('.json')]

if not 'answer.json' in jsonfiles:
    writeJson(api)
    print('Json File written')

api = readJson()#reading json file and putting in a variable

decyphered = ceasarCipher(api['cifrado'], n)#decyphering and storing
api['decifrado'] = decyphered#updating json with decyphering

hashe = hashlib.sha1(decyphered.encode()).hexdigest().lower()#doing sha1 hashing
api['resumo_criptografico'] = hashe#updating json with sha1 hash

writeJson(api)#updanting file

r = postRequest()
print('finished')
