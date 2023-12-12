import pyupbit
import requests

def filter_by_market_startswith_KRW(data):
    filtered_data = {key: value for key, value in data.items() if key == 'market' and value.startswith('KRW')}
    return filtered_data

#코인 목록 가져오기
url = "https://api.upbit.com/v1/market/all?isDetails=false"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)

for crypto in eval(response.text):
    res = filter_by_market_startswith_KRW(crypto)        
    print(res)










upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW"))         # 보유 현금 조회