#연습문제 10.6
def buy(shopping_bag):
    print('[구입]')
    item = input('\n상품명?')
    num = input('수량은?')
    shopping_bag[item] = num
    print(f'장바구니에 {item} {num}개가 담겼습니다.')
    return item

def show():
    print(f'>>> 장바구니 보기: {shopping_bag},')

def find():
    print('\n[검색]')
search = input('장바구니에서 확인하고자하는 상품은?')
a = shopping_bag[search]
if a != None:
    print(f'{search}은(는) {a}개 담겨있습니다.')
else:
    print(f'장바구니에 {search}은(는) 없습니다.')


shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
