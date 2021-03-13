import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#

def load_and_process(url_or_path_to_csv_file):
    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(['taster_name','taster_twitter_handle',
               'designation','region_2', 'description','Unnamed: 0'], axis=1)
        .dropna(axis=0)
        .groupby('variety').filter(lambda x : len(x)>100)
    )
    
    df2 = (
        df1
        .rename(columns={'country':'Country','points':'Points',
                   'price':'Price','province':'Province',
                   'region_1':'Region','title':'Name',
                   'variety':'Variety','winery':'Winery'})
        .drop_duplicates()
        .reset_index(drop = True)
    )
    return df2