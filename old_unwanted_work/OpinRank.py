import os
import re
from collections import Counter
from math import sqrt, floor
import random

class Tester:
    def __init__(self, filename1, filename2, print_debugging_info=False):
        self.filename1 = fr'{filename1}'
        self.filename2 = fr'{filename2}'
        self.print_debugging_info = print_debugging_info

    def print(self, st1, st2='', st3=''):
        if self.print_debugging_info:
            print(st1, st2, st3)

    def test_two_ways(self):
        res1 = self.test()
        self.filename1, self.filename2 = self.filename2, self.filename1
        res2 = self.test()
        self.filename1, self.filename2 = self.filename2, self.filename1
        result = (res1 + res2) / 2
        print('Averaged percentage =', result, 'percent')
        return result

    def test(self):
        data_files = [open(self.filename1, encoding='unicode_escape'), open(self.filename2, encoding='unicode_escape')]
        TOKEN = re.compile(r'([^\W\d]+|\d+|[^\w\s])')
        counters = [0, 0]
        counters[0] = [Counter(re.findall(TOKEN, line)) for line in data_files[0]]
        # self.print('first counter before making it right looks like ', counters[0])
        counters[1] = [Counter(re.findall(TOKEN, line)) for line in data_files[1]]
        res_counters = [counters[0][0], counters[1][0]]
        for i in range(1, len(counters[0])):
            res_counters[0] += counters[0][i]
        for i in range(1, len(counters[1])):
            res_counters[1] += counters[1][i]
        counters = res_counters
        set_to_delete = {'DOC', "AUTHOR", "DATE", "TEXT", "FAVORITE"}
        for i in range(2):
            keys = list(counters[i].keys())
            for word in keys:
                if len(word) < 2 or word in set_to_delete:
                    self.print(word)
                    del counters[i][word]
        self.print('first counter is ', counters[0])
        self.print('second counter is ', counters[1])

        self.print(counters[0])
        self.print(counters[1])

        def RMSE(cntr1, cntr2):
            result = 0
            words = set(cntr1.keys()).union(set(cntr2.keys()))
            total_words_in_1, total_words_in_2 = sum(cntr1.values()), sum(cntr2.values())
            num_of_different_words = len(words)
            for word in words:
                # if c1[word] > 0 and c1[word] < 10 or c2[word] > 0 and c2[word] < 10:
                #     continue
                diff = cntr1[word] / total_words_in_1 - cntr2[word] / total_words_in_2
                result += diff * diff / num_of_different_words
            return sqrt(result)

        self.print('RMSE при сравнении двух текстовых файлов', RMSE(counters[0], counters[1]))

        # ---------------
        self.print('NEXT PART')
        data_files[0].close()
        data_files[1].close()
        data_files = [open(self.filename1, encoding='unicode_escape'), open(self.filename2, encoding='unicode_escape')]
        tokens = [tok for line in data_files[0] for tok in re.findall(TOKEN, line)]
        tokens += [tok for line in data_files[1] for tok in re.findall(TOKEN, line)]
        # self.print(tokens)
        split = sum(counters[0].values())
        self.print(split)
        self.print('sizes = ', split, sum(counters[1].values()))
        distribution = []
        # self.print(tokens)
        for i in range(1000):
            random.shuffle(tokens)
            c1 = Counter(tokens[:split])
            c2 = Counter(tokens[split:])
            distribution.append(RMSE(c1, c2))
        self.print('-------')
        observed = RMSE(counters[0], counters[1])
        p_value = sum(x >= observed for x in distribution) / len(distribution)
        self.print(p_value)
        self.print(observed, max(distribution), sum(distribution) / len(distribution))

        percentage_ans = (observed / max(distribution) - 1) * 100
        self.print("Percentage is ", percentage_ans, 'percent')
        data_files[0].close()
        data_files[1].close()
        return percentage_ans


counter_of_tests = 0

def conduct_test(filename1, filename2, info, debugging=False):
    global counter_of_tests
    counter_of_tests += 1
    print("Test number", counter_of_tests, ':', info)
    print("Result is: ", end='')
    my_tester = Tester(filename1, filename2, debugging)
    to_return = my_tester.test_two_ways()
    print()
    return to_return


# conduct_test('data1.txt', 'data2.txt', '1 similar hotel reviews')  # 1
# conduct_test('data1.txt', 'data1.txt', '2 same')  # 2
# conduct_test('data2.txt', 'data2.txt', '3 same')  # 3
# conduct_test('data2.txt', 'data1.txt', '4 similar hotel reviews')  # 4
# conduct_test('OpinRankDataset/hotels/london/uk_england_london_22_jermyn_street', 'data1.txt', '5 similar hotels')
# conduct_test('OpinRankDataset/hotels/london/uk_england_london_crowne_plaza_hotel_london_ealing', 'data1.txt', '6 similar hotels')
# conduct_test('OpinRankDataset/hotels/london/uk_england_london_22_jermyn_street', 'OpinRankDataset/cars/2009/2009_acura_mdx', '7 hotel and car review')
# conduct_test('OpinRankDataset/hotels/london/uk_england_london_ace_hotel', 'OpinRankDataset/cars/2009/2009_acura_rl', '8 hotel and car review')
# conduct_test('OpinRankDataset/cars/2009/2009_acura_rl', 'OpinRankDataset/cars/2009/2009_acura_mdx', '9 cars review')
# conduct_test('OpinRankDataset/cars/2009/2009_lexus_is_250', 'OpinRankDataset/cars/2009/2009_acura_rl', '10 cars review')

# тестирование
hotels = list()
def do_multiple_tests_for_hotels():
    print("!!! HOTELS ONLY !!!")
    hotel_dir_name = 'OpinRankDataset/hotels/'
    for city_name in os.listdir(hotel_dir_name):
        city_name += '/'
        if not os.path.isdir(hotel_dir_name + city_name):
            continue
        for hotel_name in os.listdir(hotel_dir_name + city_name):
            # print(hotel_dir_name + city_name + hotel_name)
            hotels.append(hotel_dir_name + city_name + hotel_name)

    # testing
    list_of_res = []
    for i in range(21):
        first_hotel = random.choice(hotels)
        second_hotel = random.choice(hotels)
        print(first_hotel + '\tVS\t' + second_hotel)
        res = conduct_test(first_hotel, second_hotel, str(i + 1) + ' comparing hotels')
        list_of_res.append(res)
    list_of_res.sort()
    upper_bound_for = floor(0.75 * len(list_of_res))
    print(list_of_res)
    print(upper_bound_for)
    print(list_of_res[upper_bound_for])


cars = list()

def do_multiple_tests_for_cars():
    print("!!! CARS ONLY !!!")
    car_dir_name = 'OpinRankDataset/cars/'

    for year_name in os.listdir(car_dir_name):
        year_name += '/'
        if not os.path.isdir(car_dir_name + year_name):
            continue
        for car_name in os.listdir(car_dir_name + year_name):
            # print(car_dir_name + year_name + car_name)
            cars.append(car_dir_name + year_name + car_name)

    list_of_res = []
    for i in range(21):
        first_car = random.choice(cars)
        second_car = random.choice(cars)
        print(first_car + '\tVS\t' + second_car)
        res = conduct_test(first_car, second_car, str(i + 1) + ' comparing cars')
        list_of_res.append(res)
    list_of_res.sort()
    lower_bound_for = floor(0.75 * len(list_of_res))
    print(list_of_res)
    print(lower_bound_for)
    print(list_of_res[lower_bound_for])

def do_multiple_tests_for_cars_and_hotels():
    # testing
    list_of_res = []
    for i in range(21):
        first_hotel = random.choice(hotels)
        second_car = random.choice(cars)
        print(first_hotel + '\tVS\t' + second_car)
        res = conduct_test(first_hotel, second_car, str(i + 1) + ' comparing hotel and a car')
        list_of_res.append(res)
    list_of_res.sort()
    lower_bound_for = floor(0.25 * len(list_of_res))
    print(list_of_res)
    print(lower_bound_for)
    print(list_of_res[lower_bound_for])


do_multiple_tests_for_hotels()
do_multiple_tests_for_cars()
do_multiple_tests_for_cars_and_hotels()
