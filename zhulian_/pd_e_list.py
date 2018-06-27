#coding:utf-8
#python3.6

import pandas as pd
import numpy as np



list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
list = []
list =list + [list1]
list = list + [list2]
print(list)

df = pd.DataFrame(list,columns=['a','b','c'])
print(df)


import datetime

print(datetime.datetime.now())

