import pytest 
import session9
from session9 import *

from faker import Faker
fake = Faker()

from decimal import Decimal


faker_profile_dict_keys = fake.profile().keys()

fake_profile_namedtuple = convert_dictionary_to_namedtuple(generate_random_profile(1),profile)[0]
fake_profile_namedtuple_fields = fake_profile_namedtuple._fields

def test_profile_fields_available():
    ''' test for all keys in Faker dictionary matches with fields profile namedtuple'''    

    #check faker keys in profile fields
    for key in faker_profile_dict_keys:
        assert True == (key in fake_profile_namedtuple_fields) # hasattr(fake_profile_namedtuple,key)
    #check  profile fields in faker keys
    for field in fake_profile_namedtuple_fields:
        assert True == (field in faker_profile_dict_keys)

def test_profile_fields_not_empty():
    ''' test none of the fields in Faker profile is empty'''    
    for field in fake_profile_namedtuple_fields:
        assert None != getattr(fake_profile_namedtuple,field)

def test_profile_doc_string_not_empty():
    ''' test none of the doc string in profile is empty'''
    assert len(profile.__doc__) > 0
    assert len(profile.name.__doc__) > 0
    assert len(profile.birthdate.__doc__) > 0
    assert len(profile.sex.__doc__) > 0
    assert len(profile.blood_group.__doc__) > 0
    assert len(profile.ssn.__doc__) > 0
    assert len(profile.username.__doc__) > 0
    assert len(profile.website.__doc__) > 0
    assert len(profile.mail.__doc__) > 0
    assert len(profile.address.__doc__) > 0
    assert len(profile.residence.__doc__) > 0
    assert len(profile.current_location.__doc__) > 0
    assert len(profile.company.__doc__) > 0
    assert len(profile.job.__doc__) > 0


def test_profile_generation():
    '''test number of profiles created is equal to count value'''
    assert 10 == len(generate_random_profile(10))
    assert 50 == len(generate_random_profile(50))
    assert 100 == len(generate_random_profile(100))

def test_validate_datatype_of_count_generate_random_profile():
    '''validate the datatype of count is int'''
    with pytest.raises(TypeError, match=r".*'count' must be int not float.*"):
        generate_random_profile(10.0)
    with pytest.raises(TypeError, match=r".*'count' must be int not str.*"):
        generate_random_profile("hello")
    with pytest.raises(TypeError, match=r".*'count' must be int not list.*"):
        generate_random_profile([1,2,3])

def test_convert_dictionary_to_namedtuple():
    '''test if datatype of converted list is profile'''
    profile_list =  convert_dictionary_to_namedtuple(generate_random_profile(10),profile)
    for profile_ in profile_list:
        assert 'profile' == profile_.__class__.__name__


def test_get_age():
    '''test get_age function'''
    assert "1 year/s, 0 month/s, 1 day/s" == get_age(366)
    assert "0 year/s, 11 month/s, 30 day/s" == get_age(364)
    assert "1 year/s, 1 month/s, 1 day/s" == get_age(396)
    
def test_validate_datatype_of_days_get_age():
    '''validate the datatype of days is int'''
    with pytest.raises(TypeError, match=r".*'days' must be int not float.*"):
        get_age(10.0)
    with pytest.raises(TypeError, match=r".*'days' must be int not str.*"):
        get_age("hello")
    with pytest.raises(TypeError, match=r".*'days' must be int not list.*"):
        get_age([1,2,3])

def test_demograph():
    '''test the demograph calculation'''
    fake_profiles_dict = ({'address': '9089 Nichols Lodge\nNorth Anthonystad, ND 17725',
  'birthdate': datetime.date(1941, 4, 13),
  'blood_group': 'AB-',
  'company': 'Hardin, Smith and Melendez',
  'current_location': (Decimal('72.700640'), Decimal('-8.379374')),
  'job': "Barrister's clerk",
  'mail': 'william44@hotmail.com',
  'name': 'Heather Torres',
  'residence': '884 Julia Roads Suite 037\nEvansland, NV 26477',
  'sex': 'F',
  'ssn': '163-49-0337',
  'username': 'tyler59',
  'website': ['http://vance.com/', 'https://www.simmons.biz/']},
 {'address': '828 Todd Squares\nTimothybury, FL 10394',
  'birthdate': datetime.date(2012, 9, 15),
  'blood_group': 'AB+',
  'company': 'Smith, Perez and Edwards',
  'current_location': (Decimal('32.9266245'), Decimal('-136.106601')),
  'job': 'Company secretary',
  'mail': 'susanjones@yahoo.com',
  'name': 'Karen Macias',
  'residence': '267 Marsh Prairie\nPort Tracyburgh, MT 29152',
  'sex': 'F',
  'ssn': '179-94-6474',
  'username': 'wesley55',
  'website': ['https://www.pruitt.com/']},
 {'address': '33750 Weaver Ferry Apt. 525\nNorth Christopher, MI 31898',
  'birthdate': datetime.date(1955, 8, 25),
  'blood_group': 'AB-',
  'company': 'Garcia-Lopez',
  'current_location': (Decimal('50.4030935'), Decimal('177.608880')),
  'job': 'Education administrator',
  'mail': 'qford@hotmail.com',
  'name': 'Deborah Barnett',
  'residence': '804 Boyle Ridge\nHarrisshire, NC 15335',
  'sex': 'F',
  'ssn': '303-06-5199',
  'username': 'zhudson',
  'website': ['https://www.moore.net/', 'https://www.williams.com/']},
 {'address': '50331 Sherman Glen Suite 159\nWest Thomas, OR 60511',
  'birthdate': datetime.date(2019, 10, 8),
  'blood_group': 'B+',
  'company': 'Owens, Chung and Gonzales',
  'current_location': (Decimal('-57.925414'), Decimal('-179.664195')),
  'job': 'Psychologist, occupational',
  'mail': 'anthony08@yahoo.com',
  'name': 'Robert Hughes',
  'residence': '709 Ashlee Track\nNew Juanmouth, ID 11645',
  'sex': 'M',
  'ssn': '508-52-7990',
  'username': 'williamstony',
  'website': ['http://www.hamilton.com/',
   'http://mason.org/',
   'https://serrano-atkins.net/']})

    fake_profiles_namedtuple = convert_dictionary_to_namedtuple( fake_profiles_dict ,profile)

    assert  demograph(fake_profiles_dict,'dict') == demograph(fake_profiles_namedtuple,'namedtuple') ==  "     largest bloodgroup : B+ \n     mean current_location : (Decimal('24.526236'), Decimal('-36.6353225')) \n     oldest person age : 80 year/s, 3 month/s, 1 day/s \n     average age : 39 year/s, 2 month/s, 5 day/s "

fake_profile_dictionary_10_000 = generate_random_profile(10_000)
fake_profile_namedtuple_10_000 = convert_dictionary_to_namedtuple(fake_profile_dictionary_10_000,profile)


def test_dict_namedtuple_performance():
    '''test to compare the performance of dictonary and namedtuple'''

    start = perf_counter()
    for _ in range(1000):
        demograph(fake_profile_namedtuple_10_000,"namedtuple")
    end = perf_counter()
    namedtuple_elapsed = (end - start)

    start = perf_counter()
    for _ in range(1000):
        demograph(fake_profile_dictionary_10_000,"dict")
    end = perf_counter()
    dict_elapsed = (end - start)    

    assert dict_elapsed > namedtuple_elapsed



def test_stock_fields_not_empty():
    ''' test none of the fields in stock namedtuple is empty''' 
    stock_ = generate_random_stock(1)[0]   
    for field in stock._fields:
        assert None != getattr(stock_,field)

def test_stock_doc_string_not_empty():
    ''' test none of the doc string in stock is empty'''
    assert len(stock.__doc__) > 0
    assert len(stock.name.__doc__) > 0
    assert len(stock.symbol.__doc__) > 0
    assert len(stock.open.__doc__) > 0
    assert len(stock.high.__doc__) > 0
    assert len(stock.close.__doc__) > 0

def test_stock_generation():
    '''test number of stocks created is equal to count value'''
    assert 10 == len(generate_random_stock(10))
    assert 50 == len(generate_random_stock(50))
    assert 100 == len(generate_random_stock(100))

def test_validate_datatype_of_count_generate_random_stock():
    '''validate the datatype of count is int'''
    with pytest.raises(TypeError, match=r".*'count' must be int not float.*"):
        generate_random_stock(10.0)
    with pytest.raises(TypeError, match=r".*'count' must be int not str.*"):
        generate_random_stock("hello")
    with pytest.raises(TypeError, match=r".*'count' must be int not list.*"):
        generate_random_stock([1,2,3])

def test_stock_open_high_close_values():
    '''test to make sure high is less than or equal to open or close'''
    stocks = generate_random_stock(10)
    for stock_ in stocks:
        assert stock_.high >= stock_.open
        assert stock_.high >= stock_.close

def test_calculate_stock_market():
    '''test stock market open, high, close is correct'''
    stocks = [stock(name='Bowman Group', symbol='BG', open=6200.56439626876, high=9429.488513790375, close=8912.184713785548), 
            stock(name='Hicks and Sons', symbol='HS', open=4827.56386679894, high=4877.329115630371, close=1364.542280443182), 
            stock(name='Jennings-Johnson', symbol='JJ', open=10181.883950151056, high=10181.883950151056, close=9889.247048809815), 
            stock(name='Walker Inc', symbol='WI', open=10102.229791515016, high=17387.077644208843, close=17387.077644208843), 
            stock(name='Kirk, Allen and Reed', symbol='KAR', open=9433.821824140465, high=16454.845186010243, close=9582.261252321166), 
            stock(name='Schroeder-Warren', symbol='SW', open=389.3936343844695, high=464.74240037497253, close=99.93211909588699), 
            stock(name='Hall and Sons', symbol='HS', open=7291.483996717891, high=14263.850820678063, close=7026.577643208964), 
            stock(name='Young Ltd', symbol='YL', open=7521.418099415024, high=12027.760925745906, close=5520.979539997164), 
            stock(name='Shaw, Zavala and Cox', symbol='SZC', open=5205.886273339603, high=8083.736771352835, close=8083.736771352835), 
            stock(name='Chavez-Lopez', symbol='CL', open=8146.022559933936, high=16165.100685136455, close=5601.16989194355)]

    assert calculate_stock_market(stocks) == "Open index : 69300.26839266515 \nHigh index : 109335.81601307912 \nClose index : 73467.70890516693 \n"

