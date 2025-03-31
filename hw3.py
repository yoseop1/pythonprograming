
def get_fixed_price(discount,discount_price):
    price=discount_price/(1-discount/100)
    return price


discount_rate=int(input('할인율은? : '))
A_discount_price=int(input('A 상품의 할인된 가격은? : '))
B_discount_price=int(input('B 상품의 할인된 가격은? : '))


A_fixed_price=get_fixed_price(discount_rate,A_discount_price)
B_fixed_price=get_fixed_price(discount_rate,B_discount_price)


print('A 상품의 정가는? : ',A_fixed_price,'원')
print('B 상품의 정가는? : ',B_fixed_price,'원')