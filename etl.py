from sqlalchemy import create_engine
conn = create_engine('postgresql://j_adolfo12_coderhouse:5W9Nsos3e4@data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com:5439/data-engineer-database')
import pandas as pd
data = {'column1':[1,2,3], 'column2':['a','b','c']}
df = pd.DataFrame(data)
df.to_sql('test3', conn, index=False, if_exists='replace')