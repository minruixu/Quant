import tushare as ts

def get_stock(file,list_status):
    stock = pro.stock_basic(exchange_id="",list_status = list_status,is_hs="")
    stock.to_csv(file,mode = "w")
    return stock

def basic_info(path,all_stock):
    #获取全部股票的量价信息
    start_date = "20050408"
    raw = all_stock.shape[0]
    for i in range(0,raw):
        print(i)
        code = all_stock.at[i,'ts_code']
        s_date = max(start_date,all_stock.at[i,'list_date'])
        t = pro.daily_basic(ts_code = code,start_date = s_date)
        t.to_csv(path+"%s.csv"%code,mode = 'w')

if __name__ == "__main__":
    pro = ts.pro_api()
    list_stock = get_stock(file = "/home/yirui/Desktop/Quant/list_stock.csv",list_status="L")
    delist_stock = get_stock(file = "/home/yirui/Desktop/Quant/delist_stock.csv",list_status="D")
    basic_info(path = "/home/yirui/Desktop/Quant/list_stocks_info/",all_stock=list_stock)
    basic_info(path="/home/yirui/Desktop/Quant/delist_stocks_info/", all_stock=delist_stock)