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

    # print(f'returnez res partial partiala suma_tot={total_sum}, suma_para={even_sum}, suma_impare={odd_sum}')
    return total_sum, even_sum, odd_sum

all_operations = recursive_function(3)
print(all_operations)
