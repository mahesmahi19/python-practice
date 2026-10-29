from students import Student

def test_pass():
    s = Student("Mahi", 80)
    assert s.is_pass()

def test_fail():
    s = Student("Ravi", 35)
    assert not s.is_pass()

def test_pass1():
    s = Student("Mahi", 40)
    assert s.is_pass()

def test_fail1():
    s = Student("Ravi", 39)
    assert not s.is_pass()