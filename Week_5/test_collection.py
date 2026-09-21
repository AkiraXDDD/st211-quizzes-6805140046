def test_list_equality():
    assert [1,2,3] == [1,2,3]

def test_list_content():
    result = [3,2,1]
    assert sorted(result) == [1,2,3]

def test_dict_equality():
    expected = {"Name": "Alice", "Age": 30}
    actual = {"Age": 30, "Name": "Alice"}
    assert actual == expected

def test_set_operation():
    assert {1,2,3} & {2,3,4} == {2,3}
    assert {1,2,3} | {2,3,4} == {1,2,3,4}
    assert {1,2,3,4} - {3,4,5,6} == {1,2}
    assert {1,2,3,4} ^ {3,4,5,6} == {1,2,5,6}