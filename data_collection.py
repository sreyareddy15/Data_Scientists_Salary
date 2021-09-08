import glassdoor_scrapper as gs
import pandas as pd
path = "C:/Users/vishn/sreya/Data_Scientists_Salary/chromedriver.exe"
df = gs.get_jobs('data scientist',100, True, path, 10)
print(df.shape)