# my_list= [2,1,3,5,4,7,6,9,8,0,11,12]
# lenght_list= len(my_list)

# if lenght_list % 2 == 0 and lenght_list% 4 == 0:
#     print("lista para")
#     if lenght_list % 3 == 0:
#         print ("lista e si multiplu de 3")
#     print ("a intrat pe ramura if")
# elif lenght_list % 5 == 0:
#     print("lista multiplu de 5")
# else:
#     print("lista impara")
# print("orice ar fi asta e printat")


# my_list = [2, 1, 3, 5, 4, 7, 6, 9, 8, 0, 11, 12]
# lenght_list = len(my_list)
# index = 0
# while index < lenght_list:
#     list_element = my_list[index]
#
#     if % 2 list_element == 0:
#     print(f'{list_element}este numar par')
#     else:
#         print(f'{list_element}este nr impar')
#     print("list_element ", list_element)
#     index += 1

# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care
# reprezintă
# numere întregi sau reale.
# ○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
# ○ your_function() va returna 0.
# ○ your_function(2, 4, ‘abc’, param_1=2,) va returna 6 (2 + 4).
#
# def suma_numere_din_vect():
#     my_list = [1, 2, 3, 2.5, "abc", ["a", "s"]]
#     lenght_list = len(my_list)
#     index = 0
#     list_element = my_list[index]
#     sum = 0
#     while index < lenght_list:
#         list_element = my_list[index]
#         index = index + 1
#         print(f'{list_element}')
#         # if type(list_element) == int or type(list_element)== float:
#         if type(list_element) in [int, float]:
#             sum = sum + list_element
#     print(f'the sum of numbers is {sum}')
#
#
# def functie_returneaza_suma_diferenta_si_produs(a, b):
#     suma = a + b
#     diferenta = a - b
#     produs = a * b
#     return suma, diferenta, produs


# res = functie_returneaza_suma_diferenta_si_produs(5,6)
# print(res)


# def functie_recursiva_care_calculeaza_suma_numerelor_de_la_0_la_n(n):
#     if n == 0:
#         return 0, 0, 0
#     ceva_res = functie_recursiva_care_calculeaza_suma_numerelor_de_la_0_la_n(n-1)
#     suma_partiala_toate = ceva_res[0]
#     suma_partiala_para = ceva_res[1]
#     suma_partiala_impara = ceva_res[2]
#
#     suma_toate = n + suma_partiala_toate
#     # daca param e numar par
#     if n%2 == 0:
#         suma_pare =   suma_partiala_para   + n
#         suma_impare = suma_partiala_impara
#     else:
#         suma_pare =   suma_partiala_para
#         suma_impare = suma_partiala_impara  + n
#     return suma_toate, suma_pare, suma_impare
#
# res = functie_recursiva_care_calculeaza_suma_numerelor_de_la_0_la_n(3)
# print(res)
#
# user_input=input('>')
# # user_input=int(user_input)
#    try:
# user_input=int(user_input)
# except ValueError as e:
#     print(f'{user_input}is not a number')
#     print(e)
# print('end of application')


# my_list=[1,2,3,4,5,6,7,8,9]
# for n in my_list:
#
#     if n% 2==0:
#         print(f"{n} from position {my_list.index(n)} element is even")
#     elif n% 5==0:
#         print('multiplu de 5')
#         print('asta se printeaza unde elementul este par')
#         continue
#     else:
#         print(f"{n} from position {my_list.index(n)} element is odd")
#         print('asta unde se printeaza?')
#     print('de ce se printeaza mesajul asta intr-e fiecare linie?')
# print ('asta se printeaza la finalul programului')


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_lenght = len(my_list)
# index = 0
# while index < list_lenght:
#     list_element = my_list[index]
#     if list_element % 2 == 0:
#         print(f'element {index + 1} with value {list_element} is even')
#     elif list_element % 5 == 0:
#         print(f'this is the last one. current element:{list_element}')
#         break
#     else:
#         print(f'element{index + 1} with value {list_element} is odd')
#     index += 1
# print("sa iesit inafara buclei while")


# def paranteze_doua_puncte():
#     pass


# pt ca vrem suma a soua numere o sa avem nevoie de doi parametrii: a si b


# def my_func(*args, **kwargs):
#     my_sum=0
#     for i in args :
#         my_sum+=i
#     for i in kwargs.values():
#         my_sum += i
#
#     return my_sum
#
# sum_0 = my_func()
# print(sum_0)
# first_sum = my_func(1,first=19)
# print(first_sum)
# second_sum = my_func(1,2,first=21,second=22)
# print(second_sum)
# therd_sum = my_func(1,2,3, first= 31, second= 32, therd=3)
# print(therd_sum)


def recursive_sum(n):
   if n==0:
    return 0
   return n + recursive_sum(n-1)
print(recursive_sum(5))



