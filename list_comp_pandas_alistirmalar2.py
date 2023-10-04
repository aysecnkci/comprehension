
##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# RMS Titanic
# Harland and Wolff tersaneleri
# 10 Nisan 1912 Southampton
# ABD New York şehrine doğru
# 15 Nisan 1912 Buzdağına çarptığı tarih
# 52.310 ton
# 269 metre boy
# Genişlik 28 m
# Yükseklik 53 m
# Kişi kapasitesi 3547
# Filikaların top kapasitesi 1178 kişi
# Toplam kişi 2224
# 1514 kişi vefat etmiş
# 710 kişi hayatta kalmış
# Edward Smith

# of siblings/spouses aboard the Titanic - Titanic'teki kardeşlerin/eşlerin sayısı

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################
df = sns.load_dataset("titanic")
df.head()
df.shape
df.info()

#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################

df["sex"].value_counts()

df["sex"].info()


#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################

df.nunique()

#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################

# Passenger Class
# 1 = Upper Class
# 2 = Middle Class
# 3 = Lower Class
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

df["pclass"].unique()

df["pclass"].value_counts()
#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################


# Parch : the total number of the passengers' parents and children - Titanic'teki ebeveynlerin/çocukların sayısı

df[["pclass","parch"]].nunique()


#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################

# C = Cherbourg
# Q = Queenstown
# S = Southampton

df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype
df.info()

df["survived"].dtypes in [int,float]

"int" in str(df["survived"].dtypes)




#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################

df[df["embarked"]=="C"].head(10)
df.loc[(df["age"] > 50) | (df["sex"] == "male") | (df['embark_town']=="Cherbourg" )].head()


#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################

df["embarked"].unique()

df[~(df["embarked"] == "S")]["embarked"].unique()


df[~(df["embarked"] == "S")].head()
#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################

df[(df["age"]<30) & (df["sex"]=="female")].head()


#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################

df[(df["fare"] > 500 ) | (df["age"] > 70 )].head()

df["deck"].unique()
#######################################8888888888888888888888888888888888888888888888##
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################

df.isnull().sum()
df.isnull().sum().sum()
sns.heatmap(df.isnull(), cbar = False).set_title("Missing values heatmap")
plt.show(block=True)
#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################


df["who"].unique()
df["who"].value_counts()

df.drop("who", axis=1, inplace=True)
df.head()


#########################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################


type(df["deck"].mode())
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().sum()


#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################

df["age"].fillna(df["age"].median(),inplace=True)
df.isnull().sum()

fig, (axis1,axis2) = plt.subplots(1,2,figsize=(14,12))

sns.box(df,x="pclass")
plt.show()
df["pclass"].hist()
plt.show(block=True)

df["age"].hist()
plt.show(block=True)

df["fare"].hist()
plt.show(block=True)


fig, (axis1,axis2) = plt.subplots(1,2,figsize=(14,12))

sns.boxplot(x = 'age', data = df,ax=axis1)
axis1.set_title('Pclass vs Fare Survival Comparison')

sns.boxplot(x = 'fare',data = df,ax=axis2)
axis2.set_title('Pclass vs Age Survival Comparison')
plt.show(block=True)

#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################

df.groupby(["pclass","sex"]).agg({"survived": ["sum","count","mean"]})

import matplotlib.pyplot as plt
df.groupby(["pclass","sex"]).agg({"survived": ["sum","count"]}).plot(kind='bar',title='Survival Status by Passenger Class and Male/Female Passengers ')
plt.show(block=True)


fig, (axis1,axis2) = plt.subplots(1,1,figsize=(14,12))
sns.barplot(x = 'sex', y = 'survived', hue = 'pclass', data=df)
set_title('Sex vs Survived Survival Comparison')
plt.show(block=True)

sns.barplot(x = 'sex', y = 'survived', hue = 'embarked', data=df)
axis2.set_title('Sex vs Survived Survival Comparison')
axis1.set_title('Sex vs Survived Survival Comparison')


##########################################################33

g = sns.kdeplot(df["age"][(df["survived"] == 0) & (df["age"].notnull())], color="Red", shade = True)
g = sns.kdeplot(df["age"][(df["survived"] == 1) & (df["age"].notnull())], ax =g, color="Blue", shade= True)
g.set_xlabel("Age")
g.set_ylabel("Frequency")
g = g.legend(["Not Survived","Survived"])
plt.show(block=True)


#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################

def age_30(age):
    if age<30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x : age_30(x))
df.head()

df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else  0)

df["age_flag"] = df["age"].apply(lambda x: 1 if x<30 else 0)

df["age_flag"] = df["age"].apply(lambda x: 1 if x<30 else 0)


#################################################3

sns.factorplot(x="sibsp",y="survived",data=df,kind="bar", size = 6 ,
palette = "muted")
plt.show(block=True)

sns.factorplot(x="parch",y="survived",data=df,kind="bar", size = 6 ,
palette = "muted")
plt.show(block=True)

g = sns.FacetGrid(df, col='survived')
g = g.map(sns.distplot, "age")
plt.show(block=True)

g = sns.FacetGrid(df, col='survived')
g = g.map(sns.histplot, "age")
plt.show(block=True)

###########################################################3
g = sns.kdeplot(df["age"][(df["survived"] == 0) & (df["age"].notnull())], color="Red", shade = True)
g = sns.kdeplot(df["age"][(df["survived"] == 1) & (df["age"].notnull())], ax =g, color="Blue", shade= True)
g.set_xlabel("Age")
g.set_ylabel("Frequency")
g = g.legend(["Not Survived","Survived"])
plt.show(block=True)
###################################################################33
g = sns.kdeplot(df["fare"][(df["survived"] == 0) ], color="Red", shade = True)
g = sns.kdeplot(df["fare"][(df["survived"] == 1) ], ax =g, color="Blue", shade= True)
g.set_xlabel("Age")
g.set_ylabel("Frequency")
g = g.legend(["Not Survived","Survived"])
plt.show(block=True)
#########################################################################
fig, (axis1,axis2) = plt.subplots(1,2,figsize=(14,12))

sns.boxplot(x = 'pclass', y = 'fare', hue = 'survived', data = df,ax=axis1)
axis1.set_title('Pclass vs Fare Survival Comparison')

sns.boxplot(x = 'pclass', y = 'age', hue = 'survived', data = df,ax=axis2)
axis1.set_title('Pclass vs Age Survival Comparison')
plt.show(block=True)

##########################################################################


fig, qaxis = plt.subplots(1,3,figsize=(14,12))

sns.barplot(x = 'Sex', y = 'Survived', hue = 'Embarked', data=data1, ax = qaxis[0])
axis1.set_title('Sex vs Embarked Survival Comparison')

sns.barplot(x = 'Sex', y = 'Survived', hue = 'Pclass', data=data1, ax  = qaxis[1])
axis1.set_title('Sex vs Pclass Survival Comparison')

sns.barplot(x = 'Sex', y = 'Survived', hue = 'IsAlone', data=data1, ax  = qaxis[2])
axis1.set_title('Sex vs IsAlone Survival Comparison')


#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################

import seaborn as sns
df = sns.load_dataset("tips")
df.head()
df.shape

df.groupby("sex").agg({"total_bill":  ["sum","min","max","mean"]})

df.groupby("sex").agg({"tip":  ["sum","min","max","mean"]})

g = sns.lmplot(x="total_bill",y="tip",data=df);
g.fig.suptitle('Relationship b/w tip and total_bill [Scatter Plot + Regression Line]',y=1.05);
plt.show(block=True)
#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

df.groupby("time").agg({"total_bill": ["sum","min","mean","max"]})

#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

df.groupby(["day","time"]).agg({"total_bill": ["sum","min","mean","max"]})

#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################
df.head()

df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").\
agg({"total_bill": ["sum","min","max","mean"],
         "tip":  ["sum","min","max","mean"]})

#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################


df.loc[(df["size"] < 3) & (df["total_bill"] >10 ) , "total_bill"].mean()
# 17.184965034965035
df.head()
g = sns.relplot(x="total_bill",y="tip",size='size',kind='scatter',data=df);
g.fig.suptitle('total bill vs tip distinguished by table size [Scatter Plot]',y=1.05);
plt.show(block=True)



#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()



#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################

new_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]
new_df.shape

df["tip"].value_counts()
df.describe()

df["total_bill_tip_sum"].values.sort()
df.head()
df_new = df.loc[0:30,"total_bill_tip_sum"]
