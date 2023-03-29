def get_fixed_price(p):
    result=p/(100-a)*100
    return result

a=int(input('할인율은?'))
b=int(input('A상품의 할인된 가격은?'))
c=int(input('B상품의 할인된 가격은?'))
A= get_fixed_price(b)
B= get_fixed_price(c)
print('A상품의 정가는',A,'원')
print('B상품의 정가는',B,'원')
