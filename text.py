import pandas as pd
data = {'이름' : ['서준','우현','인아'], '수학' : [90,80,70], '영어' : [98,89,95], '음악' : [85,95,100], '체육' : [100,90,90]}
df = pd.DataFrame(data)
print(df.loc[0,'영어'])