import Keywords as kw
import pandas as pd
df = pd.read_csv('Project Database.csv')
saved_column = df['Keyword']
saved_column = saved_column.values.tolist()

uIn = input('Enter Keyword: ')
for word in uIn.split(" "):
    if word in saved_column:
        uIn = uIn.split(',')
        index = 0
        vector = kw.keywordIn(uIn[0])
        if len(uIn)>1:
            i = 1
            while i < len(uIn):
                vector += kw.keywordIn(uIn)
        index = kw.maxVal(vector)
        kw.reward(uIn, index[0])

    else:
        print('Wrong Input')

