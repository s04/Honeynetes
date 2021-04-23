import pandas as pd
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/data/{timeframe}/")
async def read_item(timeframe: str, fsym: str = "ETH", tsym: str = "USDT", start: Optional[int]=None, end: Optional[int]=None, hours: Optional[int]=None, minutes: Optional[int]=None):
    filename = ""
    if timeframe == 'hr':
        # filename = "_".join(["Binance", fsym,tsym, "1h"]) 
        # filename += ".csv"
        filename = "Binance_" + fsym + tsym + "_1h.csv" 
    elif (timeframe == 'min'):
        # filename = "_".join(["Binance", fsym+tsym, "minute"]) 
        # filename += ".csv"
        filename = "Binance_" + fsym + tsym + "_minute.csv" 

    print(filename)
    df = pd.read_csv(filename)
    return df.head()

    
    if hours:
        print("hours")
        to = start - hours * 3600000
        result = df.loc[(df['unix'] >= to) & (df['unix'] <= start)]
        return {"data" : result.to_string()}
    elif minutes:
        to = start - minutes * 60000
        result = df.loc[(df['unix'] >= to) & (df['unix'] <= start)]
        return {"data" : result.to_string()}
    else:
        result = df.loc[(df['unix'] >= end) & (df['unix'] <= start)]
        return {"data" : result.to_string()}