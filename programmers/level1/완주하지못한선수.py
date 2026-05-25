def solution(participant, completion):
    answer = ''
    
    p, c = sorted(participant), sorted(completion)
    
    for i in range(len(c)):
        if p[i] != c[i]:
            answer = p[i]
            return answer
        
    answer = p[-1]
    return answer