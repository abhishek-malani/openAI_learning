import os
import openai
import pandas as pd
import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import text

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

df = pd.read_csv('sales_data_sample.csv')
print(df.groupby("QTR_ID").sum()['SALES'])
temp_db = create_engine('sqlite:///:memory:', echo=True)
data = df.to_sql(name='Sales',con=temp_db)
with temp_db.connect() as conn:
    result = conn.execute(text("SELECT * FROM Sales"))
    for row in result:
        print(row)