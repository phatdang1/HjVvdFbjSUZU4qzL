import pandas as pd
from similarity_metric import vectorizerNCosineSim
import re
import seaborn as sns
import matplotlib.pyplot as plt


# candidate class includes candidate's information
class candidates:
    def __init__(self, id, job_title, location, connections):
        self.id = id
        self.job_title = job_title
        self.location = location
        self.connections = connections
        self.fit = 0
    
    # get similar score of candidate with keyword
    def get_sim_score(self, keyword):
        return vectorizerNCosineSim(self.job_title, keyword)

def read_n_processing_data(filename, keyword, analyze):
    # open file
    data = pd.read_csv(filename)
    # if analyze is true run the analysis on data
    if(analyze):
        eda_analysis(filename)

    # add candidate into dictionnary with the probability to fit the job's description
    candidate_data = {}
    for i in range(0,len(data)):
        line = data.iloc[i]
        # initialize candidate object, cleaning connections to have only digit
        cand = candidates(line.id, line.job_title, line.location, int(re.sub("\D","",line.connection)))
        cand.fit = vectorizerNCosineSim(cand.job_title, keyword)
        candidate_data[line.id] = cand
    return candidate_data

def eda_analysis(filename):
    # open file
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
