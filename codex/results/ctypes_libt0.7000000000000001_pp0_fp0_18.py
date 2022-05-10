import ctypes
ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)
```

# Pandas

## How to read a csv file?

```
import pandas as pd
df = pd.read_csv('file.csv')
```

## How to convert and write a dataframe to csv file?

```
df.to_csv('file.csv', index=False)
```

## How to convert and write a dataframe to json file?

```
df.to_json('file.json')
df.to_json('file.json', orient='records')
df.to_json('file.json', orient='records', lines=True)
```

## How to convert and write a dataframe to sql file?

```
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)
df.to_sql('table', con=engine)
```

## How to read a sql file and convert it to a dataframe?

``
