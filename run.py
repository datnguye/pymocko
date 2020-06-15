from pymocko import num, price, date, char, word
import datetime 

print("Randomize words")
print(word.mock())
print(word.mock(no_of_word=20))
print(word.mock(no_of_word=10, upper_first=True))

print("Randomize character")
print(char.mock())
print(char.mock(no_of_char=20,number_inc=True))
print(char.mock(no_of_char=30,number_inc=True,special_inc=True))

print("Randomize date")
print(date.mock())
print(date.mock(f=datetime.datetime(2020,6,1)))

print("Randomize price")
print(price.mock()) # default from 0 to 10000
print(price.mock(f=1000, t=10000))
print(price.mock(f=0, t=2500, decimal=0))
print(price.mock(f=0, t=2500, decimal=4))
print(price.mock(f=0, t=2500, neg=True))

print("Randomize number")
print(num.mock()) # default from 0 to 1000
print(num.mock(f=1, t=10))
print(num.mock(f=1, t=1000, neg=True))