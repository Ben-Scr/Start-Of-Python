from sys import stdout

def printArray(array):
    for element in array:
      stdout.write(str(element) + ' ')
    stdout.write('\n')