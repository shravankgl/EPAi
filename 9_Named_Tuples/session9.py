import datetime
from functools import wraps
from time import perf_counter

from faker import Faker
from random import uniform
from collections import namedtuple
from collections import Counter
from statistics import mean
fake = Faker()

import random


def timed(fn: "function"):
    """
    Decorator for calculating time of execution.
    """
    if (not(callable(fn))):
        raise TypeError('fn is not a callable function')

    @wraps(fn)
    def inner(*args, **kwargs):
        """
        Inner function to calculate the time of execution.
        """
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = (end - start)
        print(f'Execution time for {fn.__name__} is {elapsed} sec')
        return result
    return inner


#faker profile namedtuple
profile = namedtuple('profile',fake.profile().keys())

#doc string
profile.__doc__ = "profile of a persion"
profile.name.__doc__ = "his/her name"
profile.birthdate.__doc__ = "his/her date of birth"
profile.sex.__doc__ = "his/her sex"
profile.blood_group.__doc__ = "his/her blood_group"
profile.ssn.__doc__ = "his/her social security number"
profile.username.__doc__ = "his/her username"
profile.website.__doc__ = "his/her website"
profile.mail.__doc__ = "his/her mail"
profile.address.__doc__ = "his/her address"
profile.residence.__doc__ = "his/her residence address"
profile.current_location.__doc__ = "his/her residence latitude and longitude"
profile.company.__doc__ = "his/her company"
profile.job.__doc__ = "his/her job"


@timed
def generate_random_profile(count:int = 10)->tuple:
    '''generates faker profile tuple of given count'''
    if type(count) != int:
        raise TypeError(f"'count' must be int not {count.__class__.__name__} ")
    return tuple((fake.profile() for _ in range(count)))

@timed
def convert_dictionary_to_namedtuple(dict_:iter, named_tuple:namedtuple)->tuple:
    '''converts dictionary to namedtuple'''
    return tuple((named_tuple(**obj) for obj in dict_))

#timed
def get_age(days):
    '''calculate age from days'''
    years = abs((days)/(365.242243600))
    yearsInt=int(years)

    months = abs((years-yearsInt)*12)
    monthsInt=int(months)

    days = abs(months-monthsInt)*(365.242/12)
    daysInt=int(days)

    return f"{yearsInt} year/s, {monthsInt} month/s, {daysInt} day/s"

@timed
def demograph(profile_list: 'list',obj_type)->tuple:
    """ summarize the demogrph information largest blood type, mean-current_location, oldest_person_age, and average age
        INPUT : profile_list: list: a list which contains the profiles in either a namedtuple or dictionary
        OUTPUT : tuple : oldest person age, average age, largest blood type, mean of current location
    """
    blood_group_list = []
    location_x_list = []
    location_y_list = []
    age_list = []

    if("dict" == obj_type):
        for x in profile_list:
            blood_group_list.append(x['blood_group'])
            location_x_list.append(x['current_location'][0])
            location_y_list.append(x['current_location'][1])
            age_list.append((datetime.date.today() - x['birthdate']).days)
    elif("namedtuple" == obj_type):
        for x in profile_list:
            blood_group_list.append(x.blood_group)
            location_x_list.append(x.current_location[0])
            location_y_list.append(x.current_location[1])
            age_list.append((datetime.date.today() - x.birthdate).days)
    return f"     largest bloodgroup : {max(Counter(blood_group_list))} \n \
    mean current_location : {(mean(location_x_list),mean(location_y_list))} \n \
    oldest person age : {get_age(max(age_list))} \n \
    average age : {get_age(sum(age_list)/len(age_list))} "

#stock namedtuple
stock = namedtuple('stock', 'name symbol open high close')

#stock doc string
stock.__doc__ = "stock information of the company"
stock.name.__doc__ = "name of the company"
stock.symbol.__doc__ = "symbol of the company"
stock.open.__doc__ = "opening stock value of the day"
stock.high.__doc__ = "highest stock value the day"
stock.close.__doc__ = "closing stock value of the day"


@timed
def generate_random_stock(count:int = 10)->tuple:
    '''generates faker company stock tuple of given count'''
    if type(count) != int:
        raise TypeError(f"'count' must be int not {count.__class__.__name__} ")

    stock_list = []

    for _ in range(count):
        name = fake.company()
        symbol = "".join(filter(lambda x: x.isupper(), name))
        open = random.uniform(100, 25_000) * random.random()
        close = open * random.uniform(0.2,2)
        high = open * random.uniform(0.2,2)
        if high < open:
            high = open
        if high < close:
            high = close
        weight = 1 #random.random()
        stock_list.append(stock(name, symbol, open*weight, high*weight, close*weight))
    return stock_list

@timed
def calculate_stock_market(stocks:'list')->tuple:
    """
    This is a function which calculates the value the stock market started at,the highest value during the day, and end value.
    Output: tuple: value the stock market started at,the highest value during the day, and end value.
    """
    if isinstance(stocks[0],tuple)!= True:
        raise TypeError("Invalid input:the input should be a list of tuples!!!")
    
    day_open = 0
    day_high = 0
    day_close = 0

    for stock in stocks:
        day_open += stock.open
        day_high += stock.high
        day_close += stock.close

    return f"Open index : {day_open} \nHigh index : {day_high} \nClose index : {day_close} \n"
