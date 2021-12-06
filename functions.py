import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Функция визуализации среднего курса за каждый год
def avg_rate(data,figsize=(12,5)):
    
    year = data.groupby('year',sort=False)[data.columns[4]].mean().reset_index()
    
    fig = plt.figure(figsize=figsize)
    sns.set(style='whitegrid')
    sns.set_context('talk')
    
    sns.lineplot(x='year',y=year.columns[1],data=year,color='red')
    plt.xticks(year[year.columns[0]].unique().tolist(),rotation=45)
    plt.title("Average rate for each year")
    plt.margins(x=0);
    
# Функция визуализации данных с помощью графика pairplot
def pairplot(data,height=4):
    sns.set_style("whitegrid")
    sns.set_context('talk')
    cols = data.columns[4:]

    g=sns.pairplot(data[cols],diag_kind='kde',
               kind='scatter',
               hue_order=[1,0],
               hue='appreciation',
               corner=True,height=4)
    new_labels = ['yes', 'no']
    for t, l in zip(g._legend.texts, new_labels): t.set_text(l);

# Функция визуализации данных с помощью графика violinplot        
def violin(data,figsize=(12,16)):
    l = ['year','month','weekday']
    sns.set(style='ticks')
    sns.set_context('talk')
   
    axs = []
    fig = plt.figure(figsize=figsize)
    axs.append(fig.add_subplot(3,1,1))
    axs.append(fig.add_subplot(3,1,2))
    axs.append(fig.add_subplot(3,1,3))
    
    for i in range(3):
        sns.violinplot(x=l[i],y='fluctuation',width=0.9, data=data,ax=axs[i])
        if i != 2:
            axs[i].tick_params(axis='x', rotation=45)
        axs[i].set_title(f"Fluctuations of {data.columns[4]} by {l[i]}s")
    plt.tight_layout();

# Тепловая карта корреляции всех валют
def heatmap(data):
    sns.set_context('talk')
    plt.figure(figsize=(20,18))
    sns.heatmap(data.corr(),linewidths=0.5,cmap="Blues")
    plt.title("Currencies Heat Map",fontsize=22);
        
