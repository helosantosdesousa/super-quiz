import pandas as pd

questions = [
    ['Who was the first person to write an algorithm?', 'Ada Lovelace', 'Alan Turing', 'Beyoncé', 'Marie Curie', 1],
    ['What do we use to type on a computer?', 'Monitor', 'Mouse', 'Keyboard', 'Pen drive', 3],
    ['What do we use to browse the internet?', 'Scanner', 'Printer', 'Spreadsheet', 'Browser', 4],
    ['Which one is a social media platform?', 'Excel', 'Instagram', 'Photoshop', 'Python', 2],
    ['Which device shows what is happening on the computer?', 'USB stick', 'Monitor', 'Mouse', 'Keyboard', 2],
    ['Which of these is used to move the cursor?', 'Camera', 'Router', 'Speaker', 'Mouse', 4],
    ['What does Wi-Fi allow you to do?', 'Draw pictures', 'Watch TV', 'Print papers', 'Connect to the internet', 4],
    ['Which one is a famous computer brand?', 'Carrot', 'Banana', 'Orange', 'Apple', 4],
    ['What is the brain of the computer called?', 'USB', 'CPU', 'HDMI', 'RAM', 2],
    ['Which of these can store files?', 'Pen drive', 'Charger', 'Mouse pad', 'Cable', 1],
    ['What does a password protect?', 'Your monitor', 'Your data', 'Your charger', 'Your keyboard', 2]
]

# Creates pandas dataframe
df = pd.DataFrame(questions, columns=['Quetions', 'Option 1', 'Option 2', 'Option 3', 'Option 4', 'Answer'])

df.to_excel('questions.xlsx', index=False)
print('Questions inserted into Excel successfully.')
