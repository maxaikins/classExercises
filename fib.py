
# cache that allows us to avoid doing the same calculation a million times and using all of our memory
# the data is stored in the form 

# key = fibonnaci number
# value = resulting value

# so cache[fibbonaci number] = fibbonaci number value

cache = {
    0:0,
    1:1,
}



def fib(num):
    # check the cheapest option first. If the number has already been calculated, look it up in the cache and return it
    if num in cache:
        return cache[num]

# base case
    if num == 0:
        return 0
    if num == 1:
        return 1

    # Save fib number calculations in variables so that we can add them to cache before it is returned
    first = fib(num - 1)
    second = fib(num - 2)


# check if either or both of the 2 calculations done for the current fib number are in the cache, if not add them
    if num-1 not in cache:
        cache[num-1] = first

    if num-2 not in cache:
            cache[num-2] = first


# return the result of the current fib number
    return first + second


fib_number = 900

# do the calculation with ("target number" - 1)
# this makes it print the nth value in the sequence given n as an input
# series for reference below

# 0,1,1,2,3,5,8,13,21,34

# 1,2,3,4,5,6,7, 8, 9,10

print(fib(fib_number - 1))