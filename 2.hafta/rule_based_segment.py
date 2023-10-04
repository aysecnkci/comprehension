
# EDA for Titanic Dataset



import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

df.head()

df.columns

df["embarked"].unique()


sns.boxplot(x=df["age"])
plt.show(block=True)



df.describe().T


df[df["embarked"] == "S"].head(20)

