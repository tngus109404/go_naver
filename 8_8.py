# #백준_1920번
# import sys
# input = lambda: sys.stdin.readline().strip()
# N = int(input())
# A = sorted(list(map(int,input().split())))
# M = int(input())
# B = list(map(int,input().split()))
# for target in B:
#     l = 0
#     r = N-1
#     while l <= r:
#         mid = (l+r)//2
#         if target == A[mid]:
#             print(1)
#             break
#         elif target < A[mid]:
#             r = mid - 1
#         else:
#             l = mid + 1
#     else:
#         print(0)


# #백준_10816번
# import sys
# import bisect
# input = lambda: sys.stdin.readline().strip()
# N = int(input())
# A = sorted(list(map(int,input().split())))
# M = int(input())
# B = list(map(int,input().split()))
# out=[]
# for r in B:
#     left = bisect.bisect_left(A,r)
#     right = bisect.bisect_right(A,r)
#     out.append(str(right-left))
# print(' '.join(out))


# #백준_2805번
# import sys
# input = lambda: sys.stdin.readline().strip()
# N,M = map(int,input().split())
# trees = sorted(list(map(int,input().split())))
# low, high = 0, trees[-1]
# answer = 0
# while low <= high:
#     mid = (low+high)//2
#     total = sum(t-mid for t in trees if t > mid)
#     if total >= M:
#         answer = mid
#         low = mid+1
#     else:
#         high = mid-1
# print(answer)


# #프로그래머스_입국심사
# def solution(n, times):
#     if len(times)==1:
#         return times[0]*n
#     low,high = 1,max(times)*n
#     answer = high
#     while low <= high:
#         mid = (low+high)//2
#         result = sum( mid//t for t in times)
#         if result >= n:
#             answer = mid
#             high = mid-1
#         else:
#             low = mid+1
#     return answer
# print(solution(6,[7,10])) # 28


# #프로그래머스_예산
# def solution(d, budget):
#     answer = 0
#     sorted_list = sorted(d)
#     prefix = [0]
#     for v in sorted_list:
#         prefix.append(prefix[-1] + v)
#     low, high = 0, len(sorted_list)
#     while low <= high:
#         mid = (low + high) // 2
#         result = prefix[mid]
#         if result > budget:
#             high = mid - 1
#         else:
#             answer = mid
#             low = mid + 1
#     return answer
# print(solution([1,3,2,5,4],9)) # 3
# print(solution([2,2,3,3],10)) # 4


# #백준_1806번(부분합)
# import sys
# input = lambda: sys.stdin.readline().strip()
# N,S = map(int,input().split())
# A = list(map(int,input().split()))
# left,total = 0,0
# ans = N+1
# for right in range(N):
#     total += A[right]
#     while total >= S:
#         ans = min(ans, right-left+1)
#         total-=A[left]
#         left+=1
# print(ans if ans <= N else 0)


# #백준_3273번(두수의합)
# import sys
# input = lambda: sys.stdin.readline().strip()
# N = int(input())
# A = sorted(map(int,input().split()))
# X = int(input())
# left, right = 0,N-1
# answer = 0
# while left<right:
#     cur_sum = A[left]+A[right]
#     if cur_sum > X:
#         right -= 1
#     elif cur_sum < X:
#         left += 1
#     else:
#         answer += 1
#         left += 1
#         right -= 1
# print(answer)
