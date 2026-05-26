def solution(nodeinfo):
    nodeinfo = [[i+1] + node for i, node in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: (-x[2], x[1]))

    answer = [[],[]]

    return answer

def _recur(node, subtree, ans1, ans2):


solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])