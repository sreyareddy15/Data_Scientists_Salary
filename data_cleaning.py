import pandas as pd
import numpy as np
df = pd.read_csv('Uncleaned_DS_jobs.csv')

# SALARY PARSING

df = df[df['Salary Estimate'] != '-1']
sal = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = sal.apply(lambda x: x.replace('K','').replace('$',''))
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)
min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))
df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

# COMPANY NAME 

''' while scrapping Company name , we also got rating along with it so eliminating that part'''
df['company_txt'] = df.apply(lambda x: x['Company Name'] if int(x['Rating']) < 0 else x['Company Name'][:-3], axis = 1)


# LOCATION

'''Just extracting State 
    and checking whether the job is in main branch or not'''
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[0])
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

# AGE - founded year

df['age'] = df['Founded'].apply(lambda x: x if x < 1 else 2021-x )


# DESCRIPTION PARSING

'''
    Keeping in the mind that we are working with data scientist role,
    I have created new columns to mention whether the jo description includes technical DS skills 
    such as Python,R,spark,aws,excel 
    Keeping in mind that different job descriptions has different formats,
    I tried to generalize it by just mentioning core words
'''
#python
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
 
#r studio 
df['R'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)

#spark 
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

#aws 
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df.to_csv('salary_data_cleaned.csv',index = False)