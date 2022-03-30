def has_two_digit(number: str) -> bool:
    return len(number) == 2

def get_unit_and_ten(number: str):
    return int(number[0]), int(number[1])

def padding(mx, mn, number):
    """Inserting leading zeros, this function can be used to set all numbers with the same size of max.

    Args:
        mx (int): max length
        mn (int): min length
        number (str): the number with the same size of the mx with leading zeros. But
        if they have the same size, no zero is required.

    Returns:
        str: number with leading zeros (if required) 
    """
    return (mx - mn) * "0" + number  

def get_a1_a2_a3(number: str) -> str:
    """This functions breaks the number into three distinct parts
        e.g., 
        if number = 1234  or  12345  or  12345678
                   1|2|34    1|2|345    12|34|5678
    Args:
        number (str): the number to be divided

    Returns:
        str: three partitions
    """
    sep = len(number) // 3
    return number[:sep], number[sep:2*sep], number[2*sep:]

def get_lengths(n1: str, n2: str, n3: str) -> int:
    return len(n1), len(n2), len(n3)

def get_min_len(a: str, b: str) -> int:
    return min(len(str(int(a))), len(str(int(b))))

def adjust_pow(len_number: int, len_splitted: int) -> int:
    """This is a function to set the pow of the number,
        it fill with zeros to the RIGHT of the spllitted
        e.g., if number = 123456789, then
        len_number = 9 
        len_splitted = 3 (123) (456) (789)
        (len_number - len_splitted) = 6 
        which means: 123*10**(6) = 123000000

    Args:
        len_number (int): the whole number size
        len_splitted (int): the size of a specific partition

    Returns:
        int: the length to add zeros  
    """
    return len_number - len_splitted

def get_max_len(s1, s2, s3):
    return max(s1, s2, s3)

def split_by_3(number: str):

    if has_two_digit(number):
        d1, d2 = get_unit_and_ten(number)
        d3     = 0
        e1, e2 = 1, 0
        return d1, e1, d2, e2, d3
    else:
        a1, a2, a3  = get_a1_a2_a3(number)
        l1, l2, l3  = get_lengths(a1, a2, a3)
        l_max       = get_max_len(l1, l2, l3) 

        a1 = padding(l_max, l1, a1)
        a2 = padding(l_max, l2,  a2)
        a3 = padding(l_max, l3,  a3)
        e1 = adjust_pow(len(number), l1)
        e2 = adjust_pow(len(number), (l1 + l2))

        return a1, e1, a2, e2, a3