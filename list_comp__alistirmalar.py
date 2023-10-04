##################################################
# List Comprehensions Yeni
#################################################

# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.


import seaborn as sns
import pandas as pd

# veri setinin içindeki max. sütunlar gözükmeli
pd.set_option('display.max_columns', None)

# veri setinin içindeki görüntüyü genişletme
pd.set_option('display.width',500)

df = sns.load_dataset("car_crashes")

df1 = sns.load_dataset("titanic")

df1.columns


df.head()
df.columns
df.info()


df["total"] = df["total"].dtype
df["speeding"].info()
df["alcohol"].dtype
df["not_distracted"].dtype
df["no_previous"].dtype
df["ins_premium"].dtype
df["ins_losses"].dtype
df["abbrev"].dtype

df["abbrev"]
df.columns

import numpy as np
arr1 = np.array([1.0, 2.5, 3.7, "ahmet"], dtype=object)

for col in df.columns:
    print(df[col].dtype)


# List Comprehension
["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]


# Alternative(Düz Mantık)
for col in df.columns:
    if df[col].dtype != "O":
        print("NUM_" + col.upper())
    else:
        print(col.upper())


# Function
def method(data):
    global col
    for col in data.columns:
        if data[col].dtype != "O":
            print("NUM_" + col.upper())
        else:
            print(col.upper())

method(df)

numeric_columns = [col for col in df.columns if df[col].dtype != "O"]
print(numeric_columns)

["NUM_" + col.upper() for col in numeric_columns]


# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################
#
# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#
# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']


[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

# Alternative
for col in df.columns:
    if "no" not in col:
        print(col.upper() + "_FLAG")
    else:
        print(col.upper())


    # ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################
#
og_list = ["abbrev", "no_previous"]

[col for col in df.columns if "rev" in col]

df.columns
#
# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]

# Alternative Solution
new_cols2 = [col for col in df.columns if "rev" not  in col]
new_df = df[new_cols2]
new_df.head()



# Function
def compre(data):
    new_cols = [col for col in data.columns if col not in og_list]
    new_df = data[new_cols]
    print(new_df.head())
compre(df)

##############################################################################

# BONUS

#1 Write a list comprehension that generates a list of all possible substrings of a given string.
string = "myth"
# ['m', 'my', 'myt', 'myth', 'y', 'yt', 'yth', 't', 'th', 'h']
len(string)

sub_string =[]
for i in range(len(string)):
    for j in range(i+1,len(string)+1):
       sub_string.append(string[i:j])

print(sub_string)

# List Comprehension
sub= [string[i:j]  for i in range(len(string)) for j in range(i+1,len(string)+1)]
print(sub)


#2 Write a list comprehension that flattens a nested list into a single list.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

single= []
for flat in nested_list:
    for x in flat:
        single.append(x)
print(single)

list_single= [x for flat in nested_list for x in flat]
print(list_single)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

#3 Write a list comprehension that generates a list of all possible combinations of two strings from two given lists.
list1 = ['a', 'b']
list2 = ['x', 'y']
# ['ax', 'ay', 'bx', 'by']

combination = [x+y for x in list1 for y in list2]
print(combination)

# Best Choice by Enes Akkaya - Not List Comprehension!
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = []
for i in lst:
    a += i
print(a)

#4 # Write a list comprehension that generates a list of prime numbers up to a given number n.
n = 20

def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

prime =[]
for num in range(2,n+1):
    if is_prime(num):
       prime.append(num)
print(prime)

new_prime = [num for num in range(2,n+1) if is_prime(num)]
print(new_prime)
# [2, 3, 5, 7, 11, 13, 17, 19]

#  if is_prime(num)

# Best Choice
prime_numbers = [num for num in range(2,n+1) if all(num % i != 0 for i in range(2,int(num**0.5)+1))]
print(prime_numbers)


#5 #Write a list comprehension that finds all numbers in a given list that are divisible by the sum of their digits.
numbers = [12, 23, 34, 45, 56, 67, 78, 89, 90]
# [12, 45, 90]

result=[]
for num in numbers:
    if num % sum(map(int,str(num))) == 0:
        result.append(num)
print(result)

# list comprehension
divisle_numbers = [num for num in numbers if num % sum(map(int,str(num))) == 0 ]
print(divisle_numbers)
