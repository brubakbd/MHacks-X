import requests
import json
import numpy as np

def load_data():
    data = requests.get("https://foodphoriadb.herokuapp.com/train")
    fil = open("types.txt", "r")
    types = fil.read().replace("\"", "").replace("\n","").split(",")
    count = 0
    jsondata = json.loads(data.text)
    arr = np.zeros((len(jsondata), 260))
    y = np.zeros((len(jsondata), 1))
    for j in jsondata:
        for i in j['prefs']:
            m = types.index(i)
            arr[count][m] = 1
        arr[count][129] = j['grating'] / 5
        for i in j['rprefs']:
            m = types.index(i)
            arr[count][m+130] = 1
        arr[count][259] = j['plevel'] / 4
        y[count] = j['rating'] / 5
        count+=1
    x = np.array(arr, dtype='float32')
    y = np.array(y, dtype='float32')
    return x, y
    
def org_data(data, prefs, rprefs):
    fil = open("types.txt", "r")
    types = fil.read().replace("\"", "").replace("\n","").split(",")
    arr = np.zeros((len(data), 260))
    count = 0
    for j in data:
        for i in prefs:
            if i['type'] != 'dummy':
                m = types.index(i['type'])
                arr[count][m] = 1
        if 'rating' in j:
            arr[count][129] = j['rating'] / 5
        for i in rprefs:
            if i['type'] != 'dummy':
                m = types.index(i['type'])
                arr[count][m+130] = 1
        if 'price_level' in j:
            arr[count][259] = j['price_level'] / 4
        count +=1
    x = np.array(arr, dtype='float32')
    return x
    # for i in prefs:
    #     if i['type'] != 'dummy':
    #         m = types.index(i['type'])
    #         arr[0][m] = 1
    # if 'rating' in data:
    #     arr[0][129] = data['rating'] / 5
    # else:
    #     arr[0][129] = .6
    # for i in rprefs:
    #     m = types.index(i)
    #     arr[0][m + 130] = 1

    # plevel = 2
    # if 'price_level' in data:
    #     plevel = data['price_level']
    # arr[0][259] = plevel / 4
    # x = np.array(arr, dtype='float32')
    # return x
