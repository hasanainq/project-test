def reverse(str):
    '''
 		return reverse string
        eg: hello => olleh 
	'''
    return str[::-1]

# print(reverse("hello"))

def is_palindrom(str):
    '''
 		return true if the string is palindrom
	'''
    return str==reverse(str)

def sum(num1, num2):
    	return num1 + num2

# print(sum(2,2))

def is_prime(number):
    '''
 		return true if the number is prime
		prime number can be divided only by 1 and itself
	'''
    if number > 1:
        for num in range(2, int(number**0.5) + 1):
            if number % num == 0:
                return False
        return True
    return False

''' #################################################
    #                 PYTEST CASES                  #
	#################################################
'''
def test_palindrome():
	value = is_palindrom('dad') 
	assert Value == True

def test_prime_number():
	
	assert is_prime(4) == False
	assert is_prime(5) == True
	assert is_prime(6) == False

def test_reverse():
	value = reverse("abc") 
	assert value == "cba"
	value = reverse([1,2,3]) 
	assert value == [3,2,1]

def test_sum():
	sum_of_two_numbers = sum(2,2)
	assert sum_of_two_numbers == 4