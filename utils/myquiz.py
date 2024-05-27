
from tkinter import *  
from tkinter import messagebox as mb  
import json  
import tkinter as tk
import queue
guiWindow = Tk()  
   
guiWindow.geometry("1920x1080")  
guiWindow.wm_attributes('-fullscreen', 'True')

class myQuiz:  
    def __init__(self,question,opts,answer):       
        # setting the question number to 0  
        self.question = question
        self.opts = opts
        self.answer = answer
        self.quesNumber = 0  
  
        self.displayTitle()  
        self.displayQuestion()  

        self.optSelected = IntVar()  
           
        # displaying radio button for the current question and  
        # used to display options for the current question  
        self.options = self.radioButtons()  
           
        # displaying the options for the current question  
        self.displayOptions()  
           
        # displaying the button for next and exit.  
        self.buttons()  
           
        # number of questions  
        self.dataSize = len(question)  
           
        # keeping a counter of right answers  
        self.rightAnswer = 0  
        self.violation_label = Label(guiWindow, text="Violations: 0", font=("ariel", 16, "bold"))
        self.violation_label.place(x=50, y=50)

    def update_violations(self, count):
        self.violation_label.config(text=f"Violations: {count}")
        if count > 5:
            self.submit()
    def displayTitle(self):   
        label = Label(guiWindow, text="Quiz", bg="red",height=2,font = ("ariel", 20, "bold"))       
        label.place(x = 0, y = 2)
        label.pack(fill=tk.X, padx=10, pady=10)  

    def displayQuestion(self):  
        quesNumber = Label(  
            guiWindow,  
            text = self.question[self.quesNumber],  
            width = 60,  
            font = ('ariel', 16, 'bold'),  
            anchor = 'w'  
            )  
        quesNumber.place(x = 500, y = 300)      
    def radioButtons(self):  
        qList = []  
        y_pos = 350  

        while len(qList) < 4:  
            radio_button = Radiobutton(  
                guiWindow,  
                text = " ",  
                variable = self.optSelected,  
                value = len(qList) + 1,  
                font = ("ariel", 14)  
                )  
            qList.append(radio_button)  
            radio_button.place(x = 650, y = y_pos)  
            y_pos += 40  
        return qList  
    def displayResult(self):  
        # calculating the wrong count  
        wrongCount = self.dataSize - self.rightAnswer  
        rightAnswer = f"Correct: {self.rightAnswer}"  
        wrongAnswer = f"Wrong: {wrongCount}"  
             
        the_score = int(self.rightAnswer / self.dataSize * 100)  
        the_result = f"Score: {the_score}%"  
            
        mb.showinfo("Result", f"{the_result} \n{rightAnswer} \n{wrongAnswer}")  
    def checkAnswer(self, quesNumber):  
        if self.optSelected.get() == self.answer[quesNumber]:   
            return True  
    def nextButton(self):  
        if self.checkAnswer(self.quesNumber):   
            self.rightAnswer += 1  
        self.quesNumber += 1  
        if self.quesNumber == self.dataSize:   
            self.displayResult()      
            guiWindow.destroy()  
        else:  
            self.displayQuestion()  
            self.displayOptions()  
    def buttons(self):  
          
        next_button = Button(  
            guiWindow,  
            text = "Next",  
            command = self.nextButton,  
            width = 10,  
            bg = "blue",  
            fg = "white",  
            font = ("ariel", 16, "bold")  
            )  
        next_button.place(x = 750, y = 580)  
           
        quit_button = Button(  
            guiWindow,  
            text = "Submit test",  
            # command = guiWindow.destroy,  
            command = self.submit,  
            width = 15,  
            bg = "black",  
            fg = "green",  
            font = ("calibri", 16, " bold")  
            )  
        quit_button.place(x = 10, y = 90)  
    def submit(self):
        print("Submit")
        guiWindow.destroy()
    def getScore(self):
        return self.rightAnswer
        
    def displayOptions(self):  
        val = 0  
        # deselecting the options  
        self.optSelected.set(0)  
        # looping over the options to be displayed  
        # for the text of the radio buttons.  
        for opt in self.opts[self.quesNumber]:  
            self.options[val]['text'] = opt  
            val += 1  

def startQuiz(violation_queue,testid =""):    
    with open(f'./testdata/data_{testid}.json') as json_file:  
        data = json.load(json_file)  
    question = (data['ques'])  
    opts = (data['choices'])  
    answer = (data[ 'ans'])  
    quiz = myQuiz(question=question,opts=opts,answer=answer)  

    def check_queue():
        try:
            violation_count = violation_queue.get_nowait()
            # Update the Tkinter UI with the violation count
            quiz.update_violations(violation_count)
        except queue.Empty:
            pass
        guiWindow.after(100, check_queue)

    guiWindow.after(100, check_queue)
    guiWindow.mainloop()  
    return quiz.getScore()