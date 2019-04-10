# _*_coding:utf-8_*_
import csv
import json
import requests

# 该程序获得从2018年1月2日至今的交易排名数据

# 文件初始化，写入表头
# 当日交易数据，kx.csv

with open('kx.csv', 'w') as f:
    f.write('日期,期货名称,交割月份,前结算,今开盘,最高价,最低价,收盘价,结算参考价,涨跌1,涨跌2,成交手,持仓手数,增减量' + '\n')

# 2019A.csv里是2018年至今的交易日历
ymd = csv.reader(open("2019A.csv"))

for row in ymd:

    # 输出的每一行是一个list,list中的每一个元素转换成了string类型
    aaa = str(row[0:1])
    # 取日期部分
    aaa = aaa[2:10]
    url_a = "http://www.shfe.com.cn/data/dailydata/kx/kx"
    print(aaa)
    # 拼接成下载json数据的地址，每个地址代表一天
    url1 = url_a + aaa + ".dat"
    print(url1)

    data0 = url1[43:51]
    # 反爬虫
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    }

    jsonbj1 = json.loads(requests.get(url1, headers=headers).text)

    for i4 in jsonbj1['o_curinstrument']:

        # content = {}
        # content['日期'] = data0
        # content['期货名称'] = i4['PRODUCTID']
        # content['PRODUCTSORTNO'] = i4['PRODUCTSORTNO']
        # content['期货名称'] = i4['PRODUCTNAME']
        # content['交割月份'] = i4['DELIVERYMONTH']
        #
        # content['前结算'] = str(i4['PRESETTLEMENTPRICE'])
        # content['今开盘'] = str(i4['OPENPRICE'])
        # content['最高价'] = str(i4['HIGHESTPRICE'])
        # content['最低价'] = str(i4['LOWESTPRICE'])
        #
        # content['收盘价'] = str(i4['CLOSEPRICE'])
        # content['结算参考价'] = str(i4['SETTLEMENTPRICE'])
        # content['涨跌1'] = str(i4['ZD1_CHG'])
        # content['涨跌2'] = str(i4['ZD2_CHG'])
        #
        # content['成交手'] = str(i4['VOLUME'])
        # content['持仓手数'] = str(i4['OPENINTEREST'])
        # content['增减量'] = str(i4['OPENINTERESTCHG'])
        # content['持仓手数1'] = str(i4['ORDERNO'])
        # content['增减量1'] = str(i4['ORDERNO2'])a
        #
        # print(data0, i4['PRODUCTID'], i4['PRODUCTSORTNO'], i4['PRODUCTNAME'], i4['DELIVERYMONTH'],
        #       i4['PRESETTLEMENTPRICE'],
        #       i4['OPENPRICE'], i4['HIGHESTPRICE'], i4['LOWESTPRICE'], i4['CLOSEPRICE'], i4['SETTLEMENTPRICE'],
        #       i4['ZD1_CHG'], i4['ZD2_CHG'], i4['VOLUME'], i4['OPENINTEREST'], i4['OPENINTERESTCHG'], i4['ORDERNO'],
        #       i4['ORDERNO2'])

        with open('kx.csv', 'a') as f:
            f.write(
                data0 + ',' + i4['PRODUCTID'] + ',' + i4['DELIVERYMONTH'] + ',' + str(
                    i4['PRESETTLEMENTPRICE']) + ',' + str(i4['OPENPRICE']) + ',' + str(i4['HIGHESTPRICE']) + ',' + str(
                    i4['LOWESTPRICE']) + ',' + str(i4['CLOSEPRICE']) + ',' + str(i4['SETTLEMENTPRICE']) + ',' + str(
                    i4['ZD1_CHG']) + ',' + str(i4['ZD2_CHG']) + ',' + str(i4['VOLUME']) + ',' + str(
                    i4['OPENINTEREST']) + ',' + str(i4['OPENINTERESTCHG']) + '\n')
