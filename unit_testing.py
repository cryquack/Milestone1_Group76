def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5

def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError




def test_filter_low():
    result = filter_by_nutrition_level(food_list, 'low')
    assert len(result) == expected_low_count

def test_filter_mid():
    result = filter_by_nutrition_level(food_list, 'mid')
    assert len(result) == expected_mid_count

def test_filter_high():
    result = filter_by_nutrition_level(food_list, 'high')
    assert len(result) == expected_high_count

def test_filter_invalid():
    with pytest.raises(ValueError) as exc_info:
        filter_by_nutrition_level(food_list, 'invalid')
    assert exc_info.type is ValueError

    with pytest.raises(ValueError) as exc_info:
        filter_by_nutrition_level(food_list, None)
    assert exc_info.type is ValueError



def test_calculate_density():
    result = calculate_nutrition_density(food_list)
    assert isinstance(result, list)  # or dict, it depends on the implementation
    assert len(result) == len(food_list)  # Ensure all items were processed

def test_calculate_density_invalid():
    with pytest.raises(ValueError) as exc_info:
        calculate_nutrition_density(None)
    assert exc_info.type is ValueError

    assert calculate_nutrition_density([]) == []




def test_find_food_valid():
    apple = find_food_by_name(food_list, 'Apple')
    assert apple['name'] == 'Apple'

def test_find_food_invalid():
    unknown_food = find_food_by_name(food_list, 'Unknown')
    assert unknown_food is None

def test_find_food_invalid():
    unknown_food = find_food_by_name(food_list, 'Unknown')
    assert unknown_food is None

    assert find_food_by_name(food_list, '') is None

    with pytest.raises(ValueError) as exc_info:
        find_food_by_name(food_list, None)
    assert exc_info.type is ValueError



def test_sort_foods():
    sorted_foods = sort_foods_by_calories(food_list)
    assert sorted_foods == sorted(food_list, key=lambda x: x['calories'])

def test_sort_foods_invalid():
    with pytest.raises(ValueError) as exc_info:
        sort_foods_by_calories(None)
    assert exc_info.type is ValueError

    assert sort_foods_by_calories([]) == []




def test_compare_foods_valid():
    result = compare_foods(food_item1, food_item2)
    assert result == "Banana has more calories than Apple"
def test_compare_foods_invalid():
    invalid_food = {"name": "Banana", "calories": 105}  # Missing other attributes
    with pytest.raises(KeyError) as exc_info:
        compare_foods(food_item1, invalid_food)
    assert exc_info.type is KeyError


def test_compare_foods_invalid():
    invalid_food = {"name": "Banana", "calories": 105}  # Missing other attributes
    with pytest.raises(KeyError) as exc_info:
        compare_foods(food_item1, invalid_food)
    assert exc_info.type is KeyError

    with pytest.raises(ValueError) as exc_info:
        compare_foods(None, food_item2)
    assert exc_info.type is ValueError




pytest test_all_functions.py --html=unit_test.html --self-contained-html
