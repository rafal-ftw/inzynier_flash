import os
import csv

from interpreter import interpreter


def executeAllScenarios():

    # egzekutuje wszystkie scenariusze z biblioteki scenarios
    arr = os.listdir(str(os.getcwd()) + "\\app\\scenarios\\")

    i = 0
    while i < len(arr):
        arr[i] = (str(os.getcwd()) + "\\app\\scenarios\\") + arr[i]
        i += 1
        
    print(arr)

    #krok w instrukcji dla jednego scenariusza, lines
    step      = 0
    lines     = []

    #zczytanie pliku csv
    var = 0

    while var < len(arr):
        with open(arr[var], 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                lines.append(row)

            # przywołanie do stołu interpretera z pliku interpreter.py, cale selenium gada za pomocą klasy interpreter
            mainInterpreter = interpreter()

            while step < len(lines):
                            
                print("KROK " + str(step + 1))
                mainInterpreter.readStep(lines[step])
                step += 1
        var += 1

def executeSelectedScenarios(arr):

    print(arr)

    #krok w instrukcji dla jednego scenariusza, lines
    step      = 0
    lines     = []

    #zczytanie pliku csv
    var = 0

    while var < len(arr):
        with open(arr[var], 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                lines.append(row)

            # przywołanie do stołu interpretera z pliku interpreter.py, cale selenium gada za pomocą klasy interpreter
            mainInterpreter = interpreter()

            while step < len(lines):
                            
                print("KROK " + str(step + 1))
                mainInterpreter.readStep(lines[step])
                step += 1
        var += 1



if __name__ == "__main__":
    executeAllScenarios()