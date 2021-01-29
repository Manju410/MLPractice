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
