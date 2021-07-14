import re
import json
from getcsv import Getcsv


class UniqueVis:

    def __init__(self, jsonfile_path):
        self.jsonfile_path = jsonfile_path

    def get_unique_visits(self):
        zim_data = []
        
        with open(self.jsonfile_path) as readjson:
            data = json.load(readjson)
            subtables = data[0]['subtable']
            for subtable in subtables:
                for k, v in subtable.items():
                    if k == "url" and v.endswith("zim.torrent"):
                        zim_data.append(subtable)
        
        self.calculate_popularity(zim_data)

    def calculate_popularity(self, zim_download_data):

        score_list, zim_list = [], []
        regex = '(?:_\d{4}-\d{2})'
        max_visits = zim_download_data[0]['nb_uniq_visitors']

        for i in range(len(zim_download_data)):
            url = zim_download_data[i]['url'].split('/')[-1]
            zim = re.split(regex, url)[0]
            score_list.append(float(zim_download_data[i]['nb_uniq_visitors']/max_visits)*100)
            zim_list.append(zim)
        
        zim_dict = {
                "Score": score_list,
                "Zim": zim_list
                }
        get_csv = Getcsv(zim_dict)

        if get_csv.add_rank():
            return "CSV File created"




if __name__ == "__main__":
    obj = UniqueVis("download_kiwix_org.json")
    obj.get_unique_visits()
