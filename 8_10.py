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


#프로그래머스_카펫
