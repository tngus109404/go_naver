#백준_1260
from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()
def dfs(graph, v, visited):
    visited[v]=True
    print(v,end=" ")
    for neighbor in sorted(graph[v]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)
def bfs(graph, start):
    visited = [False] * (len(graph))
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for neighbor in sorted(graph[v]):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor]=True
n,m,start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (n+1)
dfs(graph, start, visited)
print()
bfs(graph,start)


#백준_2606
from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()
def bfs(graph, start):
    count = 0
    queue = deque([start])
    visited[start]=True
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor]=True
                count += 1
    return count
N = int(input()) # number of computer
M = int(input()) # number of network
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (N+1)
print(bfs(graph,1))


#백준_2178번
from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == M-1:
            return graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))   
    return -1
N,M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
print(bfs(0,0))


#프로그래머스_타겟넘버
def solution(numbers, target):
    answer = 0
    def dfs(index,total):
        nonlocal answer
        if index == len(numbers):
            if total == target:
                answer += 1
            return
        dfs(index+1, total + numbers[index])
        dfs(index+1, total - numbers[index])
    dfs(0,0)
    return answer
print(solution([1,1,1,1,1], 3)) # 5
print(solution([4,1,2,1],4)) # 2

#프로그래머스_게임맵최단거리
from collections import deque
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        while queue:
            x,y = queue.popleft()
            if x == N - 1 and y == M - 1:
                return maps[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny))
    answer = bfs(0,0)
    return answer if answer is not None else -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))#11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))#-1
	