# input = 20
#
#
# def find_prime_list_under_number(number):
#     prime_list = []
#     for n in range(2, number + 1): # n 의 범위는 2부터 number 까지
#         for i in range(2,n): # i 의 범위는 2 부터 n -1 까지
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list
#
#
# result = find_prime_list_under_number(input)
# print(result)

# input = 20
#
#
# def find_prime_list_under_number(number):
#     prime_list = []
#     for n in range(2, number + 1):
#         for i in prime_list:
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list
#
#
# result = find_prime_list_under_number(input)
# print(result)

input = 20


def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)