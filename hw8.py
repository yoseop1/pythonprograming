shopping_bag = {}

print('[구입]')

def buy(shopping_bag):
    item = input('상품명? ')
    if item == '':
        return False
    
    else:
        count = int(input('수량은? '))
        shopping_bag[item] = count
        print(f'장바구니에 {item} {count}개가 담겼습니다\n')


def show(shopping_bag):
    print(f'\n>>> 장바구니 보기: {shopping_bag}')    

def find(shopping_bag):
    while True:
        print('\n[검색]')
        n = input('장바구니에서 확인하고자 하는 상품은? ')
        if n in shopping_bag:
            print(f'{n}은(는) {shopping_bag[n]}개 담겨 있습니다.')

        else:
            print(f'{n}은(는) 장바구니에 담겨있지 않습니다.')
            break

while True:
    if buy(shopping_bag) == False:
        break

show(shopping_bag)
find(shopping_bag)

