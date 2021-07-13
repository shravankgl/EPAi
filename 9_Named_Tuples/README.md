# Session 9 assignment of EPAi3.0
## Named Tuples

### Named Tuples
#### **1) Profile
Profile is declared with the keys of porfile dictionary from faker package
```
profile = namedtuple('profile',fake.profile().keys())

#profile doc string
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
```
#### **2) Profile
```
stock = namedtuple('stock', 'name symbol open high close')

#stock doc string
stock.__doc__ = "stock information of the company"
stock.name.__doc__ = "name of the company"
stock.symbol.__doc__ = "symbol of the company"
stock.open.__doc__ = "opening stock value of the day"
stock.high.__doc__ = "highest stock value the day"
stock.close.__doc__ = "closing stock value of the day"
```

#### ** Functions**

#### **1) generate_random_profile(count:int = 10) **:
This function generated tuple of random faker profiles of required count
**Parameters**
1) count: an integer value, default value is 10

**Exceptions**
1) count should be an integer

**Implementation**
```return tuple((fake.profile() for _ in range(count))) ```

#### **2) convert_dictionary_to_namedtuple(dict_:iter, named_tuple:namedtuple)**:
converts an collection of dictionaries to namedtuple 
**Parameters**
1) dict_: any collection of dictionary
2) named_tuple: a namedtuple type

**Implementation**
```
return tuple((named_tuple(**obj) for obj in dict_))
```


#### **3) get_ageget_age(days)**:
Converts no of days into years, months, days 
**Parameters**
1)  days: an integer value of no of days

**Exceptions**
1) days should be an integer

**Implementation**
```
    years = abs((days)/(365.242243600))
    yearsInt=int(years)

    months = abs((years-yearsInt)*12)
    monthsInt=int(months)

    days = abs(months-monthsInt)*(365.242/12)
    daysInt=int(days)

    return f"{yearsInt} year/s, {monthsInt} month/s, {daysInt} day/s"
```


#### **4) demograph(profile_list: 'list',obj_type)**:
summarize the demogrph information largest blood type, mean-current_location, oldest_person_age, and average age
**Parameters**
1)  profile_list: list of profiles
2)  obj_type: data type of object in the list

**Implementation**
1) extract the blood group, location values and age into separate list
  ```
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
  ```
2) Calculate and return demograph information from the extracted lists
```
    return f"     largest bloodgroup : {max(Counter(blood_group_list))} \n \
    mean current_location : {(mean(location_x_list),mean(location_y_list))} \n \
    oldest person age : {get_age(max(age_list))} \n \
    average age : {get_age(sum(age_list)/len(age_list))} "
```

#### **5) generate_random_stock(count:int = 10) **:
This function generated tuple of random faker profiles of required count
**Parameters**
1) count: an integer value, default value is 10

**Exceptions**
1) count should be an integer

**Implementation**
```
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
```

#### **6) calculate_stock_market(stocks:iter) **:
Calculate the value the stock market started at,the highest value during the day, and end value.
**Parameters**
1)  stocks: collection of stocks

**Implementation**
```
    for stock in stocks:
        day_open += stock.open
        day_high += stock.high
        day_close += stock.close

    return f"Open index : {day_open} \nHigh index : {day_high} \nClose index : {day_close} \n"
```

#### **Testcases**
|Sl No| Testcase|Description |
|:--- | :-- | :-- | 
|1|test_profile_fields_available | test for all keys in Faker dictionary matches with fields profile namedtuple|
|2|test_profile_fields_not_empty| test none of the fields in Faker profile is empty|
|3|test_profile_doc_string_not_empty | test none of the doc string in profile is empty|
|4|test_profile_generation | test number of profiles created is equal to count value|
|5|test_validate_datatype_of_count_generate_random_profile |validate the datatype of count is int |
|6|test_convert_dictionary_to_namedtuple | test if datatype of converted list is profile|
|7|test_get_age | test get_age function|
|8|test_validate_datatype_of_days_get_age | validate the datatype of days is int|
|9|test_demograph | test the demograph calculation|
|10|test_dict_namedtuple_performance | test to compare the performance of dictonary and namedtuple|
|11|test_stock_fields_not_empty | test none of the fields in stock namedtuple is empty|
|12|test_stock_doc_string_not_empty | test none of the doc string in stock is empty|
|13|test_stock_generation | test number of stocks created is equal to count value|
|14|test_validate_datatype_of_count_generate_random_stock | validate the datatype of count is int|
|15|test_stock_open_high_close_values | test to make sure high is greater than or equal to open or close|
|16|test_calculate_stock_market | test stock market open, high, close is correct|


### Testcase results
```
================================================= test session starts =================================================
platform win32 -- Python 3.8.3, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- c:\python38\python.exe
cachedir: .pytest_cache
rootdir: D:\TSAI\EPAi\Session9_NamedTuple
plugins: Faker-8.10.0
collected 16 items

test_session9.py::test_profile_fields_available PASSED                                                           [  6%]
test_session9.py::test_profile_fields_not_empty PASSED                                                           [ 12%]
test_session9.py::test_profile_doc_string_not_empty PASSED                                                       [ 18%]
test_session9.py::test_profile_generation PASSED                                                                 [ 25%]
test_session9.py::test_validate_datatype_of_count_generate_random_profile PASSED                                 [ 31%]
test_session9.py::test_convert_dictionary_to_namedtuple PASSED                                                   [ 37%]
test_session9.py::test_get_age PASSED                                                                            [ 43%]
test_session9.py::test_validate_datatype_of_days_get_age PASSED                                                  [ 50%]
test_session9.py::test_demograph PASSED                                                                          [ 56%]
test_session9.py::test_dict_namedtuple_performance PASSED                                                        [ 62%]
test_session9.py::test_stock_fields_not_empty PASSED                                                             [ 68%]
test_session9.py::test_stock_doc_string_not_empty PASSED                                                         [ 75%]
test_session9.py::test_stock_generation PASSED                                                                   [ 81%]
test_session9.py::test_validate_datatype_of_count_generate_random_stock PASSED                                   [ 87%]
test_session9.py::test_stock_open_high_close_values PASSED                                                       [ 93%]
test_session9.py::test_calculate_stock_market PASSED                                                             [100%]

=========================================== 16 passed in 134.72s (0:02:14) ============================================
```
