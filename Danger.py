import os

keyWords = [['kill myself', 100, '\self harm.txt'],
            ['die', 10, '\self harm.txt']]

def scanFile(txt):
    danger = 0
    for word in keyWords:
        newTxt = txt
        All = False
        while not All:
            if word[0] in newTxt:
                danger += word[1]
                newTxt = newTxt.replace(word[0], '', 1)
            else:
                All = True

    if danger > 99:
        return True
    else:
        return False

def search():
    dangers = []
    directory = os.getcwd().replace('\Program Code', '\Journal Entries')
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if scanFile(open(f).read()):
            dangers.append(filename)
    return(dangers)