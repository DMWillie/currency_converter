"""
    作者：北辰
    功能：汇率兑换
    版本：4.0
    日期：08/06/2018
    2.0新增功能:根据输入判断是人民币还是美元，进行相应的转换计算
    3.0新增功能:程序可以一直运行，直到用户退出
    4.0新增功能:将汇率兑换功能封装到函数当中
"""

def convert_currency(im,er):
    """
    汇率兑换函数
    """
    out=im*er
    return out

#汇率
USD_VS_RBM=6.77
#带单位的货币输入
currency_str_value = input('请输入带单位的货币金额: ')
# 获取货币单位
unit = currency_str_value[-3:]
if unit == 'CNY':
    exchange_rate = 1 / USD_VS_RBM
elif unit == 'USD':
    exchange_rate = USD_VS_RBM
else:
    exchange_rate = -1
if exchange_rate != -1:
    in_money = eval(currency_str_value[:-3])
    # 调用函数
    out_money = convert_currency(in_money, exchange_rate)
    print('兑换后的金额: ', out_money)
else:
    print('该版本尚不支持该种货币!')
