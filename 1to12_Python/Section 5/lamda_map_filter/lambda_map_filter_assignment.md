# 📘 Python Assignment – Lambda, Map, and Filter

---

## Part A – Basics

### 1. Write a lambda function to add 10 to a given number.
```python
add_10 = lambda x: x + 10
print(add_10(5))   # 15
```

---

### 2. Use a lambda function to find the square of a number.
```python
square = lambda x: x ** 2
print(square(7))   # 49
```

---

### 3. Use `map` and a lambda function to square each number in a list.
```python
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)   # [1, 4, 9, 16, 25]
```

---

### 4. Use `filter` and a lambda function to get only even numbers from the list.
```python
nums = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [10, 20, 30]
```

---

## Part B – Intermediate

### 5. Convert each word to uppercase using `map` and lambda.
```python
words = ["python", "lambda", "map", "filter"]
upper_words = list(map(lambda w: w.upper(), words))
print(upper_words)   # ['PYTHON', 'LAMBDA', 'MAP', 'FILTER']
```

---

### 6. Extract numbers greater than 50 using `filter`.
```python
numbers = [34, 67, 89, 12, 56, 99, 10]
greater_50 = list(filter(lambda x: x > 50, numbers))
print(greater_50)   # [67, 89, 56, 99]
```

---

### 7. Calculate length of each word using `map` and lambda.
```python
fruits = ["apple", "banana", "cherry", "kiwi"]
lengths = list(map(lambda f: len(f), fruits))
print(lengths)   # [5, 6, 6, 4]
```

---

### 8. Keep only perfect squares using `filter`.
```python
nums = [4, 5, 9, 12, 16, 20, 25]
perfect_squares = list(filter(lambda x: int(x**0.5)**2 == x, nums))
print(perfect_squares)   # [4, 9, 16, 25]
```

---

## Part C – Advanced

### 9. Get only people aged 18 or above using `filter`.
```python
people = [("Alice", 17), ("Bob", 20), ("Charlie", 16), ("David", 25)]
adults = list(filter(lambda p: p[1] >= 18, people))
print(adults)   # [('Bob', 20), ('David', 25)]
```

---

### 10. Extract only names using `map` and lambda.
```python
names = list(map(lambda p: p[0], people))
print(names)   # ['Alice', 'Bob', 'Charlie', 'David']
```

---

### 11. Find squares of even numbers using `map` and `filter`.
```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(even_squares)   # [4, 16, 36, 64, 100]
```

---

### 12. Lambda function to return the greater of two numbers.
```python
greater = lambda x, y: x if x > y else y
print(greater(10, 20))   # 20
```

---

## Bonus Challenge

### 13. Count the number of vowels in each word of a sentence using `map` and lambda.
```python
sentence = "Lambda functions are powerful in Python"
words = sentence.split()
vowel_count = list(map(lambda w: sum(1 for c in w.lower() if c in 'aeiou'), words))
print(vowel_count)   # [2, 3, 2, 3, 1, 1]
```

---

### 14. Extract words with more than 5 letters using `filter`.
```python
words = sentence.split()
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)   # ['functions', 'powerful', 'Python']
```
