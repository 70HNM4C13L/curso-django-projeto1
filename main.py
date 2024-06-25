def teste():
    assert 1 == 2


try:
    teste()
    print("Hello World!")
except AssertionError:
    print("Test Failed")

