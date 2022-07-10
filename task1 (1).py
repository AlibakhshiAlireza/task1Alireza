# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ft1tzRPp2oCFE3tySUgE8kXQZfF-RBkW

# Import libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime, timedelta
import matplotlib.ticker as ticker
import matplotlib.ticker as plticker
pd.options.display.float_format='{:.2f}'.format
plt.rcParams['figure.figsize'] = [12,12]
sns.set(style='darkgrid')
import matplotlib.ticker as ticker
import matplotlib.ticker as plticker
from matplotlib import pyplot as plt
plt.style.use('ggplot')

"""# Loading Data"""

df = pd.read_csv("/content/drive/MyDrive/Data Analyst - Commercial/data_analysis_task_q1.csv")

df

df.sort_values(['passenger', 'price_check_time'],inplace = True)

df['price_check_time'] = pd.to_datetime(df['price_check_time'], dayfirst=True)
df['req_time'] = pd.to_datetime(df['req_time'], dayfirst=True)
df['passenger'] = df['passenger'].astype(str)
df['status'] = df['status'].astype(str)
df['driver'] = df['driver'].astype(str)
df['origin'] = df['origin'].astype(str)
df['destination'] = df['destination'].astype(str)

df.dtypes

df

Requested_DF = df[df['req_time'].isna() == False]
Not_requested_DF = df[df['req_time'].isna() == True]

Requested_DF['req_time'].isna().sum()

New_DF = pd.read_csv("/content/drive/MyDrive/Data Analyst - Commercial/data_analysis_task_q1.csv")
New_DF["FinalPrice"] = New_DF['price'] - New_DF['subsidy']
New_DF['price_check_time'] = pd.to_datetime(New_DF['price_check_time'], dayfirst=True)
New_DF['req_time'] = pd.to_datetime(New_DF['req_time'], dayfirst=True)
New_DF['passenger'] = New_DF['passenger'].astype(str)
New_DF['status'] = New_DF['status'].astype(str)
New_DF['driver'] = New_DF['driver'].astype(str)
New_DF['origin'] = New_DF['origin'].astype(str)
New_DF['destination'] = New_DF['destination'].astype(str)

New_DF

df.dtypes

Requested_DF["Time Delay"] = Requested_DF['req_time'] - Requested_DF['price_check_time']

New_DF["price_check_time"].isna().any()

New_DF.iloc[1,0].strftime('%A')

l = {}
l["DOW_PRICE_CHECK"] = []
for i in New_DF['price_check_time']:
  z = i.strftime('%A')
  l["DOW_PRICE_CHECK"].append(z)

l = pd.DataFrame(l)

New_DF = pd.concat([New_DF,l],axis = 1)

New_DF.sort_values(['passenger', 'price_check_time'],inplace = True)

New_DF.dtypes

df.iloc[0,0].strftime('%A')

Requested_DF

Requested_DF["Time Delay"].dt.days.unique()

plt.style.use('ggplot')
sns.countplot(x = Requested_DF["Time Delay"].dt.days)

New_DF['req_hour'] = ""

index = 0
for i in New_DF['req_time']:
  if pd.isnull(i) == False:
    New_DF.iloc[index,13] = i.strftime('%H')
  if pd.isnull(i) == True:
    New_DF.iloc[index,13] = np.nan
  index = index + 1

New_DF.dtypes
New_DF['req_hour'] = pd.to_numeric(New_DF['req_hour'], errors='coerce')

New_DF.dtypes

break_point = [0,5,8,11,16,19,22,24]
time_slots =['Early Morning','Morning Rush','Morning','Daytime','Evening Crowd','night','LateNight']
New_DF['Request_BINS'] = pd.cut(New_DF['req_hour'], bins = break_point, labels = time_slots)

plt.rcParams['figure.figsize'] = [12,12]
f = New_DF[pd.isnull(New_DF['req_hour']) == False]
ax = sns.countplot(x = f['Request_BINS'],data = f,hue = f['status'])
total = float(len(f))
for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_height()/total)
    x = p.get_x() + p.get_width()
    y = p.get_height()
    ax.annotate(percentage, (x, y),ha='center')
plt.show()

x = df.iloc[0,8] - df.iloc[0,0]

x.days

New_DF["Hour of price check"] = New_DF['price_check_time'].dt.hour

New_DF.dtypes
New_DF.corr()

New_DF['status of request from user'] = ""
index = 0
for i in New_DF['req_time']:
  if pd.isnull(i) == False:
    New_DF.iloc[index,16] = 1
  elif pd.isnull(i) == True:
    New_DF.iloc[index,16] = 0
  index = index + 1

New_DF['Dayname of Request'] = ""
New_DF['Dayname of pricecheck'] = ""

index = 0
for i in New_DF['req_time']:
  if pd.isnull(i) == False:
    New_DF.iloc[index,18] = i.day_name()
  else:
    New_DF.iloc[index,18] = np.nan
  index = index + 1

index = 0
for i in New_DF['price_check_time']:
  New_DF.iloc[index,19] = i.day_name()
  index = index + 1

New_DF.iloc[0,8].month_name()

New_DF

New_DF['status of drive from driver'] = ""
index = 0
for i in New_DF['status']:
  if i == "1.0":
    New_DF.iloc[index,17] = 1
  elif i == "2.0":
    New_DF.iloc[index,17] = 1
  elif i == "3.0":
    New_DF.iloc[index,17] = 0
  else:
    New_DF.iloc[index,17] = np.nan
  index = index + 1

New_DF['Monthname of Request'] = ""
New_DF['Monthname of pricecheck'] = ""

index = 0
for i in New_DF['req_time']:
  if pd.isnull(i) == False:
    New_DF.iloc[index,20] = i.month_name()
  else:
    New_DF.iloc[index,20] = np.nan
  index = index + 1

index = 0
for i in New_DF['price_check_time']:
  New_DF.iloc[index,21] = i.month_name()
  index = index + 1

New_DF

New_DF["Monthname of Request"].unique()
New_DF["Monthname of pricecheck"].unique()

"""#Customers And Drivers Behavior"""

Bashgah_Moshtarian = pd.DataFrame()
Club_Ranandegan = pd.DataFrame()

moshtarian = list(New_DF['passenger'].unique())

Bashgah_Moshtarian['id'] = moshtarian

ranandegan = list(New_DF['driver'].unique())
ranandegan.remove('nan')

Club_Ranandegan['id'] = ranandegan

Bashgah_Moshtarian["count of requests"] = ""
Bashgah_Moshtarian["count of cancelation"] = ""
Bashgah_Moshtarian["total spent"] = ""
Bashgah_Moshtarian["total subsidy"] = ""

New_DF

moshtarireqcount = {}
for i in moshtarian:
  x = df.loc[(df['passenger'] == i) & (pd.isnull(df['req_time']) == False)]
  g = x.shape[0]
  moshtarireqcount[i] = g

df.dtypes

moshtaricancelc = {}
for i in moshtarian:
  x = df.loc[(df['passenger'] == i) & (df['status'] == "2.0")]
  g = x.shape[0]
  moshtaricancelc[i] = g

moshtariantotalspent = {}
for i in moshtarian:
  spent = []
  x = df.loc[(df['passenger'] == i) & (df['status'] == "1.0")]
  for j in x['price']:
    spent.append(j)
  g = sum(spent)
  moshtariantotalspent[i] = g

moshtariansubsidy = {}
for i in moshtarian:
  spent = []
  x = df.loc[(df['passenger'] == i) & (df['status'] == "1.0")]
  for j in x['subsidy']:
    spent.append(j)
  g = sum(spent)
  moshtariansubsidy[i] = g

Bashgah_Moshtarian

index = 0
for i in Bashgah_Moshtarian['id']:
  Bashgah_Moshtarian.iloc[index,1] = moshtarireqcount[i]
  Bashgah_Moshtarian.iloc[index,2] = moshtaricancelc[i]
  Bashgah_Moshtarian.iloc[index,3] = moshtariantotalspent[i]
  Bashgah_Moshtarian.iloc[index,4] = moshtariansubsidy[i]
  index = index + 1

Bashgah_Moshtarian["points"] = ""

Bashgah_Moshtarian['count of cancelation'] = Bashgah_Moshtarian['count of cancelation'].astype(int)
Bashgah_Moshtarian['count of requests'] = Bashgah_Moshtarian['count of requests'].astype(int)

index = 0
for i,j,k in zip(Bashgah_Moshtarian["count of requests"],Bashgah_Moshtarian["count of cancelation"],Bashgah_Moshtarian["total spent"]):
  point = (i - j/2) * (k/1000)
  Bashgah_Moshtarian.iloc[index,5] = point
  index = index + 1

Bashgah_Moshtarian

"""Now Drivers Club"""

Club_Ranandegan["count of Compelete Trips"] = ""
Club_Ranandegan["count of cancelation"] = ""
Club_Ranandegan["total earning"] = ""
Club_Ranandegan["points"] = ""

New_DF

drivercompletetrip = {}
for i in Club_Ranandegan['id']:
  x = New_DF.loc[(New_DF['driver'] == i) & (New_DF['status'] == "1.0")]
  g = x.shape[0]
  drivercompletetrip[i] = g

drvcancl = {}
for i in Club_Ranandegan['id']:
  x = New_DF.loc[(New_DF['driver'] == i) & (New_DF['status'] == "3.0")]
  g = x.shape[0]
  drvcancl[i] = g

totalearn = {}
for i in Club_Ranandegan['id']:
  earn = []
  x = df.loc[(df['driver'] == i) & (df['status'] == "1.0")]
  for j in x['price']:
    earn.append(j)
  g = sum(earn)
  totalearn[i] = g

index = 0
for i in Club_Ranandegan['id']:
  Club_Ranandegan.iloc[index,1] = drivercompletetrip[i]
  Club_Ranandegan.iloc[index,2] = drvcancl[i]
  Club_Ranandegan.iloc[index,3] = totalearn[i]
  index = index + 1

Club_Ranandegan

index = 0
for i,j,k in zip(Club_Ranandegan["count of Compelete Trips"],Club_Ranandegan["count of cancelation"],Club_Ranandegan["total earning"]):
  point = (i - (j*2)) * (k/1000)
  Club_Ranandegan.iloc[index,4] = point
  index = index + 1

Club_Ranandegan

"""#Analyzing DATA"""

x = New_DF.loc[(pd.isnull(New_DF['req_hour']) == False) & (New_DF['price'] < 130000)]
sns.violinplot(data = x,
               x="status", y="price",
               split=True, inner="quart", linewidth=1)

sns.boxplot(data = New_DF,x = "price")

"""we have some outliers"""

def fences(df, variable_name):    
    q1 = df[variable_name].quantile(0.25)
    q3 = df[variable_name].quantile(0.75)
    iqr = q3-q1
    outer_fence = 3*iqr
    outer_fence_le = q1-outer_fence
    outer_fence_ue = q3+outer_fence
    return outer_fence_le, outer_fence_ue

outer_fence_le, outer_fence_ue = fences(New_DF, 'price')
print('Lower end outer fence: ', outer_fence_le)
print('Upper end outer fence: ', outer_fence_ue)

New_DF[New_DF['price']>130000]

x = New_DF.loc[(pd.isnull(New_DF['req_hour']) == False) & (New_DF['price'] < 130000)]
plt.rcParams['figure.figsize'] = [30,30]
sns.relplot(data=x,x="price", y="expected_duration", hue="status",size ="distance", sizes=(40, 400), alpha=.5, palette="muted",
            height=6)

max(New_DF['price'])
New_DF[New_DF['price'] == 1900000]

New_DF

New_DF.drop([21358],inplace = True)

New_DF['origin'].unique()

list_of_regions = list(New_DF['origin'].unique())

pd.options.display.float_format='{:.2f}'.format
for i in list_of_regions:
  for j in list_of_regions:
    m = New_DF.loc[(New_DF['origin'] == i) & (New_DF['destination'] == j)]
    o = float("{:.2f}".format(m['distance'].mean()))
    if pd.isnull(o) == False:
      print("Mean of Region {} and {} is {}".format(i,j,o))

for i in list_of_regions:
  for j in list_of_regions:
    m = New_DF.loc[(New_DF['origin'] == i) & (New_DF['destination'] == j)]
    o = float("{:.2f}".format(m['price'].mean()))
    if pd.isnull(o) == False:
      print("Mean of Region {} and {} is {}".format(i,j,o))

for i in list_of_regions:
  for j in list_of_regions:
    m = New_DF.loc[(New_DF['origin'] == i) & (New_DF['destination'] == j)]
    o = float("{:.2f}".format(m['expected_duration'].mean()))
    if pd.isnull(o) == False:
      print("Mean of Region {} and {} is {}".format(i,j,o))

New_DF.dtypes

plt.rcParams['figure.figsize'] = [12,12]
sns.barplot(data = x , x = "Request_BINS" , y = "price" , hue = "status")

outer_fence_le, outer_fence_ue = fences(New_DF, 'distance')
print('Lower end outer fence: ', outer_fence_le)
print('Upper end outer fence: ', outer_fence_ue)

x = New_DF.loc[(New_DF["distance"] < 10785.0) & (New_DF["distance"] > 0)]
sns.displot(x, x="distance" , hue = "status of request from user" , kind="kde")

x = New_DF.loc[(New_DF["price"] < 130000) & (New_DF["distance"] > 0)]
sns.displot(x, x="price" , hue = "status of request from user" , kind="kde")

pd.isnull(New_DF["status of drive from driver"]).any()

x = New_DF.loc[(New_DF["distance"] < 10785.0) & (New_DF["distance"] > 0)]
palette ={1: "C0", 0: "C1"}
sns.displot(x, x="distance" , hue = "status of drive from driver" , kind="kde" , palette = palette)

x = New_DF.loc[(New_DF["price"] < 130000) & (pd.isnull(New_DF['req_hour']) == False)]
sns.displot(x, x="price" , hue = "status" , kind="kde")

x = New_DF.loc[(New_DF["price"] < 130000) & (pd.isnull(New_DF['req_hour']) == False)]
sns.displot(x, x="subsidy" , hue = "status" , kind="kde")

x = New_DF.loc[New_DF["price"] < 130000]
sns.displot(x, x="subsidy" , hue = "status of request from user" , kind="kde")

sns.boxplot(data = x , x = "status" , y = "price")

x = New_DF.loc[(New_DF["distance"] < 10785.0) & (New_DF["distance"] > 0) & (pd.isnull(New_DF['req_hour']) == False)]
sns.boxplot(data = x , x = "status" , y = "distance")

sns.boxplot(data = x , x = "status" , y = "subsidy")

x = New_DF.loc[(New_DF["price"] < 130000) & (pd.isnull(New_DF['req_hour']) == False)]
sns.boxplot(data = x , x = "Request_BINS" , y = "price" , hue = "status")

plt.rcParams['figure.figsize'] = [12,12]
sns.barplot(data = x , x = "origin" , y = "price" , hue = "status")

plt.rcParams['figure.figsize'] = [12,12]
sns.barplot(data = x , x = "destination" , y = "price" , hue = "status")

x = New_DF.loc[(New_DF["price"] < 130000) & (pd.isnull(New_DF['req_hour']) == False)]
sns.boxplot(data = x , x = "Dayname of Request" , y = "price" , hue = "status")

plt.rcParams['figure.figsize'] = [12,12]
sns.barplot(data = x , x = "Dayname of Request" , y = "price" , hue = "status")

plt.rcParams['figure.figsize'] = [12,12]
f = New_DF[pd.isnull(New_DF['req_hour']) == False]
ax = sns.countplot(x = f['Dayname of Request'],data = f,hue = f['status'])
total = float(len(f))
for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_height()/total)
    x = p.get_x() + p.get_width()
    y = p.get_height()
    ax.annotate(percentage, (x, y),ha='center')
plt.show()

plt.rcParams['figure.figsize'] = [12,12]
f = New_DF
ax = sns.countplot(x = f['Dayname of pricecheck'],data = f,hue = f['status of request from user'])
total = float(len(f))
for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_height()/total)
    x = p.get_x() + p.get_width()
    y = p.get_height()
    ax.annotate(percentage, (x, y),ha='center')
plt.show()

plt.rcParams['figure.figsize'] = [12,12]
f = New_DF
ax = sns.barplot(x = f['Dayname of pricecheck'],data = f, y = "price")

plt.rcParams['figure.figsize'] = [12,12]
f = New_DF[pd.isnull(New_DF['req_hour']) == False]
ax = sns.countplot(x = f['Dayname of Request'],data = f,hue = f['status of drive from driver'])
total = float(len(f))
for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_height()/total)
    x = p.get_x() + p.get_width()
    y = p.get_height()
    ax.annotate(percentage, (x, y),ha='center')
plt.show()

x = New_DF.loc[(pd.isnull(New_DF['req_hour']) == False) & (New_DF['price'] < 130000) & ((New_DF['status'] == "2.0") | (New_DF['status'] == "3.0"))]
g = sns.relplot(
    data=x,
    x="distance", y="price",
    hue="status", size="expected_duration", sizes=(10, 200),
)

Bashgah_Moshtarian

sns.displot(Bashgah_Moshtarian, x="total spent")
sns.displot(Bashgah_Moshtarian, x="count of cancelation")

plt.ticklabel_format(style='plain')
g = sns.scatterplot(x="total spent", y="total subsidy", data=Bashgah_Moshtarian)

"""#First Impression"""

plt.rcParams['figure.figsize'] = [12,12]
Requested_DF['status'] = Requested_DF['status'].astype(str)
f = Requested_DF.loc[Requested_DF['price'] < 150000]
sns.stripplot(data=f, x='price', y='status')

sns.boxplot(data = f , x = "status" , y = "price")

ax = sns.countplot(data = f , x = "status")
total = float(len(f))
for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_height()/total)
    x = p.get_x() + p.get_width()
    y = p.get_height()
    ax.annotate(percentage, (x, y),ha='center')
plt.show()

f = df.loc[df["price"]<150000]
sns.distplot(f["price"])

sns.pairplot(f, hue="status")

plt.rcParams['figure.figsize'] = [12,12]
sns.pairplot(f, hue="status" , x_vars = "price" , y_vars = "price" , height = 12)

sns.pairplot(f, hue="status" , x_vars = "price" , y_vars = "distance" , height = 12)

New_DF

f = Requested_DF.loc[(Requested_DF['price']<130000) & ((Requested_DF['status'] == "2.0") | (Requested_DF['status'] == "1.0"))]

sns.pairplot(f, x_vars = "price" , y_vars = "distance" , height = 12)

sns.scatterplot(data = f,x = "price",y = "distance",hue = "status")

f = Requested_DF.loc[(Requested_DF['price']<130000) & (Requested_DF['status'] == "2.0")]
sns.scatterplot(data = f,x = "price",y = "distance",hue = "status")

f = Requested_DF.loc[(Requested_DF['price']<130000) & (Requested_DF['status'] == "3.0")]
sns.scatterplot(data = f,x = "price",y = "distance",hue = "status")

f = Requested_DF.loc[(Requested_DF['price']<130000) & (Requested_DF['status'] == "4.0")]
sns.scatterplot(data = f,x = "price",y = "distance",hue = "status")

"""#Statistical Tests"""

df.corr()

pip install researchpy

import researchpy as rp
import scipy.stats as stats

summary, results = rp.ttest(group1= df['price'][df['status'] == '2.0'], group1_name= "Canceled By Customer",
         group2= df['price'][df['status'] == '1.0'], group2_name= "Done")
print(summary)

print(results)

stats.ttest_ind(df['price'][df['status'] == '2.0'],
         df['price'][df['status'] == '1.0'])

"""now drivers"""

summary, results = rp.ttest(group1= df['price'][df['status'] == '3.0'], group1_name= "Canceled By Driver",
         group2= df['price'][df['status'] == '1.0'], group2_name= "Done")
print(summary)

print(results)

"""now drivers and customers"""

summary, results = rp.ttest(group1= df['price'][df['status'] == '2.0'], group1_name= "Canceled By Customer",
         group2= df['price'][df['status'] == '3.0'], group2_name= "Canceled By Driver")
print(summary)

print(results)

"""#Saves and inputs

Bashgah_Moshtarian
Club_Ranandegan
New_DF
Not_requested_DF
Requested_DF
"""

Bashgah_Moshtarian.dtypes

Club_Ranandegan.dtypes

New_DF.dtypes

Bashgah_Moshtarian.to_csv("/content/drive/MyDrive/Save Variables/Bashgah_Moshtarian.csv")
Club_Ranandegan.to_csv("/content/drive/MyDrive/Save Variables/Club_Ranandegan.csv")
New_DF.to_csv("/content/drive/MyDrive/Save Variables/New_DF.csv")
Not_requested_DF.to_csv("/content/drive/MyDrive/Save Variables/Not_requested_DF.csv")
Requested_DF.to_csv("/content/drive/MyDrive/Save Variables/Requested_DF.csv")