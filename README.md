# Flask API with request filtering on JSON 

This is a simple example of using Flask based API with filtering of JSON responses based on fixed filters provided in the query string. 
I had used as a backend for the React App [Quiz App](https://github.com/SafdarJamal/quiz-app) to define custom quizess based on internal documents. 

## How to run the API ?

```
python3 main.py
```
Filtering will work when you use all parameters in the query : 

[http://127.0.0.1:8080/?amount=10&category=AI&difficulty=hard&type=multiple ](http://127.0.0.1:8080/?amount=4&category=AI&difficulty=hard&type=multiple)

<img width="1072" alt="image" src="https://github.com/VNSHANPR/Flask_API_with_Filtering/assets/41034062/2dcdd29a-95e6-45de-bbb9-a318260095b0">

## Use GPT to generate the JSON for the Quizzes 

sample prompt : 

```
Generate 10 multiple choice question answer set featuring technical questions related to Large language models, and output as a JSON using below template , the link property of the JSON should default to the url: “link":"https://chat.openai.com/”

{
            "type": "multiple",
            "difficulty": "easy",
            "category": "AI",
            "question": “What is fundamental technology behind ChatGPT”,
            "correct_answer": “Generative “AI,
            "incorrect_answers": [
                "Its cool",
                "Ethanol",
                "Formaldehyde"
            ],
            "link":""
```

<img width="523" alt="image" src="https://github.com/VNSHANPR/Flask_API_with_Filtering/assets/41034062/1847ef2f-29c8-4a5d-ad31-9fd5ac18acc5">


## Deploy the API in CF

Manifest file is added in the folder

```
cf login 
cf push
```

## Use the deployed API in the React app : [Quizz App](https://github.com/SafdarJamal/quiz-app)

clone the repository & run it locally. 
Navigate to src-->components-->Main--> index.js

update the API url to below for testing : 

const API = `http://127.0.0.1:8080/?amount=${numOfQuestions}&category=${result[0]["text"]}&difficulty=${difficulty}&type=${questionsType}`;

```
const fetchData = () => {
    setProcessing(true);

    if (error) setError(null);
    console.log(CATEGORIES);
    const result = CATEGORIES.filter((word) => word["value"] == category); //defined by me to filter category using
    console.log(result[0]["text"]);
    // const API = `https://opentdb.com/api.php?amount=${numOfQuestions}&category=${category}&difficulty=${difficulty}&type=${questionsType}`;
    //const API = `http://127.0.0.1:8080/?amount=${numOfQuestions}&category=${result[0]["text"]}&difficulty=${difficulty}&type=${questionsType}`;
```
