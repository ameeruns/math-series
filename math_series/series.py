
def fibonacci(input_num): 
 if input_num < 0: 
  print("Incorrect input") 
# First Fibonacci number is 0 
 elif input_num==1: 
    return 0
# Second Fibonacci number is 1 
 elif input_num==2: 
   return 1
 else: 
   return fibonacci(input_num-1)+fibonacci(input_num-2) 

def lucas(input_num): 
 if input_num < 0: 
  print("Incorrect input") 
# First Lucas number is 2
 elif input_num==1: 
    return 2
# Second Lucas number is 1 
 elif input_num==2: 
   return 1
 else: 
   return lucas(input_num-1)+lucas(input_num-2) 

def sum_series(num_check,optional_one=0,optional_two=1):
    if optional_one == 0 and optional_two == 1:
       return fibonacci(num_check)
    elif optional_one == 2 and optional_two == 1:
       return lucas(num_check)
    else:
        print("Incorrect parameter") 