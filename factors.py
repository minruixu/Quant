import tushare as ts
import pandas as pd
import os
from datetime import date,timedelta

def valuation_factor(year):
    report = ts.get_report_data(year,4)
    report = report.sort_values(by = 'code',axis = 0,ascending = True)
    report = report.reset_index(drop = True)
    report.to_csv("/home/yirui/Desktop/Quant/Report/%s.csv"%year, mode="w")

    profit = ts.get_profit_data(year, 4)
    profit = profit.sort_values(by='code', axis=0, ascending=True)
    profit = profit.reset_index(drop=True)
    profit.to_csv("/home/yirui/Desktop/Quant/Profit/%s.csv"%year,mode= "w")

    operation = ts.get_operation_data(year,4)
    operation = operation.sort_values(by='code', axis=0, ascending=True)
    operation = operation.reset_index(drop=True)
    operation.to_csv("/home/yirui/Desktop/Quant/Operation/%s.csv" % year, mode="w")

    growth = ts.get_growth_data(year,4)
    growth = growth.sort_values(by='code', axis=0, ascending=True)
    growth = growth.reset_index(drop=True)
    growth.to_csv("/home/yirui/Desktop/Quant/Growth/%s.csv" % year, mode="w")

    debtpaying = ts.get_debtpaying_data(year,4)
    debtpaying = debtpaying.sort_values(by='code', axis=0, ascending=True)
    debtpaying = debtpaying.reset_index(drop=True)
    debtpaying.to_csv("/home/yirui/Desktop/Quant/Debtpaying/%s.csv" % year, mode="w")

    cashflow = ts.get_cashflow_data(year,4)
    cashflow = cashflow.sort_values(by='code', axis=0, ascending=True)
    cashflow = cashflow.reset_index(drop=True)
    cashflow.to_csv("/home/yirui/Desktop/Quant/Cashflow/%s.csv" % year, mode="w")

if __name__ == "__main__":
    pro = ts.pro_api()
    for i in range(2004,2017):
        valuation_factor(i)