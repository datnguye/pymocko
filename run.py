from pymocko import num, price, date, char, word, model
import datetime 

print("Mock model")
print(model.mock(schema_json={"id":"num", "user_name":"word", "name":"word", "dob":"date", "phone_no":"char", "email":"word", "gender":"word", "ip_address":"char"}, count=5))

# print("Randomize words")
# print(word.mock())
# print(word.mock(no_of_word=20))
# print(word.mock(no_of_word=10, upper_first=True))
# print(word.mock_phone())
# print(word.mock_phone(prefix="+41"))
# print(word.mock_email())
# print(word.mock_email(domain="data.com"))
# print(word.mock_gender())

# print("Randomize character")
# print(char.mock())
# print(char.mock(no_of_char=20,number_inc=True))
# print(char.mock(no_of_char=30,number_inc=True,special_inc=True))

# print("Randomize date")
# print(date.mock())
# print(date.mock(f=datetime.datetime(2020,6,1)))

# print("Randomize price")
# print(price.mock()) # default from 0 to 10000
# print(price.mock(f=1000, t=10000))
# print(price.mock(f=0, t=2500, decimal=0))
# print(price.mock(f=0, t=2500, decimal=4))
# print(price.mock(f=0, t=2500, neg=True))

# print("Randomize number")
# print(num.mock()) # default from 0 to 1000
# print(num.mock(f=1, t=10))
# print(num.mock(f=1, t=1000, neg=True))