#student information system:creates a program that stores and displays student information,such as name,age,grades,courses and using strings,integers,floats, list and dictionaries.
#name=string,age=integer,grades=list,courses=dictionary.
#student data
student_name="john"#string
student_age=20#integer
student_marks=[90,98,99]#list
student_courses={"ajay":"A","vinay":"B","vijay":"C"}#dictionary
student_Cgpa=98.8#float
student_scholarship=True#boolean
student_scholarship_money=900+2j#complex
student_subjects=("maths","physics","chemistry")#tuple
student_subject_code={1,2,3}#set
#display student data
print(student_name,type(student_name))
print(student_age,type(student_age))
print(student_marks,type(student_marks))
print(student_courses,type(student_courses))
print(student_Cgpa,type(student_Cgpa))
print(student_scholarship,type(student_scholarship))
print(student_scholarship_money,type(student_scholarship_money))
print(student_subjects,type(student_subjects))
print(student_subject_code,type(student_subject_code))
#calculate student grades:
def calculate_grade(marks):
    if marks >= 90:
        return "a"
    elif marks >= 80:
        return "b"
    elif marks >= 70:
        return "c" 
    elif marks >= 60:
        return "d"
    else:
        return "f"
print("student grade:",calculate_grade(sum(student_marks)/len(student_marks)))   
# logic behind:calculate_garde(sum(student_marks)/len(student_marks)) 
# student_marks=[90,98,99]
#90 and above:"A",80-89:"B",70-70:"C",60-69="D",59 and before:"F"
# sum(student_marks)=90+80+70+60=287
# sum(len(student_marks))=3
# sum(student_marks/lrn(student_marks))=287/3=95.333

#movie database:
# this code defines a simple movie database that store information about a movie,including its title,genre,rating, and cast.
movie_title="krsihna"#string
movie_genre="action"#string
movie_rating=8.5#float
movie_cast=["ajay", "abdul","khan"]#list
print("movie_title:",movie_title)
print("movie_genre:",movie_genre)
print("movie_rating:",movie_rating)
print("movie_cast:",movie_cast)
print(type(movie_title))
print(type(movie_genre))
print(type(movie_rating))
print(type(movie_cast))

# Personal Finance Manager:
#As a responsible individual, managing your finances effectively is crucial for achieving financial stability stability and security.in this example,we'll demonstrate how to use python to create a simple personal finance manager.
income=5000#int
expenses=[1000,2000,300]#list
budget=2500#int
print("income:",income)
print("expenses:",expenses)
print("budget:",budget)
print(type(income))
print(type(expenses))
print(type(budget))

# Weather Forecast:
this code is a simple weather forecast program that stores and displays temperature,humidity and wind spedd data.the program utilizes python's basic integer datatype to reprsent the weather data and prints out the values along with their respective data types.
temperature=25#int
humidity=60#int
wind_speed=10#int
print("temperature:",temperature)
print("humidity:",humidity)
print("wind_speed:",wind_speed)
print(type(temperature))
print(type(humidity))
print(type(wind_speed))

# Quiz Program:
# it is a simple quiz program that stores and displays  a question and its corresponding answer.the program utilizes python's list datatype to represent the questions and answers, and print out the values along with their respective datatype.
questions=["what is python?"]#list
answers=["programming langauge"]#list
print("questions:",questions)
print("answers:",answers)
print(type(questions))
print(type(answers))


# To-Do List App:
#a simple to-do list app created using python,demonstrating how to store and display tasks using python's list datatype
tasks=["buy milk","buy curd"]
print("tasks:",tasks)
print(type(tasks))

# Recipe Book:
#A simple Recipe Book program created using Python, storing and displaying recipe details such as name, ingredients, and instructions using Python's string and list data types.
recipe_name="chicken soup"#string
ingredients=["chicken","vegetables","broth"]#list
instructions=["boil chicken and vegetables in broth","season with salt and pepper"]#list
print("reciepe name:",recipe_name)
print("ingredients:",ingredients)
print("instructions:",instructions)
print(type(recipe_name))
print(type(ingredients))
print(type(instructions))


# Music Library:
#A simple Music Library program created using Python, storing and displaying song titles and artist names using Python's list data type.
song_titles=["song1","song2","song3"]#list
artist_names=["artist1","artist2","artist3"]#list
print("song titles:",song_titles)
print("artist names:",artist_names)
print(type(song_titles))
print(type(artist_names))


# Sports Team Manager:
#A simple Sports Team Manager program created using Python, storing and displaying team name and player names using Python's string and list data types.
team_name="team A"#string
player_names=["player 1","player 2","player 3"]#list
print("team name:",team_name)
print("player names:",player_names)
print(type(team_name))
print(type(player_names))
