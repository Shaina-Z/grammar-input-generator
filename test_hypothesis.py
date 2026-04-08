from main import expr
from hypothesis import given

# When thinking about the inputs we have been talking about in class, most of them
# were decided with set parameters or types of inputs in mind, such as when we 
# were partioning tests based on unique characteristics. However, hypothesis 
# randomly generates the inputs, which can lead to a greater variety of test cases.
# This help us test the boundaries of our code and allows us todiscover edge cases 
# and unexpected behaviors in our code that we might not have been aware of when 
# we were deciding on the criteria for our tests.
@given(expr())
def test_print(expr: str):
  print(expr)