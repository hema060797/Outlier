import pandas as pd
import numpy as np
import seaborn as sns
dataset=[10,11,12,13,14,15,12,13,112,10,13,12,14,108,12,11,14,13,15,10,12,15,18,17]
print(dataset)
outliers=[]
print('USING Z SCORE')
def detect_outliers(data):
    threshold=3
    mean=np.mean(data)
    std=np.std(data)
    
    for i in dataset:
        z_score=(i-mean)/std
        if np.abs(z_score)>threshold:
            outliers.append(i)
    return outliers
outliers_pt=detect_outliers(dataset)
print(outliers_pt)

#IQR
sorteddataset=sorted(dataset)
print(sorteddataset)
quantile1,quantile3=np.percentile(dataset,[25,75])
print(quantile1,quantile3)


#finding IQR
iqr_value=quantile3-quantile1
print(iqr_value)

#find the upper and lower bound value
lower_bound_val=quantile1-(1.5*iqr_value)
upper_bound_val=quantile3-(1.5*iqr_value)
print(lower_bound_val,upper_bound_val)
