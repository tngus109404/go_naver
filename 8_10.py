# #백준_14503번
# import sys
# input = lambda: sys.stdin.readline().strip()
# N,M = map(int,input().split())
# r,c,d = map(int,input().split())
# room = [list(map(int,input().split())) for _ in range(N) ]
# count = 0 # 청소한 방의 수
# dr = [-1,0,1,0]
# dc = [0,1,0,-1]
# while True:
#     if room[r][c] == 0:
#         room[r][c] = 2
#         count += 1
#     for _ in range(4): # 북동남서 순으로 살펴보기
#         d = (d+3) % 4
#         nr = r + dr[d]
#         nc = c + dc[d]
#         if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
#             r,c = nr,nc
#             break
#     else:
#         nr = r - dr[d]
#         nc = c - dc[d]
#         if 0 <= nr < N and 0 <= nc < M and room[nr][nc] != 1:
#             r,c = nr,nc
#         else:
#             break
# print(count)


# #백준_14889번
# import sys
# from itertools import combinations
# input = lambda: sys.stdin.readline().strip()
# N = int(input())
# S = [list(map(int,input().split())) for _ in range(N) ]
# result = float('inf')
# def sum_score(team):
#     score = 0
#     for i, j in combinations(team,2):
#         score += S[i-1][j-1] + S[j-1][i-1]
#     return score
# for A_tail in combinations(range(2,N+1),(N//2)-1):
#     team_A = (1,) + A_tail
#     team_B = tuple(x for x in range(1,N+1) if x not in team_A)
#     result = min(result,abs(sum_score(team_A)-sum_score(team_B)))
# print(result)


# #프로그래머스_카펫
# import math
# def solution(brown, yellow):
#     total = brown + yellow
#     for h in range(3,int(math.sqrt(total)+1)): 
#         if total % h:
#             continue
#         w = total // h
#         if (w-2) * (h-2) == yellow:
#             return[w,h]
#     return 0
# print(solution(10,2)) # [4,3]
# print(solution(8,1)) # [3,3]
# print(solution(24,24)) # [8,6]


# #프로그래머스_행렬테두리회전하기
# def solution(rows, columns, queries):
#     # 초기 행렬: 1..rows*columns
#     board = [[c + r*columns + 1 for c in range(columns)] for r in range(rows)]
#     ans = []
#     for x1, y1, x2, y2 in queries:
#         x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1  # 0-index
#         prev = board[x1+1][y1]   # 첫 교환에 들어갈 값(왼쪽 열 아랫칸)
#         minv = prev
#         # 위쪽 행: (x1, y1..y2)
#         for y in range(y1, y2 + 1):
#             board[x1][y], prev = prev, board[x1][y]
#             minv = min(minv, board[x1][y])
#         # 오른쪽 열: (x1+1..x2, y2)
#         for x in range(x1 + 1, x2 + 1):
#             board[x][y2], prev = prev, board[x][y2]
#             minv = min(minv, board[x][y2])
#         # 아래쪽 행: (x2, y2-1..y1)
#         for y in range(y2 - 1, y1 - 1, -1):
#             board[x2][y], prev = prev, board[x2][y]
#             minv = min(minv, board[x2][y])
#         # 왼쪽 열: (x2-1..x1+1, y1)
#         for x in range(x2 - 1, x1, -1):
#             board[x][y1], prev = prev, board[x][y1]
#             minv = min(minv, board[x][y1])
#         ans.append(minv)
#     return ans
# print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # [8,10,25]
# print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])) # [1,1,5,3]
# print(solution(100,97,[[1,1,100,97]])) # [1]
