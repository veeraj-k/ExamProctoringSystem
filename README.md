# Examination Proctoring System
This project is an examination proctoring system developed using Python. It leverages OpenCV for movement detection to ensure the integrity of the examination process and provides a user interface built with PyQt5 and Tkinter. The system captures video to monitor the test-taker and presents a quiz through a graphical user interface.


## Features

- Real-time video feed and movement detection
- Quiz interface with multiple-choice questions
- Supports multiple tests
- Records user violations during the test

## Technologies Used

- Python
- OpenCV for video processing
- PyQt5 for user interface
- Tkinter for quiz interface
- MySQL for storing user details
  
## Setup and Installation

### Prerequisites

- Python 3.8.3
- MySQL 
- Virtual environment (recommended)
  
### Installation
1. Clone the repository:
   
   ```bash
        git clone https://github.com/veeraj-k/ExamProctoringSystem.git
        cd ExamProctoringSystem
   ```
2. Create and activate [virtual environment](https://docs.python.org/3/tutorial/venv.html)
   ```bash
   python -m venv venv
   source venv/bin/activate     #Unix or macOs
   source venv\Scripts\activate   #Windows 
   ```
3. Install required packages:
4. ```bash
   pip install -r requirements.txt
   ```
### Usage
1. Run the main application:
   ```bash
   python main.py
   ```
2. The login screen will appear. Enter your details and select the test you want to take.

3. Once the test starts, the system will monitor your activity using the webcam and present the quiz.

4. After completing the quiz, submit your answers, and the system will stop monitoring.
### Adding test
You can add custom tests my creating a data_[index].json file in this format and by adding in the myQuiz class to apply the changes .
```javascript
{
  "ques": [],
  "ans": [],
  "choices": [[]]
}
```
