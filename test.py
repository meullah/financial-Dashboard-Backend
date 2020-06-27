import pandas as pd
df = pd.read_csv('data.csv',parse_dates=['SERVICE_DATE','DOB']).set_index('SERVICE_DATE')

def doctorsEarlyRecord(df,year,doc_id):
    print(df)
    temp = df.loc[df['DOC_ID']==doc_id]
    # df = df.loc[year]
    print(temp)
    df_monthly = df[['DOC_ID']].resample('M').count()
    z = df_monthly['DOC_ID'].tolist()
    
doctorsEarlyRecord(df,'2018',511)