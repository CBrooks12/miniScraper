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


def get_top_score():
    topScore = 0;
    for key, value in dataContainer.items():
        if value["score"] > topScore:
            topScore = value["score"]
    return topScore


def update_lines(tCounter,lines,cap):
    threshold = 3
    for key, value in dataContainer.items():
        if key not in lines:
            if value["score"] > threshold:
                aPkg = {"x":[tCounter],"y":[value["score"]]}
                lines.update({key: aPkg})
        else:
            if all(i < threshold for i in lines[key]["y"]):
                del lines[key]
            else:
                lines[key]["x"].append(tCounter)
                lines[key]["y"].append(value["score"])
                if len(lines[key]["x"]) > cap:
                    lines[key]["x"].pop(0)
                    lines[key]["y"].pop(0)
    return lines
