'''
Created on May 30, 2013

@author: bhsingh
'''
import requests
import csv
from re import search
class GoogleSearch():
    '''
    makes a custom google search and formats the output
    '''
    
    def customSearch(self, parameters, outFile):
        """ 
        makes a custom search  google search
        """
        resultFile = open(outFile, 'wb')
        wr = csv.writer(resultFile, dialect='excel', delimiter='\t')
        for i in range(0, 10):
            startIndex = i * 10 + 1
            parameters['startIndex'] = startIndex
            r = requests.get('https://www.googleapis.com/customsearch/v1', params=parameters)
            response = r.json()
            for items in response['items']:
                print(items)
                out = [items['link'], items['displayLink'], items['title'],  items['snippet'], items['formattedUrl']]
                wr.writerow(out)
                
        
if __name__ == "__main__":
    p = GoogleSearch()
    payload = {"key":"AIzaSyBtyyRS0_UtmPcXZ1d_mTdTNH0lNEbRO24", "cx":"014352858120178105224:xvlai4qpbzc", "q":"+('Actos' OR 'Pioglitazone' OR 'Glustin' OR 'Glizone' OR 'Pioz' OR 'Zactos') AND ('myocardial infarction' OR 'acute myocardial infarction' OR 'heart attack' OR 'stroke' OR 'heart failure')", "alt":"json"}
    p.customSearch(payload, "/Users/bhsingh/Desktop/actos-output.tsv")