import pandas as pd

from mozscape import Mozscape

client = Mozscape('my_access_id', 'my_secret_key')

dict_urls = {}

csv_file = pd.read_csv("urls.csv", header=None)
for row in csv_file:
    domainAuthority = client.urlMetrics(row[0])['pda']
    dict_urls[row[0]] = domainAuthority
        
pd.DataFrame(dict_urls,index=[0]).transpose().to_csv("DA_check_results.csv", header=False)