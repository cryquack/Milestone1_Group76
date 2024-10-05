# Unit Testing Report

### GitHub Repository URL: https://github.com/cryquack/Milestone1_Group76.git

---

The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to 
the five required features.</span> There is no need to test the GUI components. Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.


## 1. **Test Summary**
list all tested functions related to the five required features and the corresponding test functions designed to test 
those functions, for example:

| **Tested Functions** | **Test Functions**                               |
|----------------------|--------------------------------------------------|
| `add(x1,x2)`         | `test_add_valid()` <br> `test_add_invalid`       |
| `divide(x1,x2)`      | `test_divide_valid()` <br> `test_divide_invalid` |
|`filter_by_nutrition_level(food, level)`	    | `test_filter_low() ` <br> ` test_filter_mid() ` <br> ` test_filter_high()`      |
| `calculate_nutrition_density(food_list)`      | `test_calculate_density()` |
| `find_food_by_name(food_list, name)`         | `test_find_food_valid() ` <br> ` test_find_food_invalid()`       |
| `sort_foods_by_calories(food_list) `     | `test_sort_foods`|
| `compare_foods(food1, food2)	 `     | `test_compare_foods_valid() ` <br> ` test_compare_foods_invalid()`|


---

## 2. **Test Case Details**

### Test Case 1:
- **Test Function/Module**
  - `test_divide_valid()`
  - `test_divide_invalid()`
- **Tested Function/Module**
  - `divide(a, b)`
- **Description**
  - A brief description of the tested function's usage, including its purpose, input, and output.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```
### Test Case 2:
- **Test Function/Module**
  - `test_filter_low()`
  - `test_filter_mid()`
  - `test_filter_high()`
- **Tested Function/Module**
  - `filter_by_nutrition_level(food, level)`
- **Description**
  -The filter_by_nutrition_level function filters a list of food items based on a specified nutritional level ('low', 'mid', or 'high'). It returns a list of foods that match the given level criteria.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `filter_by_nutrition_level(food_list, 'low')`               | `List of foods with low nutritional levels`                 |
| `filter_by_nutrition_level(food_list, 'mid')`              | `List of foods with mid nutritional levels
`                |
| `filter_by_nutrition_level(food_list, 'high')` | `List of foods with high nutritional levels`               |

- **1) Code for the Test Function**
```python
def test_filter_low():
    result = filter_by_nutrition_level(food_list, 'low')
    assert len(result) == expected_low_count

def test_filter_mid():
    result = filter_by_nutrition_level(food_list, 'mid')
    assert len(result) == expected_mid_count

def test_filter_high():
    result = filter_by_nutrition_level(food_list, 'high')
    assert len(result) == expected_high_count
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 3:
- **Test Function/Module**
  - `test_calculate_density()`
- **Tested Function/Module**
  - `calculate_nutrition_density(food_list)`
- **Description**
  - The calculate_nutrition_density function calculates the nutritional density of a list of food items, which could be based on a formula like nutritional value per 100g. It returns a dictionary or list of items with calculated densities.

- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `calculate_nutrition_density(food_list)`               | `Dictionary/list with nutritional density values`                 |

- **1) Code for the Test Function**
```python
def test_calculate_density():
    result = calculate_nutrition_density(food_list)
    assert isinstance(result, list)  # or dict, depending on the implementation
    assert len(result) == len(food_list)  # Ensure all items were processed

```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 4:
- **Test Function/Module**
  - `test_find_food_valid()`
  - `test_find_food_invalid()`
- **Tested Function/Module**
  - `find_food_by_name(food_list, name)`
- **Description**
  - The find_food_by_name function searches for a food item by name from a given list of foods. It returns the food item if found, otherwise returns None.

- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `ind_food_by_name(food_list, 'Apple')`               | `Food item dictionary for 'Apple'`                 |
| `find_food_by_name(food_list, 'Banana')`              | `Food item dictionary for 'Banana'`                |

- **1) Code for the Test Function**
```python
def test_find_food_valid():
    apple = find_food_by_name(food_list, 'Apple')
    assert apple['name'] == 'Apple'

def test_find_food_invalid():
    unknown_food = find_food_by_name(food_list, 'Unknown')
    assert unknown_food is None
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```


### Test Case 5:
- **Test Function/Module**
  - `test_sort_foods()`
- **Tested Function/Module**
  - `sort_foods_by_calories(food_list)`
- **Description**
  - The sort_foods_by_calories function sorts a list of food items based on their calorie content, in ascending or descending order. It returns the sorted list.

- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `sort_foods_by_calories(food_list)`               | `List sorted by calorie content (ascending/descending)`                 |


- **1) Code for the Test Function**
```python
def test_sort_foods():
    sorted_foods = sort_foods_by_calories(food_list)
    assert sorted_foods == sorted(food_list, key=lambda x: x['calories'])

```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 6:
- **Test Function/Module**
  - `test_compare_foods_valid()`
  - `test_compare_foods_invalid()
`

- **Tested Function/Module**
  - `compare_foods(food1, food2)`
- **Description**
  - The compare_foods function compares two food items based on attributes such as calorie content or nutritional value. It returns a comparison result (e.g., "Food1 has more calories than Food2").


- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `compare_foods(food_item1, food_item2)`               | `"Banana has more calories than Apple"`                 |


- **1) Code for the Test Function**
```python
def test_compare_foods_valid():
    result = compare_foods(food_item1, food_item2)
    assert result == "Banana has more calories than Apple"
def test_compare_foods_invalid():
    invalid_food = {"name": "Banana", "calories": 105}  # Missing other attributes
    with pytest.raises(KeyError) as exc_info:
        compare_foods(food_item1, invalid_food)
    assert exc_info.type is KeyError


```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

## 3. **Testing Report Summary**
Include a screenshot of unit_test.html showing the results of all the above tests. 

You can use the following command to run the unit tests and generate the unit_test.html report.

```commandline
pytest test_all_functions.py --html=unit_test.html --self-contained-html
```
Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related 
to the five required features.

![unit_test_summary](./Unit_test.png)
