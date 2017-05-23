from utils.getSecWind import *

def getAllFinancialNumber(wind_code):
    result = []
    qtr_list = ["0331", "0630", "0930", "1231"]
    for year in range(2010,2017):
        for qtr in qtr_list:
            date = str(year) + qtr
            result = result + getIncomeSheet(wind_code, date, isQuarter=True)
    return(result)

def processNumberList(num_list):
    result = [0]*10
    for num in num_list:
        x = abs(num) + 0.000001
        first_digit = int(x // np.power(10,np.floor(np.log(x)/np.log(10))))
        result[first_digit] = result[first_digit]+1
    result = [x / len(num_list) for x in result]
    return(result)

if __name__ == "__main__":
    sec_list = getAllSec_AShare()
    base_result = [0]*10
    for i in range(1,10):
        base_result[i] = np.log(i+1) / np.log(10) - np.log(i) / np.log(10)
    print(base_result)

    result_li = []
    for ind, row in sec_list.iterrows():
        if ind > 100:
            break
        print("ind: {0}, code: {1}".format(ind, row['wind_code']))
        num_list = getAllFinancialNumber(row['wind_code'])
        result = processNumberList(num_list)

        sum = 0
        for x, y in zip(result, base_result):
            sum = sum + (x-y)*(x-y)
        result_li.append({'wind_code':row['wind_code'], 'sum':sum})

    result_df = pd.DataFrame(result_li)
    result_df.sort_values(by='sum', inplace=True)
    print(result_df.head())
    print(result_df.tail())