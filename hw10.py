#연습문제 12.2
import os
filename = 'scores.txt'
def input_scores():
    scores = []
    i = 1
    while (True):
        n = int(input(f'#{i}? '))
        if n<0:
            break
        scores.append(n)
        i += 1
    return scores

def get_average(scores):
    total = 0
    for n in scores:
        total += n
    return total / len(scores)

def show_scores(scores):
    for n in scores:
        print(n, end=' ')
    print()
    
def save_data(scores, filepath):
    with open(filepath, 'w', encoding='utf8') as file:
        for item in scores:
            file.write(f'{item}\n')
            
def load_data(filepath):
    lines = []
    with open(filepath, 'r', encoding='utf8') as file:
        for line in file:
            lines.append(int(line.strip()))
        return lines
#주 프로그램    
if os.path.exists(filename):
    print('[파일 읽기]')
    scores = load_data(filename)
    print('\n[점수 출력]')
    print('개인 점수:', end='')
    show_scores(scores)
    avg = get_average(scores)
    print(f'평균: {avg:.1f}')
else:
    print('[점수 입력]')
    scores = input_scores()
    print('\n[점수 출력]')
    print('개인 점수:', end='')
    show_scores(scores)
    avg = get_average(scores)
    print(f'평균: {avg:.1f}')

save_data(scores, filename)
