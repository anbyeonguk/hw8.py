shopping_bag = {}

def buy(shopping_bag):
    while True:
        item = input('상품명? ')
        if item == '':
            return False
        quantity = int(input('수량은? '))
        shopping_bag[item] = quantity
        print('장바구니에 {0} {1}개가 담겼습니다.'.format(item, quantity))

def show(shopping_bag):
    print('>>> 장바구니 보기:', shopping_bag)

def find(shopping_bag):
    print('[검색]')
    search_item = input('장바구니에서 확인하고자 하는 상품은? ')
    if search_item in shopping_bag:
        print('{0}은(는) {1}개 담겨 있습니다.'.format(search_item, shopping_bag[search_item]))
    else:
        print(f'장바구니에 {search_item}은 없습니다')
        return False

while True:
    buy(shopping_bag)
    show(shopping_bag)
    if find(shopping_bag)==False:
        break