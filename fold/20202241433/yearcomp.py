import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('E:\dataanalyze\stack-overflow-developer-survey-2022\survey_results_public.csv')


select =['YearsCode', 'ConvertedCompYearly']  
fdf=df[select].copy()

fdf=fdf[fdf.YearsCode!='More than 50 years']
fdf=fdf[fdf.YearsCode!='Less than 1 year']
fdf=fdf.dropna(axis=0,how='any')

fdf=fdf[:200]

yc=fdf['YearsCode']
ccy=fdf['ConvertedCompYearly']

yc=np.array(yc)
ccy=np.array(ccy)

yc=yc.astype('float64')
ccy=ccy.astype('float64')

yc.sort()
ccy.sort()

print(yc)
print(ccy)

plt.scatter(yc,ccy,s=1)

plt.ylim(0,500000)

#clf=LogisticRegression(solver='liblinear')

#yc=np.array(yc).reshape(-1,1)
#ccy=np.array(ccy).reshape(-1,1)
#ccy=ccy.ravel()


#clf.fit(yc,ccy)

#plt.plot(yc,yc*clf.coef_+clf.intercept_)
plt.show()

