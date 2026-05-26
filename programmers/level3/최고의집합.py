def solution(n, s):
    if s<n: return [-1]

    q = s % n 
    p = (s-q) / n
    
    answer = [p] * n 
    
    for i in range(n):
        if q > 0:
            answer[n-1-i] += 1
            q -= 1
    return answer
    
    
#s를 n으로 나눠서 몫 r과 나머지 q가 있을 때 숫자 (r+1)이 q개, r이 n-q개 있는 집합이 곱을 최대로 합니다.