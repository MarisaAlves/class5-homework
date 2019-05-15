import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

diabetes = pd.read_csv(filepath_or_buffer='diabetes.data', sep ='\t', header=0)
print(diabetes.describe().to_string())

os.makedirs('plots', exist_ok=True)


diab_columns = list(diabetes)
for i in diab_columns:
    plt.hist(diabetes[i], bins=10, color = 'g')
    plt.title(i)
    plt.xlabel(i)
    plt.ylabel('Count')
    plt.savefig(f'plots/hist'+str(i)+'.png', format='png')
    plt.clf()

for i in diab_columns:
    for j in diab_columns:
        if diab_columns.index(i) < diab_columns.index(j):
            plt.scatter(diabetes[i], diabetes[j], color='b')
            plt.title(str(i)+' to '+str(j))
            plt.xlabel(i)
            plt.ylabel(j)
            plt.savefig(f'plots/'+str(i)+'_to_'+str(j)+'.png', format='png')

#Advanced section of homework
#the diabetes dataset already comes with the columns headers as part of the data
#But the code to manually add in column headers would be as follows:

diabetes.columns = ['AGE', 'SEX', 'BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'Y']


#Reach section of homework
#Plotting a correlogram
plt.figure(figsize=(12, 10), dpi=80)
sns.heatmap(diabetes.corr(), xticklabels=diabetes.corr().columns, yticklabels=diabetes.corr().columns, cmap='RdYlGn', center=0, annot=True)
plt.title('Correlogram of diabetes', fontsize=22)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig(f'plots/correlogram_diabetes.png', format='png')