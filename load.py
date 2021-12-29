import pandas as pd

df  = pd.read_csv('data.csv',index_col=0)
df1 = pd.read_csv('data.csv')

elements = df1['Element'].values.tolist()
types = sorted(list(set(df1['Type'].values.tolist())))

def read(element: str):
    data = df.loc[element]
    return data

main_layout = [['x' ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,'x'],
               ['x' ,'x' ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,'x' ,'x' ,'x' ,'x' ,'x' ,'x'],
               ['x' ,'x' ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,''  ,'x' ,'x' ,'x' ,'x' ,'x' ,'x'],
               ['x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x'],
               ['x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x'],
               ['x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x'],
               ['x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x']]

sec_layout  = [['x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x'],
               ['x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x' ,'x']]

color_dict = {'Nonmetal':'#feaa91',
    'Noble Gas':'#ffe36b',
    'Halogen':'#dadf23',
    'Alkali Metal':'#fee0b3',
    'Alkaline Earth Metal':'#fdc721',
    'Metalloid':'#e79cf4',
    'Transition Metal':'#77c3f6',
    'Metal':'#ff9fc2',
    'Lanthanide':'#39d8ab',
    'Actinide':'#abdf4b',
    'Unknown Properties':'#b2b3b2'}
