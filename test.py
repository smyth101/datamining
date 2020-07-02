import pandas as pd
import matplotlib.pyplot as plt
import datetime
df = pd.read_feather('sao_paulo-traffic_jams.feather')

def convert(timestamp):
    time = timestamp.time()
    time = time.strftime("%H:%M:%S")
    return time

def getDay(timestamp):
    date  = timestamp.date()
    days = {
        'Monday':0,
        'Tuesday':1,
        'Wednesday':2,
        'Thursday':3,
        'Friday':4,
        'Saturday':5,
        'Sunday':6
    }
    day = date.strftime('%A')
    return days[day]


def type_convert(types):
    if types == 'E':
        return 1
    else:
        return 0 

def rounder(value):
    return 100 * (round((value/100)))

def region_convert(region):
    regions = {
        'LESTE':0,
        'SUL':1,
        'CENTRO':2,
        'OESTE':3,
        'NORTE':4
    }
    return regions[region]

# print(df)
df1 = df.drop(columns=['segment','region','passage','direction','index'])
df1['timestamp'] = df1['timestamp'].apply(convert)
values = {'type': 0}
df1 = df1.astype({'type':'str'})
df1['type'] = df1['type'].apply(type_convert)
df5 = df
df5['day'] = df5['timestamp'].apply(getDay)
# print(df5)
dfRegion = df5
dfRegion['region'] = dfRegion['region'].apply(region_convert)
print(dfRegion)
df1 = df1.astype({'type':'int32'})
df1['jam_size'] = df1['jam_size'].apply(rounder)
# print(df1)
# plt.scatter(df1['timestamp'], df1['jam_size'])
# plt.show()

df3 = df1.loc[df1['type'] == 0]
df4 = df1.loc[df1['type'] == 1]

dfMon = df5.loc[df5['day'] == 0]
dfTue = df5.loc[df5['day'] == 1]
dfWed = df5.loc[df5['day'] == 2]
dfThu = df5.loc[df5['day'] == 3]
dfFri = df5.loc[df5['day'] == 4]
dfSat = df5.loc[df5['day'] == 5]
dfSun = df5.loc[df5['day'] == 6]

dfR0 = dfRegion.loc[dfRegion['region'] == 0]
dfR1 = dfRegion.loc[dfRegion['region'] == 1]
dfR2 = dfRegion.loc[dfRegion['region'] == 2]
dfR3 = dfRegion.loc[dfRegion['region'] == 3]
dfR4 = dfRegion.loc[dfRegion['region'] == 4]

# print('mean',df1['jam_size'].mean())
# print('med',df1['jam_size'].median())
# print('mode',df1['jam_size'].mode())

print('mean w/o expressway',df3['jam_size'].mean())
print('med w/o expressway',df3['jam_size'].median())
print('mode w/o expressway',df3['jam_size'].mode())

print('mean w expressway',df4['jam_size'].mean())
print('med w expressway',df4['jam_size'].median())
print('mode w expressway',df4['jam_size'].mode())

print('mean mon',dfMon['jam_size'].mean())
print('mean tue',dfTue['jam_size'].mean())
print('mean wed',dfWed['jam_size'].mean())
print('mean thu',dfThu['jam_size'].mean())
print('mean fri',dfFri['jam_size'].mean())
print('mean sat',dfSat['jam_size'].mean())
print('mean sun',dfSun['jam_size'].mean())


print('mean region 0', dfR0['jam_size'].mean())
print('mean region 1', dfR1['jam_size'].mean())
print('mean region 2', dfR2['jam_size'].mean())
print('mean region 3', dfR3['jam_size'].mean())
print('mean region 4', dfR4['jam_size'].mean())

# plt.scatter(df1['jam_size'], df1['type'])
# plt.show()
# plt.hist(df1['jam_size'])
# plt.show()
df2 = df1.groupby('jam_size').count()
df3 = df1.loc[df1['type'] == 0]
df4 = df1.loc[df1['type'] == 1]
df3 = df3.groupby('jam_size').count()
df4 = df4.groupby('jam_size').count()
# print(df1.groupby('jam_size').count())
# with pd.option_context("display.max_rows", 1000):
#     print(df1.groupby('jam_size').count())

# plt.plot(df3)
# plt.plot(df4)
# plt.show()

