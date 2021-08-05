import pandas as pd

dataset = pd.read_csv('dataset_ZakirTestZ1.csv')
df = pd.DataFrame(dataset)
df.drop(df.iloc[:, 1200:1275], inplace = True, axis = 1)
mean = df.mean(axis=1)
data_new = df.fillna('mean')
data_new['mean'] = mean
data_new['max'] = df.max(axis=1)
data_new['min'] = df.min(axis=1)
data_new['kurtosis'] = df.kurtosis(axis=1)
data_new['skew'] = df.skew(axis=1)
data_new['std'] = df.std(axis=1)
data_new = data_new.fillna(mean) 
data_new = data_new.iloc[:,-6:]
data_new = pd.DataFrame(data_new)
data_new.to_csv('NewFile.csv')
exit()

# dataset1 = pd.read_csv('NewFile.csv')
# df2 = pd.DataFrame(dataset1)
# print(df2)



print(df.head())
df.drop(df.iloc[:, 1200:1275], inplace = True, axis = 1)
print('After removing Extra column \n', df.head())
a=len(df.columns)-1
print('Length of column ', a)


mean = df.mean(axis=1)
print('Mean \n', mean)
print('Hello \n', df.iloc[:, 0:-1])
data_new = df.fillna(mean, inplace = True, axis=0)
print('New Data \n', data_new)
#data_new = df.fillna(0.0)                       
#print('Remove NaN \n', data_new) 
 

#data_new['Mean Values']= data_new.iloc[:,1:-1].mean(axis=0)
#print('Mean ', data_new['Mean Values'])

#Mean.name = 'Mean Values'
#MeanColumn = data_new.append(Mean.transpose())   # .append(Mean.transpose())
#print(MeanColumn)
df['mean'] = df.mean(axis=1)
df['max'] = df.max(axis=1)
df['min'] = df.min(axis=1)
df['kurtosis'] = df.kurtosis(axis=1)
df['skew'] = df.skew(axis=1)
df['std'] = df.std(axis=1)
df = df.iloc[:,-6:]
df = pd.DataFrame(df)
print('New Data ', df)


df.to_csv('NewFile.csv')
dataset1 = pd.read_csv('NewFile.csv')
df2 = pd.DataFrame(dataset1)
print(df2)