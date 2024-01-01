
def format_moolah(number):
        suffixes = ['', 'k', 'M', 'B']
        temp_num = number
        thousands_order = 0
        while temp_num > 1:
            thousands_order += 1
            temp_num = temp_num / 1000

        # back off one, for some precision
        thousands_order -= 1

        if thousands_order > 3:
            thousands_order = 3
        if thousands_order < 0:
            thousands_order = 0

        reduction_factor = 1000**thousands_order
        reduced_number = numpy.floor(number / reduction_factor)
        reduced_number_string = str(int(reduced_number)) + suffixes[thousands_order]
        return(reduced_number_string)

