import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#upload our dataset and also read our csv dataset
df=pd.read_csv("D:\\Python\\data.csv")
#use head() function
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
sns.histplot(df['expend'], bins= 12)
plt.show()
sns.pairplot(df)
plt.show()
