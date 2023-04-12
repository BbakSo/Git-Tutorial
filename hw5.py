def read_single_digit(num):
    if num == 1:
        return '일'
    elif num == 2:
        return '이'
    elif num == 3:
        return '삼'
    elif num == 4:
        return '사'
    elif num == 5:
        return '오'
    elif num == 6:
        return '육'
    elif num == 7:
        return '칠'
    elif num == 8:
        return '팔'
    elif num == 9:
        return '구'
    elif num == 0:
        return '영'
    elif num == '':
        return ''


def read_number(n):
    a = n//100
    n = n % 100
    b = n // 10
    n = n % 10
    c = n
    return read_single_digit(a),read_single_digit(b),read_single_digit(c)

d = int(input('세 자리 정수 입력: '))
if 10 > d:
    print(f'{read_single_digit(d)}')
else:
    print(f'{read_number(d)}')
