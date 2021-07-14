import csv
import pandas as pd
import numpy as np

class Getcsv:

    def __init__(self, zim_stats):
        self.zim_stats = zim_stats

    def add_rank(self):

       df = pd.DataFrame(data=self.zim_stats)
       df['Score'] = df['Score'].apply(np.int64)
       df['Rank'] = (df['Score'].rank(pct=True))*100
       df['Rank'] = df['Rank'].apply(np.int64)

       first_column = df.pop('Rank')
       df.insert(0, 'Rank', first_column)
       print(df.sort_values(by=['Score'], ascending=False))
       return df.to_csv('popularity_computation.csv', index=False)



if __name__ == "__main__":

    obj = Getcsv({"Score":[100,66,34,34,89,54],"Zim":["free","values","to","check","some","stats"]})
    obj.add_rank()
    #obj.insert_csv()


