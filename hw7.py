#연습문제 9.4
shopping_bag = {}

print('[구입]')
while True:
    item = input('\n상품명?')
    if item == '':
        break
    else:
        num = input('수량은?')
        shopping_bag[item] = num
        print(f'장바구니에 {item} {num}개가 담겼습니다.')
print(f'>>> 장바구니 보기: {shopping_bag},')

print('\n[검색]')
search = input('장바구니에서 확인하고자하는 상품은?')
a = shopping_bag[search]
print(f'{search}은(는) {a}개 담겨있습니다.')

