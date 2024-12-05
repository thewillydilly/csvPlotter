import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from tkinter import *
from tkinter import filedialog


def inputBrowse():    
    inputPath = filedialog.askdirectory()

    if not inputPath:
        return

    inputEntry.delete(0, END)
    inputEntry.insert(0, inputPath)

    return

def outputBrowse():    
    outputPath = filedialog.askdirectory()

    if not outputPath:
        return

    outputEntry.delete(0, END)
    outputEntry.insert(0, outputPath)

    return



def runPlotter():
    inputPath = inputEntry.get()
    outputPath = outputEntry.get()
    plotIndependently = plotInd.get() #0 if unchecked, 1 if checked

    # run checkers first
    if inputPath == "":
        print("no input path dummy")
        return
    csvFiles = glob.glob(f'{inputPath}/*.csv')  #get list of all csv files in specified directory
    if len(csvFiles) == 0:
        print("couldn't find any csv files in:", inputPath)
        return

    if outputPath == "":
        print("no output path specified!")
        return
    os.makedirs(outputPath, exist_ok=True)     #create output dir (if not already)

    #plot
    for file in csvFiles:
    
        #read in csv file
        df = pd.read_csv(file)
        name = os.path.basename(file).split('.')[0] #filename (for title)

        print("plotting " + name + "...")


        #massage data here
        x = df['x'] #column with header labeled "x"
        y = df['y']


        #plot
        plt.plot(x,y)
        
        if plotIndependently:
            plt.title(name)
            plt.grid()
            plt.savefig(os.path.join(outputPath, name + '.png'))
            plt.close()

    if not plotIndependently:
        name = "test"

        plt.title(name)
        plt.grid()
        plt.savefig(os.path.join(outputPath, name + '.png'))
        plt.close()


    print("Finished! Plots saved to: " + outputPath)


    return



root = Tk()
root.title("csv plotter v0.1")
root.geometry("500x280")


# input directory selection
inputRow = Frame(root)

Label(inputRow, text="Input: ").pack(side=LEFT)

inputEntry = Entry(inputRow, width=55)
inputEntry.pack(side=LEFT)

inputBrowseBtn = Button(inputRow, text="...", command=inputBrowse).pack(side=LEFT, padx=5)




# output directory selection
outputRow = Frame(root)

Label(outputRow, text="Output: ").pack(side=LEFT)

outputEntry = Entry(outputRow, width=55)
outputEntry.pack(side=LEFT)

outputBrowseBtn = Button(outputRow, text="...", command=outputBrowse).pack(side=LEFT, padx=5)



# options selections
optionsRow = Frame(root)

#Label(optionsRow, text="Plot Independently: ").pack(side=LEFT)
plotInd = IntVar() 
Checkbutton(optionsRow, text = "Plot Independently", 
                    variable = plotInd, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 20).pack(side=LEFT)


# run buttons
runbuttonRow = Frame(root)

runBtn = Button(runbuttonRow, text="Run", command=runPlotter).pack(side=LEFT)




# pack all rows together
inputRow.pack(fill=X)
outputRow.pack(fill=X)
optionsRow.pack(fill=X)
runbuttonRow.pack(fill=X)


root.mainloop()














