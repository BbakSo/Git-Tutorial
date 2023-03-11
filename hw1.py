def get_radius() :
    r = int(input('넓이를 구하고자 하는 원의 반지름은?'))
    return r
def get_circle_area(result) :
    a = 3.14*result*result
    print('반지름', result, '인 원의 넓이 = 3.14*',result,'*',result,'=',a)
result = get_radius()
get_circle_area(result)

