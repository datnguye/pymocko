# pymocko
This is to generate mock data

Installation:
```
python -m pip install pymocko
```

#### Development Eviroment:
```
git clone https://github.com/datnguye/pymocko.git
cd pymocko/pymocko

python -m venv env
.\env\Scripts\activate
OR source env/bin/activate (linux)

python -m pip install -r requirements.txt

```

Run test cases:
```
cd ..
python run.py
```

### Version used
```
Python 3.7.5
```

## USAGE

#### Mokcing by json model:
```
print("Mock model")
print(model.mock(schema_json={"id":"num", "name":"word", "qty":"num", "unit_price":"price", "created_at":"date", "updated_at":"date"}, count=5))
print(model.mock(schema_json={"id":"num", "user_name":"word", "name":"word", "dob":"date", "phone_no":"char", "email":"word", "gender":"word", "ip_address":"char"}, count=5))
print(model.mock(schema_json={"id":"num", "name":"word", "qty": { "stocked": "num", "online": "num" }, "price":[ { "unit_price":"price", "effective_date": "date"} ], "created_at":"date", "updated_at":"date"}, count=3))
print(model.mock(schema_json={"id":"num", "name":"word", "tags": ["word"], "reference_names": [ "word" ], "qty": { "stocked": "num", "online": "num" }, "price":[ { "unit_price":"price", "effective_date": "date"} ], "created_at":"date", "updated_at":"date"}, count=3))
```

#### Randomize number:
```
from pymocko import num
print(num.mock())
print(num.mock(f=1, t=10))
print(num.mock(f=1, t=1000, neg=True))
```

#### Randomize price:
```
from pymocko import price
print(price.mock())
print(price.mock(f=1000, t=10000))
print(price.mock(f=0, t=2500, decimal=0))
print(price.mock(f=0, t=2500, decimal=4))
print(price.mock(f=0, t=2500, neg=True))
```

#### Randomize date:
```
from pymocko import date
print(date.mock())
print(date.mock(f=datetime.datetime(2020,6,1)))
```

#### Randomize character:
```
from pymocko import char
print(char.mock())
print(char.mock(no_of_char=20,number_inc=True))
print(char.mock(no_of_char=30,number_inc=True,special_inc=True))
```

#### Randomize word/sentence:
```
from pymocko import word
print(word.mock()) 
print(word.mock(no_of_word=20))
print(word.mock(no_of_word=10, upper_first=True))
print(word.mock_phone())
print(word.mock_phone(prefix="+84"))
print(word.mock_email())
print(word.mock_email(domain="data.com"))
print(word.mock_gender())
```