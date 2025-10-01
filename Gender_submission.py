import pandas as pd
import matplotlib.pyplot as mp
gendersubmission = pd.read_csv("gender_submission.csv")
print(gendersubmission.head(40))
gendersubmission.rename(columns= {"PassengerId":"Number"},inplace=True)
print(gendersubmission)
filter = gendersubmission[gendersubmission["Survived"]==1]
print(filter)
totalPass = gendersubmission["Survived"].value_counts()
Total = len(gendersubmission)
a = totalPass[0]
percent = (a / Total) * 100
print(f"Percentage of non-survivors is: {percent:.2f}%")
totalPass.plot(kind = 'bar', color = ["Blue", "Red"])
mp.xlabel("Survived People")
mp.ylabel("Non-Survived People")
mp.title("Survived Passenger In The Flight")
mp.xticks(rotation=0)
mp.yticks(rotation=20)
mp.show()