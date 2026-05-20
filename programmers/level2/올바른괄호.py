# 문제: 프로그래머스 - 올바른 괄호
# 분류: 스택/큐
# 풀이 시간: 20분
# 핵심 아이디어: 여는 괄호면 push, 닫는 괄호면 pop

def solution(s):
    answer = False
    stack = []
    
    for data in s:
        if len(stack) == 0:
            if data == ')':
                return answer
            stack.append(data)
        else:
            if data == ')':
                stack.pop()
            else:
                stack.append(data)
    if len(stack) == 0:
        answer = True
    return answer