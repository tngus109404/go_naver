# #백준_1697번
# from collections import deque
# import sys
# input = lambda: sys.stdin.readline().strip()
# N,K = map(int,input().split())
# MAX = 100000
# queue = deque()
# dist = [-1] * (MAX+1)
# dist[N] = 0
# queue.append(N)
# while queue:
#     x = queue.popleft()
#     if x == K:
#         print(dist[x])
#         break
#     nx = x - 1
#     if nx >= 0 and dist[nx] == -1:
#         dist[nx] = dist[x] + 1
#         queue.append(nx)
#     nx = x + 1
#     if nx <= MAX and dist[nx] == -1:
#         dist[nx] = dist[x] + 1
#         queue.append(nx)
#     nx = x * 2 
#     if nx <= MAX and dist[nx] == -1:
#         dist[nx] = dist[x] + 1
#         queue.append(nx)


# #백준_7576번
# import sys
# from collections import deque
# input = lambda: sys.stdin.readline().strip()

# M,N = map(int,input().split())
# g = [list(map(int,input().split())) for _ in range(N)]

# q = deque()
# unripe = 0
# dirs = [(-1,0),(1,0),(0,-1),(0,1)]
# last = 1

# for x in range(N):
#     for y in range(M):
#         if g[x][y] == 1:
#             q.append((x,y))
#         elif g[x][y] == 0:
#             unripe += 1
# if unripe == 0:
#     print(0)
#     sys.exit(0)
# while q:
#     x,y = q.popleft()
#     cur = g[x][y]
#     for dx, dy in dirs:
#         nx,ny = x+dx,y+dy
#         if 0<=nx<N and 0<=ny<M and g[nx][ny] == 0:
#             g[nx][ny] = cur + 1
#             last = g[nx][ny]
#             unripe -= 1
#             q.append((nx,ny))
# print(last-1 if unripe == 0 else -1)


# #백준_1026번
# import sys
# input = lambda: sys.stdin.readline().strip()
# N = int(input())
# A = sorted(map(int,input().split()))
# B = list(map(int,input().split()))
# order = sorted(range(N), key= lambda i : B[i], reverse=True)
# assigned = [0] * N
# for i,v in enumerate(order):
#     assigned[v] = A[i]
# print(sum(assigned[q]*B[q] for q in range(N)))


# # 프로그래머스_가장큰수
# from functools import cmp_to_key
# def solution(numbers):
#     answer = ''
#     s = list(map(str,numbers))
#     def cmp(a,b):
#         ab, ba = a + b, b + a
#         if ab>ba:
#             return -1
#         if ab<ba:
#             return 1
#         return 0
#     s.sort(key=cmp_to_key(cmp))
#     answer = ''.join(s)
#     return '0' if answer[0] == '0' else answer
# print(solution([6, 10, 2])) # "6210"
# print(solution([3, 30, 34, 5, 9])) # "9534330""


# # 프로그래머스_스킬트리
# from collections import deque
# def solution(skill, skill_trees):
#     count = len(skill_trees)
#     for combo in skill_trees:
#         q = deque(skill)
#         s = q.popleft()
#         for ch in combo:
#             if ch == s:
#                 if q:
#                     s = q.popleft()
#             elif ch in q:
#                 count -= 1
#                 break
#     return count
# print(solution("CBD"	,["BACDE", "CBADF", "AECB", "BDA"])) # 2


# # 프로그래머스_네트워크
# def solution(n, computers):
#     visited = [False] * n
#     def dfs(u):
#         visited[u] = True
#         for v in range(n):
#             if not visited[v] and computers[u][v] == 1:
#                 dfs(v)
#     answer = 0
#     for u in range(n):
#         if not visited[u]:
#             dfs(u)
#             answer+=1
#     return answer
# print(solution(3	,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
# print(solution(3	,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1