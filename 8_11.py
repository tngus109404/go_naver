# #백준_1316번
# import sys
# input = lambda: sys.stdin.readline().strip()
# N = int(input())
# count = 0
# for _ in range(N):
#     s = input()
#     seen = set()
#     prev = False
#     ok = True
#     for ch in s:
#         if ch != prev: # 이어진문자가 아니면 실행함
#             if ch in seen: # 사용된적 있음
#                 ok = False # 그룹문자 아님 판정
#                 break
#             seen.add(ch) # 사용된적 없음
#             prev = ch
#     if ok:
#         count += 1
# print(count)


# #백준_2941번
# import sys
# input = lambda: sys.stdin.readline().strip()
# N = input()
# two = set(['c=','c-','d-','lj','nj','s=','z='])
# i = 0
# count = 0
# while i < len(N):
#     if i + 2 < len(N) and N[i:i+3] == 'dz=':
#         count += 1
#         i+=3
#     elif i + 1 < len(N) and N[i:i+2] in two:
#         count +=1
#         i+=2
#     else:
#         count +=1
#         i+=1
# print(count)


# #백준_1541번
# import sys
# input = lambda: sys.stdin.readline().strip()
# N = input()
# num=0
# total = 0
# minus  = False
# for ch in N + '$':
#     if ch.isdigit():
#         num = num*10 + int(ch)
#     else:
#         total = total + num if not minus else total - num
#         num = 0
#         if ch == '-':
#             minus = True
# print(total)


# #프로그래머스_문자열압축
# def solution(s):
#     n = len(s)
#     best = n
#     for i in range(1,(n//2)+1):
#         prev = s[:i]
#         count = 1
#         res=''
#         for j in range(i,n,i):
#             if prev == s[j:j+i]:
#                 count += 1
#             else:
#                 res += (str(count) if count > 1 else '') + prev
#                 prev = s[j:j+i]
#                 count = 1
#         res += (str(count) if count > 1 else '') + prev
#         best = min(best,len(res))
#     return best
# print(solution("aabbaccc")) # 7
# print(solution("ababcdcdababcdcd")) # 9
# print(solution("abcabcdede")) # 8
# print(solution("abcabcabcabcdededededede")) # 14
# print(solution("xababcdcdababcdcd")) # 17


# #프로그래머스_괄호변환
# def solution(p):
#     if p == "":
#         return p
#     def divide(strings):
#         open_sign = 0
#         close_sign = 0
#         u = ''
#         v = ''
#         for_u = True
#         for sign in strings:
#             if sign == '(':
#                 open_sign += 1
#             else:
#                 close_sign +=1
#             if for_u:
#                 u += sign
#                 if open_sign == close_sign:
#                     for_u = False
#             else:
#                 v += sign
#         return u,v
#     def check(strings):
#         sign_count = 0
#         result = 0
#         for sign in strings:
#             if sign == '(':
#                 sign_count += 1
#             else:
#                 sign_count -= 1
#             if sign_count < 0:
#                 return sign_count == 0
#         return True
#     def other_side(string):
#         result = ''
#         for ch in string:
#             if ch =='(':
#                 nc = ')'
#             else:
#                 nc = '(' 
#             result += nc
#         return result
#     def func(u,v):
#         if check(u):
#             r = solution(v)
#             return u+r
#         else:
#             new_result='('
#             r = solution(v)
#             new_result = new_result + r + ')'
#             u = u[1:-1]
#             u = other_side(u)
#             return new_result + u
#     u,v = divide(p)
#     return func(u,v)
# print(solution("(()())()")) # "(()())()"
# print(solution(")("	)) # "()""
# print(solution("()))((()")) # "()(())()"


# #프로그래머스_전화번호목록
# def solution(phone_book):
#     phone_book.sort()
#     for a, b in zip(phone_book, phone_book[1:]):
#         if b.startswith(a):   # a가 b의 접두어면 실패 (동일 번호도 접두어 취급)
#             return False
#     return True
# print(solution(["119", "97674223", "1195524421"]	)) # false
# print(solution(["123","456","789"]	)) # true
# print(solution(["12","123","1235","567","88"]	)) # false
