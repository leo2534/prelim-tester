filePath = input("enter file path\n: ")
delimiter = input("enter delimiter\n: ")
questions = []
answers = []

# Source - https://stackoverflow.com/a
# Posted by Martijn Pieters, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-04, License - CC BY-SA 4.0

import os

with open("C:/Users/PughL14/OneDrive - Hutchesons' Grammar School/ICT/Co-curricular programming/visual studio/projects/prelim tester/websites/quotes.json", 'rb+') as filehandle:
    filehandle.seek(-3, os.SEEK_END)
    filehandle.truncate()




with open(filePath, "r") as file:
    for line in file:
        dummy = ""
        for character in line:
            if character == delimiter:
                questions.append(dummy)
                dummy = ""
            elif character == '"':
                dummy += "\\"
                dummy += '"'
            else:
                dummy += character
        answers.append(dummy[:-1])
        



outputName = filePath[:-4]
with open("C:/Users/PughL14/OneDrive - Hutchesons' Grammar School/ICT/Co-curricular programming/visual studio/projects/prelim tester/websites/quotes.json", "a") as file:
    contents = ',\n"' + outputName + '":[\n'
    print(questions)
    print(answers)
    for index in range(0,len(answers)):
        print(index)
        contents += '   {   "question":"' + questions[index]
        contents += '", "answer":"' + answers[index] + '"},\n'
    contents = contents[:-2] + "\n"
    contents += ']\n\n}'
    
    file.write(contents)
