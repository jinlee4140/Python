# (1) Write a function countVowels to count up the 
#number of vowels contained in a given string. Valid vowels are: 'a', 'e', 'i', 'o', 'u'.
# For example, countVowels('aeiou') should return 5.

def countVowels(str):
	vowels = [1 for letter in str if letter in ['a', 'e', 'i', 'o', 'u']]
	return sum(vowels)

print countVowels('aeiou')
print countVowels('python')



print countVowels('') #0
print countVowels(' bcd fgh jklmn pqrst vwxyz') #0
print countVowels('a')#1


print "(2) Write a function count_nyc to count up the number of times the string 'boston' occurs in a given string."


def count_boston(str):
	return str.count('boston')


print count_boston('') #0
print count_boston('welcome to BOSTON') #0
print count_boston('boston') #1

print "(3) Write a function countString with two arguments raw_string and string_to_count. Your function should return the number of times of string_to_count occurs in the the raw_string argument. In addition, Your function should be case insensitive in this time."
def countString(raw_string, string_to_count):
    str_to_count = string_to_count.lower()
    raw_str = raw_string.lower()
    return raw_str.count(str_to_count)

print countString('Hello boston', 'boston')

print countString('welcome to Launch Academy', '') 

print countString('bostonBOSTONboston', 'boston')


#(4) Recall the last example in question 3, count_string('welcome to Launch Academy', '')
# returns 26, which is the length of the first argument. It is because we assign nothing to the second argument,
#  so any character was counted. This time you need to rewrite the function count_string, if the second argument
#   is still nothing, the function should raise an ValueError with message:

#The length of string_to_count should not be 0!

def countString(raw_string, string_to_count):
	if not string_to_count:
		raise ValueError('The length of string_to_count should not be 0!')
	else:
		str_to_count = string_to_count.lower()
		raw_str = raw_string.lower()
		return raw_str.count(str_to_count)



# print countString("welcome to Launch Academy", '')
print countString("hello world", 'o')
print countString("hello world", 'i')


#(5) Write a function countAlphabet to count the number of frequencies of each
# letter occurs. Your function should return a dict. Again, your function should
#  be case insensitive.



