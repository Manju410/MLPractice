#PANDAS_DataFrame
#Creating DataFrame from Csv file--- weather csv contains temprature, windspeed,event columns

import pandas as pd
df= pd.read_csv("C:\Manjunath\Personal\Manju\Pandas\csv\dataframe.csv")
df.head()
df["temprature"].max()
df["day"][df["event"]=="rain"]
df["windspeed"].mean()

# Creating DataFrame from Dictionary passing weather table columns to it.

weather={
    "day":["1/1/2018","1/2/2018","1/2/2018"],
    "temp":[32,28,44],
    "windspeed":[8,7,5],
    "event":["rain","snow","sunny"]
}
df1= pd.DataFrame(weather)

rows,cols=df1.shape
df[1:9]    # slicing dataframe
df.columns # datarame columns
type(df["event"]) # type of dataframe column
df.describe()  # provides statistics of dataframe
df[df["temprature"]>=32]  # printing columns having temp >32
df[df["temprature"]==df["temprature"].max()] # printing rows having max temp
df.index                        # to find index of dataframe
df.set_index("day",inplace=True)  # setting index values to day column of dataframe
df.reset_index(inplace=True)     # undoing dataframe column for reseting


# Handling missing values

#importing stocks table contains ticker, eps, revenue,price columns
# prive header is none to skip headers, provide customize names for columns
#dfexcel= pd.read_csv("C:\Manjunath\Personal\Manju\Pandas\csv\excel.csv",header=None, names=["ticker","eps","revenue","price","people"])

#handle null values for particular words
#dfexcel= pd.read_csv("C:\Manjunath\Personal\Manju\Pandas\csv\excel.csv",na_values=["not available","n.a"])

#handle null values by using dictionary
dfexcel= pd.read_csv("C:\Manjunath\Personal\Manju\Pandas\csv\excel.csv",na_values={
    "eps":["not available","n.a"],
    "revenue":["not available","n.a",-1],
     "people":["not available","n.a",-1],
     "price":["not available","n.a"]
})


#dfexcel.to_csv("C:\Manjunath\Personal\Manju\Pandas\csv\new.csv", index=false) # to write csv
#dfexcel.to_csv("new.csv", columns=["tickcer","eps"]) # specified columns
#dfexcel.to_csv("new.csv", header=false) # skiping header

# Writing customize function to handle null values
def convertpeople(cell):
    if cell=="n.a":
        return "sam walton"
    return cell

# call customize function by parameter converters
dfex= pd.read_excel("C:\Manjunath\Personal\Manju\Pandas\excel.xlsx","Sheet1", converters={
    "people":convertpeople
})

# exporting dataframe to excel sheet by making index false
pd.to_excel("new.xlsx",sheet_name="stocks", index=False)

pd.to_excel("new.xlsx",sheet_name="stocks", index=False,startrow=3,startcol=2) # writing from particular row and col
