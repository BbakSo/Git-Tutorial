def rep_char(c, n):
    print(c*n)

def draw_string(msg1):
    msg2 = 'Welcome to Seoul'
    nstr = len(msg1) if(len(msg1)>len(msg2)) else len(msg2)
    rep_char('-', nstr + 6)
    print(f'Hello {msg1},')
    print('Welcome to Seoul.')
    rep_char('-', nstr + 6)

a = draw_string(input('Input his/her name: '))
