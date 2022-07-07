import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# EDA 

def eda_analysis(filename):
    # read csv file
    df = pd.read_csv(filename)

    # take a glance at the first 10 rows of data
    print(df.head(10))

    # shape of data 
    print('Shape of data (in (row:column) format): ',df.shape)

    # describe data
    print(df.describe())

    # get data information like data type, null value found
    print(df.info())

    # display connection graph
    sns.histplot(x='connection', data=df)
    plt.show()

eda_analysis('data/potential-talents - Aspiring human resources - seeking human resources.csv')