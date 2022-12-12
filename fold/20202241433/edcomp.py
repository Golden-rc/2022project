import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('E:\dataanalyze\stack-overflow-developer-survey-2022\survey_results_public.csv')
mean_values=df.groupby('EdLevel')['ConvertedCompYearly'].mean()

print(df['EdLevel'].value_counts())

plt.bar(mean_values.index,mean_values.values,width=0.2)
plt.show()