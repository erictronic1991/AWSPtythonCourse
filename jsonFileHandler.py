import json

def readJsonFile(fileName):
    data = ""
    with open('C:/Users/Eric/PycharmProjects/pythonProject3/insulin.json') as json_file:
        data = json.load(json_file)
    return data

