import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("students.csv")

print("Student Data:")
print(data)

# Calculate average marks
data["Average"] = data[["Math","Physics","English"]].mean(axis=1)
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

data["Grade"] = data["Average"].apply(grade)

print("\nStudent Grades:")
print(data[["Name","Average","Grade"]])
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

data["Grade"] = data["Average"].apply(get_grade)

print("\nStudent Grades:")
print(data[["Name","Average","Grade"]])
print("\nStudent Averages:")
print(data[["Name","Average"]])

# Find topper
topper = data.loc[data["Average"].idxmax()]

print("\nTopper of the class:")
print(topper["Name"], topper["Average"])

# Calculate subject averages
subject_avg = data[["Math","Physics","English"]].mean()

print("\nSubject Average Marks:")
print(subject_avg)

# Create graph
subject_avg.plot(kind="bar")

plt.title("Subject Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()
grade_counts = data["Grade"].value_counts()

plt.figure()
grade_counts.plot(kind="pie", autopct="%1.1f%%")

plt.title("Grade Distribution")
plt.ylabel("")

plt.show()

