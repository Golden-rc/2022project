import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from scipy import stats

df = pd.read_csv('E:\dataanalyze\stack-overflow-developer-survey-2022\survey_results_public.csv')


select =['YearsCode', 'ConvertedCompYearly']  
fdf=df[select].copy()

fdf=fdf[fdf.YearsCode!='More than 50 years']
fdf=fdf[fdf.YearsCode!='Less than 1 year']
fdf=fdf.dropna(axis=0,how='any')

#fdf=fdf[:200]

yc=fdf['YearsCode']
ccy=fdf['ConvertedCompYearly']

yc=np.array(yc)
ccy=np.array(ccy)

yc=yc.astype('float64')
ccy=ccy.astype('float64')

combine=[yc,ccy]
combine=np.array(combine)

combine=(combine.T)[np.lexsort(combine[::-1,:])].T

yc=combine[0]
ccy=combine[1]

plt.scatter(yc,ccy,s=1)

plt.ylim(0,1000000)

i=0
for p in yc:
    if(yc[i]<29):
        i+=1


slope,intercept,r_value,p_value,std_err=stats.linregress(yc,ccy)

plt.plot(yc,slope*yc+intercept,'r')

plt.show()

print(slope,intercept)

