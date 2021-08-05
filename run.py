import pandas as pd

dataset = pd.read_csv('dataset_ZakirTestZ1.csv')
df = pd.DataFrame(dataset)
df.drop(df.iloc[:, 1200:1275], inplace = True, axis = 1)
mean = df.mean(axis=1)
data_new = df.fillna(mean)
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
