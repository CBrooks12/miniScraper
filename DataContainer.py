import math


class WordObject(object):
    def __init__(self):
        self.weight = 1.0;
        self.time = 0.0;


dataContainer = {}


def add_to_container(word):
    #print("adding " + word + "to container")
    if word not in dataContainer:
        #print("initializing container for " + word)
        aPkg = {"list": [], "score": 0}
        dataContainer.update({word: aPkg})
    dataContainer[word]["list"].append(WordObject())
    dataContainer[word]["score"] += 1
    #print(word + " added!")


def update_objects(decay,threshold):
    #print("updating weights")
    for key in list(dataContainer):
        #print("updating " + key)
        count = 0.0
        for obj in dataContainer[key]["list"]:
            obj.time += 1.0
            obj.weight = 2.0-math.pow(math.e, obj.time/(decay*2))
            #print("weight " + str(obj.time))
            if obj.weight < threshold:
                #print("object removed!")
                dataContainer[key]["list"].remove(obj)
            else:
                count += obj.weight
        if not dataContainer[key]["list"]:
            #print("key removed!")
            del dataContainer[key]
        else:
            dataContainer[key]["score"] = count
        #print("score " + str(count))


def display_results():
    for key, value in dataContainer.items():
        if(len(value["list"])) > 2:
            print("----------------------------")
            print("Word: " + key)
            print("Number: " + str(len(value["list"])))
            print("Score: " + str(value["score"]))