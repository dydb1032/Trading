import pyupbit

#API 키 발급받고 로그인
access = "UZh8xdcnBtSpCb4iTdbx1nnFI9JEQWL2q0bZvGnr"
secret = "ktAUvcETr60G5esnxbQEX2HiIMC6elflXFfYwvuG"
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW"))         # 보유 현금 조회