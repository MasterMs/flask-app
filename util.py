def readAssign(file):
    file = open('index.html', 'r')
    index = file.read()
    file.close()
    return index