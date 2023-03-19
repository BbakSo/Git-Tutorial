def exchange(n):
    b=n//500
    n=n%500
    c=n//100
    n=n%100
    d=n//50
    n=n%50
    e=n//10
    print('500원 동전의 개수:',b,'\n100원 동전의 개수:',
          c,'\n50원 동전의 개수:',d,'\n10원 동전의 개수:',e)
def get_integer(prompt):
    res = int(input(prompt))
    return res
a=get_integer('동전으로 교환하고자 하는 금액은?')
exchange(a)
