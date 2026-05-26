def hanoi(s, m, e, n):
    if n == 0:
        return []
    return hanoi(s, e, m, n-1) + [[s,e]] + hanoi(m, s, e, n-1)
    

def solution(n):
    return hanoi(1, 2, 3, n)
        
    
        