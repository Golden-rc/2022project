import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

df = pd.read_csv('E:\dataanalyze\stack-overflow-developer-survey-2022\survey_results_public.csv')

select =['Gender', 'OpSysPersonal use','OpSysProfessional use']  
sdf=df[select].copy()

survey_mdf =sdf[sdf.Gender=='Man']
survey_fdf =sdf[sdf.Gender=='Woman']

print(survey_mdf['OpSysPersonal use'].value_counts())
print(survey_fdf['OpSysProfessional use'].value_counts())

matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']

p=plt.subplot(2,2,1)
plt.title('个人操作系统使用（男）')
plt.pie(survey_mdf['OpSysPersonal use'].value_counts()[0:3],labels=["Windows ","Linux-based "," macOS"],autopct='%.1f%%')

p=plt.subplot(2,2,2)
plt.title('个人操作系统使用（女）')
plt.pie(survey_fdf['OpSysPersonal use'].value_counts()[0:3],labels=["Windows ","Linux-based "," macOS"],autopct='%.1f%%')

p=plt.subplot(2,2,3)
plt.title('职业操作系统使用（男）')
plt.pie(survey_mdf['OpSysProfessional use'].value_counts()[0:3],labels=["Windows ","Linux-based "," macOS"],autopct='%.1f%%')

p=plt.subplot(2,2,4)
plt.title('职业操作系统使用（女）')
plt.pie(survey_fdf['OpSysProfessional use'].value_counts()[0:3],labels=["Windows ","Linux-based "," macOS"],autopct='%.1f%%')

plt.show()

