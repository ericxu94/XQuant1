from WindPy import *
import datetime
import pandas as pd

def getSec_AShare(date=None):
    if date is None:
        today = datetime.datetime.now()
        date = today.strftime("%Y-%m-%d")
    w.start()
    data = w.wset("sectorconstituent", "date={0};sectorid=a001010100000000".format(date))
    result = pd.DataFrame({
        'wind_code': data.Data[1],
        'sec_name': data.Data[2]
    })
    return(result)