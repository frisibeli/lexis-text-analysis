# Lexis - emotion detection in text

Lexis is web based application that analyzes given user text input using SVM and shows the emotion(s) in the text. The model is trained on more than 75k tweets, seperated in six categories, based on their hashtag: anger, disgust, fear, happiness, irony, neutral, sadness, sarcasm, surprise.

#### Hackathon winning project

![Demo](images/winners.jpg)
Lexis was created at a hackathon (HackFMI 8 - hack for data) by me and 5 other university coleagues.
The code in this repository is "cleaner" and refactored version of what we presented (the original repository can be seen [here](https://github.com/emil-kirilov/lexis)). Also here I am using React for UI.

## Getting Started

Make sure you have Python3, virtualenv and NodeJS installed on your system. 

#### Clone the repository

```
git clone https://github.com/frisibeli/lexis-text-analysis.git
```

#### Initialize and activate virtualenv

```
cd lexis-text-analysis/backend
virtualenv -p python3 .
source bin/activate
```

### Installing

Assuming that you have already initialized virtualenv and you are in `lexis-text-analysis/backend`:

Install python requirements using pip

```
pip install -r requirements.txt
```

To run the app execute

```
python app.py
```

The app will run on port 8080 by default, but you can change that in app.py
Now go to `lexis-text-analysis/frontend` and execute `npm install`

To run the webapp execute `npm start` in the frontend directory.

## Demo
![Demo](images/demo.gif)

## Built With

* [React](https://reactjs.org/) - JavaScript library for building user interfaces
* [Flask](http://flask.pocoo.org/) - Flask is a micro web framework written in Python.
* [Scikit learn](https://scikit-learn.org) - free software machine learning library for Python 
