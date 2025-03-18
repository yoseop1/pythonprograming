
import math

def get_radius(prompt) :
    r = int(input(prompt))
    return r

def get_circle_area(R) :
    s = 3.14 * R * R
    return s

input_R = "넓이를 구하고자 하는 원의 반지름은?"
r_result= get_radius(input_R)
s_result= get_circle_area(r_result)
print('반지름이', r_result, '인 원의 넓이는 = 3.14 X', r_result, 'X', r_result, '=', s_result)






