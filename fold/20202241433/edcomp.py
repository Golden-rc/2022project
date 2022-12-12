import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('E:\dataanalyze\stack-overflow-developer-survey-2022\survey_results_public.csv')
mean_values=df.groupby('EdLevel')['ConvertedCompYearly'].mean()

print(df['EdLevel'].value_counts())

plt.subplot(1,2,2)
plt.barh(mean_values.index,mean_values.values,height=0.2)

#plt.xticks(rotation=15)
plt.show()