import requests
import pandas as pd
from sqlalchemy import create_engine

#EXTRACT DATA API
baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'
r = requests.get(baseurl + endpoint)
data = r.json()
print




# LOAD DATA --> REDSHIFT

# conn = create_engine('postgresql://j_adolfo12_coderhouse:5W9Nsos3e4@data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com:5439/data-engineer-database')
# data = {'column1':[1,2,3], 'column2':['a','b','c']}
# df = pd.DataFrame(data)
# df.to_sql('j_adolfo12_coderhouse.jos_table2', conn, index=False, if_exists='replace')
