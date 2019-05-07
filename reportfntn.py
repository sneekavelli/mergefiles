import os
import glob
import pandas


def concatenate(in="/Users/khalidbashier/Desktop/index/",outfile ="/Users/khalidbashier/Desktop/index/concatenated.csv"):

#take in the the tables/files we need from my index directory and print out the file we concatenate into the out file

    os.chdir(in)
    fileList=["parentOrder.csv","childOrder.csv","fillOrder.csv"]
    dfList=[]
    colnames=["ParentOrderId", "Symbol", "ParentOrderQuantity","Side", "Name", "Sector", "Broker", "Algo", "FillQty", "Fill", "Price"]

#for loop which stores all filenames into a dataframe variable which can then be used to append the files.

for filename in fileList:
    print(filename)
    df = pd.read_csv(filename, header = None)
    dfList.append(df) 
    concatDf=pandas.concat(dfList,axis=0)
    concatDf.columns=colnames
    concatDf.to_csv(outfile, index=None)	  
