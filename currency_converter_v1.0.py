"""
    作者：北辰
    功能：汇率兑换
    版本：1.0
    日期：07/06/2018
"""
#汇率
USD_VS_RBM=6.77
#人民币的输入
rmb_str_value = input('请输入人民币(CNY)金额: ')
rmb_value = eval(rmb_str_value)  #python3里面eval()函数是将字符串转换为数值
usd_value = rmb_value / USD_VS_RBM
print('美元(USD)金额是: ',usd_value)