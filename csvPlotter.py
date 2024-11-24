import pandas as pd
import matplotlib.pyplot as plt
import glob
import os


pathIn = "C:/Users/Josh/Documents/GitHub/csvPlotter/dummyData/"   #backslash vs forward slash important here (also trailing slash)
pathOut = "C:/Users/Josh/Documents/GitHub/csvPlotter/Output/"



################ MAIN CODE #################
csvFiles = glob.glob(f'{pathIn}*.csv')  #get list of all csv files in specified directory
os.makedirs(pathOut, exist_ok=True)     #make sure output directory is valid (create it if not)


#loop through each csv file
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
    plt.title(name)
    plt.grid()
    #plt.show()
    plt.savefig(os.path.join(pathOut, name + '.png'))

    plt.close()

print("Finished! Plots saved to: " + pathOut)
