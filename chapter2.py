import os
import openai
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

df = pd.read_csv('sales_data_sample.csv')
print(df)