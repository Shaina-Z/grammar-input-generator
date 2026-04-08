from main import expr
from hypothesis import given


@given(expr())
def test_print(expr: str):
  print(expr)