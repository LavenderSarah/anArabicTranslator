import pandas as pd

df = pd.read_csv(r'Arabic.csv')

while True:
    user = input("Type in a word\n").capitalize()
    if user == "":
        print("Goodbye!")
        break
    row = df.loc[df['English'] == user]
    cell = row['Arabic'].values[0]
    
    print(cell)
