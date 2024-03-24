# -*- coding: utf-8 -*-
# @CreateTime : 2024/3/24 14:49
# @Author : Atem
# @Email : atem.jetson@gmail.com
# @File : quiz_1
# @Project : intern_quiz
# @LastEdit : 2024/3/24

import requests
import pandas as pd

"""
通过fiddler抓包进行请求构造，结构较简单，无需使用框架
"""


def do_request(page_no: int):
    # 执行请求
    page_url = "https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    params = {"pageNo": page_no, "pageSize": 15, "bondType": 100001, "issueYear": 2023}
    response = requests.post(page_url, headers=headers, params=params, verify=False)
    resp = response.json()
    return resp
    pass


def request_logic():
    # json数据列表
    json_data_list = []
    # 爬取第1页
    resp_1 = do_request(1)
    # 解析json数据为所需格式
    for r in resp_1['data']['resultList']:
        data_dict = {"ISIN": r['isin'],
                     "Bond Code": r['bondCode'],
                     "Issuer": r["entyFullName"],
                     "Bond Type": r['bondType'],
                     "Issue Date": r["issueStartDate"],
                     "Latest Rating": r["debtRtng"]}
        json_data_list.append(data_dict)
    # 获取总页面数
    page_total = resp_1['data']['pageTotal']
    page = 2
    # 爬取后续页面
    while page <= page_total:
        resp_x = do_request(page)
        for r in resp_x['data']['resultList']:
            data_dict = {"ISIN": r['isin'],
                         "Bond Code": r['bondCode'],
                         "Issuer": r["entyFullName"],
                         "Bond Type": r['bondType'],
                         "Issue Date": r["issueStartDate"],
                         "Latest Rating": r["debtRtng"]}
            json_data_list.append(data_dict)
        page += 1
    data_df = pd.DataFrame(json_data_list)
    # 存储为csv
    data_df.to_csv("./data.csv")
    pass


# def

if __name__ == '__main__':
    request_logic()
    pass
