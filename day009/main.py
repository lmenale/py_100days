# The Python Dictionary

# Scoring criteria
# Scores 91-100: Grade = "Outstanding"
# Scores 81 -90: Grade = "Exceeds Expectations"
# Scores 71-80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

# Create an empty dictionary.
student_grades = {}

# Loop through a dictionary
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)

# Nesting Lists and Dictionaries
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}
#Nesting a List in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}
#Nesting a Dictionary in a List
travel_log = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
  },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
  },
]