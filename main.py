from tkinter import *
from random import choice
from random import shuffle
from tkinter import messagebox


root = Tk()
root.title('Word Jumble')
root.geometry("800x400")
root.iconbitmap("./icon.ico")

# Create label to display scrambled word
myLabel = Label(root, text="", font=("Helvetica", 50))
myLabel.pack(pady=20)

# Initialize game score and time left
score = 0
timeleft = 120

def startGame(event):
    """
     This function starts the timer countdown, displays the scrambled word, updates the score, and informs
     the player whether the reconstructed word is correct or incorrect
    """
    if timeleft == 120:
        countdown()
        shuffler()
        scorelabel.config(text="Score: 0")
    else:
        answer()


def countdown():
    """
    This function decrements the timer and displays the time left.
    """
    global timeleft
    if timeleft == 0:
        messagebox.showinfo(
            "Time Over", "Time is over and your score is " + str(score))
    if timeleft > 0:
        timeleft -= 1
        timelabel.config(text="Time Left: " + str(timeleft))
        timelabel.after(1000, countdown)


def shuffler():
    """
    This function randomly picks the name of a country and scrambles the word.
    """

    # Clear text box
    eAnswer.delete(0, END)
    # ansLabel.config(text="")
    # Clear label
    ansLabel.after(400, lambda: ansLabel.config(text=''))

    global word

    Countries = ['Egypt', 'Sudan', 'Oman', 'Yemen', 'Syria', 'Algeria', 'Qatar', 'Lebanon', 'Tunisia', 'Libya',
                 'Kuwait', 'Jordan', 'Iraq', 'France', 'Germany', 'Spain', 'China', 'India', 'Canada', 'Brazil',
                 'Italy', 'Poland', 'Sweden', 'Norway', 'Greece', 'Netherlands', 'Japan', 'Iran', 'Portugal', 'Mexico',
                 'Cuba', 'Argentina', 'Colombia', 'Nigeria', 'South Africa', 'Ghana', 'United States of America', 'Liberia',
                 'Uganda', 'Cameroon', 'Kenya', 'Algeria', 'Mali', 'Somalia', 'Zimbabwe', 'Sierra Leone', 'Congo',
                 'Central African Republic', 'Mauritania', 'Libya', 'Togo', 'Tunisia', 'Gabon', 'Guinea-Bissau', 'Equatorial Guinea',
                 'Comoros', 'Seychelles', 'Djibouti', 'Sao Tome & Principe', 'Cabo Verde', 'Botswana', 'Benin', 'Rwanda', 'Chad', 'Senegal'
                 'Burkina Faso', 'Morocco', 'Mozambique', 'Madagascar', 'Côte d\'Ivoire', 'Niger', 'Angola', 'Malawi', 'Ethiopia',
                 'Tanzania', 'DR Congo']

    word = choice(Countries)

    breakWord = list(word)
    shuffle(breakWord)

    global shuffled
    shuffled = ''
    for letter in breakWord:
        shuffled += letter

    # Display scrambled word
    myLabel.config(text=shuffled)


def answer():
    """
     This function does the following: 
      - Compares and determines if the randomly chosen word matches the reconstructed word.  
      - Displays the next scrambled word.
    """
    global score
    global timeleft

    if timeleft > 0:
        eAnswer.focus_set()
        if eAnswer.get().lower() == word.lower():
            score += 1
            ansLabel.config(text="Correct!")
        else:
            ansLabel.config(text="Incorrect")
        scorelabel.config(text="Score: " + str(score))

        shuffler()


# Create label to display score
scorelabel = Label(root, text="Enter to start", font=('Helvetica', 24))
scorelabel.pack()

# Create label to display remaining time left
timelabel = Label(root, text="Time left: " +
                  str(timeleft), font=('Helvetica', 12))
timelabel.pack()

# Create textbox to enter reconstructed word
eAnswer = Entry(root, font=("Helvetica", 25))
eAnswer.pack(pady=20)

# Create frame to arrange other widgets
myFrame = Frame(root)
myFrame.pack(pady=20)

# Create button to show answer when clicked
ansButton = Button(myFrame, text="Answer!", command=answer)
ansButton.grid(row=0, column=1, padx=10)

# Create label to show whether the reconstructed word is correct or incorrect
ansLabel = Label(root, text="", font=("Helvetica", 20))
ansLabel.pack(pady=20)

# Show new scrambled word when button is pressed
root.bind('<Return>', startGame)
eAnswer.focus_set()


root.mainloop()
