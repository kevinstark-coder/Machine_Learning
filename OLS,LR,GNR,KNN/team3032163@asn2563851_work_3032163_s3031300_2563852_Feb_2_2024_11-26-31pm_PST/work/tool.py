import pandas as pd
df = pd.read_csv("./Q4_test.csv")
a = df.iloc[0,:]
print(type(a))

# df.iloc[:,6] = (df.iloc[:,6] * 50).round(2)

# df.loc[1,'BloodPressure'] = 1

# for i in range((df.shape[1]-1)):
#     mean = df.iloc[:,i].mean()
#     var = df.iloc[:,i].var()
#     df.iloc[:,i] = ((df.iloc[:,i]-mean)/var*50).round(2)

# df.to_csv("./Q4_test3.csv", index = False)

# for i in range(df.shape[1]-1):
#     df.iloc[:,i] = (df.iloc[:,i]/(df.iloc[:,i].max() - df.iloc[:,i].min())*100).round(2)

# df.to_csv("./Q4_test4.csv", index = False)