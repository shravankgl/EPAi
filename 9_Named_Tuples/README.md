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
