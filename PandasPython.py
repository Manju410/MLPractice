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


#Handling null values by fillna method
# parsedates methode will convert to datetime
dfweather= pd.read_csv("C:\Manjunath\Personal\Manju\Pandas\csv\missing_data.csv", parse_dates=["day"])

dfweather.set_index("day", inplace=True) # setting day column as index value
dffill=dfweather.fillna(0) # filling null values to 0 in dataframe

#filling null values to 0 and words by passing into dictionary
dfnew=dfweather.fillna({
    "temprature":0,
    "windspeed":0,
    "event":"No event"
})

# ffill method will fill in forward steps
newdf= dfweather.fillna(method="ffill",axis="columns") # method="bfill" backword filling

#limit will fill the na values to one step forword
newdf= dfweather.fillna(method="ffill", limit=1)

# method time and interpolate will fill the null values by time analysis
newdf= dfweather.interpolate(method="time") # default method is linear

# to drop the null values
newdf= dfweather.dropna()
newdf= dfweather.dropna(how="all") # droping row contains all na values in row

newdf= dfweather.dropna(thresh=1) # droping null values with particular rows


# Replacing wrong data to nan values
dfweather= pd.read_csv("C:\Manjunath\Personal\Manju\Pandas\csv\replace.csv")
dfweather
newdf= dfweather.replace([-999,-8888], np.Nan)

# Replacing wrong data by regular expression
newdf= dfweather.replace({
    "temprature":"[A-Za-z]+",
    "windspeed":"[A-Za-z]+"
},'', regex=True)
newdf

# Group By method
# Grouping table by city wise
newyorkweather= pd.read_csv("C:\Manjunath\Personal\Manju\Pandas\csv\groupby.csv")

g= newyorkweather.groupby("city")
for city,citydf in g:
    print(city)
    print(citydf)
 
# groupin by mumbai city
g.get_group("mumbai")
g.max() # maximum value in group
g.mean() # average value in group


# Concatenating two dataframes
# india weather dataframe
india_weather=pd.DataFrame({
    "city":["mumbai","delhi","banglore"],
    "temprature":[32,45,30],
    "humidity":[80,60,70]
})

#us weather dataframe
us_weather=pd.DataFrame({
    "city":["newyork","chicago","orlando"],
    "temprature":[21,10,30],
    "humidity":[70,50,80]
})

df=pd.concat([india_weather,us_weather])
df=pd.concat([india_weather,us_weather], ignore_index=True)
df=pd.concat([india_weather,us_weather],keys=["india","us"])
df.loc["india"]


# Merging two Data Frames
df=pd.DataFrame({"cituy":["newyork","chikogo","canada"],"temp":[56,76,34]})
df1=pd.DataFrame({"cituy":["newyork","chikogo","canada"],"temp":[56,76,34]})
pd.merge(df,df1,on="cituy")


# Pivot Table
pivotdf= pd.read_csv("C:\Manjunath\Personal\Manju\Pandas\csv\groupby.csv")
pivotdf.pivot(index="day", columns="city",values="windspeed")
pivotdf.pivot(index="windspeed", columns="city")
pivotdf.pivot_table(index="city",columns="day",aggfunc="sum")
pivotdf.pivot_table(index="city",columns="day",margins=True)


#Merge

meltdf= pd.read_csv("C:\Manjunath\Personal\Manju\Pandas\csv\melt.csv")
df1=pd.melt(meltdf,id_vars=["day"])
df1[df1["variable"]=="banglore"]

# stack and unstack
satckdf= pd.read_csv("C:\Manjunath\Personal\Manju\Pandas\csv\stack.csv",header=[0,1])
satckdf.stack()
satckdf.stack(level=0)
