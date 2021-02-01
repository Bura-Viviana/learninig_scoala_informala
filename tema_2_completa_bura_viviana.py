# exrcitiul_1
my_list=[1,2,3,2.5,"abc",["a","s"]]
lenght_list=len(my_list)
index = 0
list_element = my_list[index]
sum=0
while index < lenght_list:
    list_element = my_list[index]
    index =index + 1
    print(f'{list_element}')
    #if type(list_element) == int or type(list_element)== float:
    if type(list_element) in [int, float]:
        sum=sum+list_element
print(f'the sum of numbers is {sum}')

#exercitiul_2
def recursive_function(n):
    if n == 0:
        return 0, 0, 0

    recursive_result_tuple = recursive_function(n-1)
    # # despachetare tupla in cele 3 tuple partiale - ver 1
    # partial_total_sum = recursive_result_tuple[0]
    # even_partial_sum = recursive_result_tuple[1]
    # odd_partial_sum = recursive_result_tuple[2]

    # despachetare tupla in cele 3 supe partiale - ver 2
    partial_total_sum, even_partial_sum, odd_partial_sum = recursive_result_tuple

    total_sum = n + partial_total_sum

    if n % 2 == 0:
        even_sum = even_partial_sum + n
        odd_sum = odd_partial_sum
    else:
        even_sum = even_partial_sum
        odd_sum = odd_partial_sum + n

    return total_sum, even_sum, odd_sum
all_operations = recursive_function(3)
print(all_operations)

#exercitiul_3

def read_int_no():
    ceva_citit = input('provide an input: ')
    try:
        numar = int(ceva_citit)
        print(f'am citit un numar: {numar}')
        return numar
    except:
        print(f'ai dat ceva ce nu e numar:{ceva_citit}')
        return 0

print(f'rezultatul functiei este {read_int_no()}')

