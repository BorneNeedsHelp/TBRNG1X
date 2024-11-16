import time


class TBRNG1X:
    @staticmethod
    def TBRNG():
        current_time = int(time.time())
        random_number = (current_time * 123456789) % 1000000
        random_decimal = float(random_number) / 10000
        return random_decimal

    @staticmethod
    def TBRNG_Int_Range(min_value, max_value):
        min_value = int(min_value)
        max_value = int(max_value)
        current_time = int(time.time())
        random_number = (current_time * 123456789) % (max_value - min_value + 1)
        scaled_number = min_value + random_number
        return scaled_number

    @staticmethod
    def TBRNG_Int():
        current_time = int(time.time())
        random_number = (current_time * 123456789) % 1000000
        return random_number

    @staticmethod
    def TBRNG_Range(min_value, max_value):
        min_value = int(min_value)
        max_value = int(max_value)
        current_time = int(time.time())
        random_number = (current_time * 123456789) % (max_value - min_value + 1)
        scaled_number = min_value + random_number + random_number
        return scaled_number / 10 % 1000

    @staticmethod
    def TBRNG_Binary():
        current_time = int(time.time())
        random_number = (current_time * 123456789) % 1000000
        return format(random_number, 'b')

    @staticmethod
    def TBRNG_Double():
        current_time = int(time.time())
        random_number = (current_time * 123456789) % 1000000
        random_decimal = float(random_number) / 10000
        return random_decimal / 10

    @staticmethod
    def TBRNG_Gauss():
        current_time = int(time.time())
        real = current_time * 123456789 % 100
        fake = real * 123456789 % 100
        gauss = complex(real, fake)
        return gauss

    @staticmethod
    def TBRNG_Average(times_to_recurculate):
        current_time = int(time.time())
        times = 0
        random_full = 0
        for i in range(1, int(times_to_recurculate)):
            random_number = (current_time * 123456789) % 1000000
            random_number += random_full
            times += 1
            time.sleep(1)
        return int(random_number // times)

    @staticmethod
    def TBRNG_Statistics(times_to_recurculate):
        current_time = int(time.time())
        random_full = 0
        for i in range(1, times_to_recurculate):
            random_number = (current_time * 123456789) % 1000000
            random_number += random_full
            time.sleep(1)
        return random_number

    @staticmethod
    def TBRNG_Sort(times_to_recalculate):
        current_time = int(time.time())
        lists = []
        for i in range(0, times_to_recalculate):
            random_number = (current_time * 123456789) % 1000000
            current_time = time.time()
            lists.append(random_number)

        for i2 in range(1, len(lists)):
            swapped = False
            for i3 in range(0, len(lists) - i2):
                if lists[i3] > lists[i3 + 1]:
                    lists[i3], lists[i3 + 1] = lists[i3 + 1], lists[i3]
                    swapped = True
            if not swapped:
                break
        return lists

    @staticmethod
    def TBRNG_Lean(a, b, lean):
        if not (a <= lean <= b):
            return -0

        current_time = int(time.time() * 1000)
        range_span = b - a
        time_based_value = (current_time * 123456789) % range_span

        if lean >= (a + b) // 2:
            result = a + (lean - a) * (time_based_value / range_span)
        else:
            result = b - (b - lean) * (time_based_value / range_span)

        return int(result)

    import time

    @staticmethod
    def TBRNG_Hex():
        current_time = int(time.time())
        random_number = (current_time * 123456789) % 1000000
        return hex(random_number)[2:]

    @staticmethod
    def TBRNG_Hex_Range(min_value, max_value):
        min_value = int(min_value)
        max_value = int(max_value)
        current_time = int(time.time())
        random_number = (current_time * 123456789) % (max_value - min_value + 1)
        scaled_number = min_value + random_number
        hex_result = hex(scaled_number)[2:]
        return hex_result

    @staticmethod
    def TBRNG_Unicode(length):
        current_time = int(time.time())
        random_string = ""

        for _ in range(length):
            random_number = (current_time * 123456789) % 1000000
            current_time += 1
            unicode_char = chr(33 + (random_number % 94))
            random_string += unicode_char

        return random_string

    @staticmethod
    def TBRNG_Time_12():
        min_value, min_2_value = 1, 1
        max_value, max_2_value = 12, 60
        current_time = int(time.time())
        random_hour = (current_time * 123456789) % (max_value - min_value + 1)
        random_min = (current_time * 123456789) % (max_2_value - min_2_value + 1)
        scaled_hour = min_value + random_hour
        scaled_min = min_2_value + random_min
        return f'{scaled_hour}:{scaled_min}'

    @staticmethod
    def TBRNG_Time_24():
        min_value, min_2_value = 0, 1
        max_value, max_2_value = 24, 60
        current_time = int(time.time())
        random_hour = (current_time * 123456789) % (max_value - min_value + 1)
        random_min = (current_time * 123456789) % (max_2_value - min_2_value + 1)
        scaled_hour = min_value + random_hour
        scaled_min = min_2_value + random_min
        return f'{scaled_hour}:{scaled_min}'

    @staticmethod
    def TBRNG_UPD_Log():
        with open('UPDS', 'r') as Read_Updates:
            return Read_Updates.read()
        
