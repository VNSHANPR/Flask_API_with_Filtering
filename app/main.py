from fastapi import FastAPI
from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from flask import Flask 
from flask_cors import CORS
from flask import request
import requests

from flask import jsonify, make_response, request, Blueprint,render_template,redirect,url_for


#Flask Code 
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def root(amount:int=10,category:str="AI",difficulty:str="hard",type:str="mulitple"):
    category=request.args.get("category")
    difficulty=request.args.get("difficulty")
    type=request.args.get("type")
    amount=int(request.args.get("amount"))
    print(category,amount,type,difficulty)
    headers={'Authorization': 'Bearer <PUT YOUR PERSONAL ACCESS TOKEN for PRIVATE REPOSITORY>'}

    data_from_git=requests.get('https://raw.githubusercontent.com/VNSHANPR/Flask_API_with_Filtering/main/questions_answers.json',headers=headers)
    data_json=data_from_git.json()

    if category not in set(list([n['category'] for n in list(filter(lambda a: True if a["category"]==category else False,data_json["results"]))])):
        response_code=1
    elif type not in set(list([n['type'] for n in list(filter(lambda a: True if a["type"]==type else False,data_json["results"]))])):
        response_code=1
    else:
        response_code=0

    return {"response_code": response_code,
    "results": list(filter(lambda a: True if a["category"]==category and a["difficulty"]==difficulty and a["type"]==type else False,data_json["results"]))[:amount]
    }

@app.route('/categories')
def catgories_fetch():
    headers={'Authorization': '<PUT YOUR PERSONAL ACCESS TOKEN for PRIVATE REPOSITORY>'}

    categories_from_git=requests.get('https://raw.githubusercontent.com/VNSHANPR/Flask_API_with_Filtering/main/categories.json',headers=headers)
    categories_data_json=categories_from_git.json()
 
    return categories_data_json
    


if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=8080)


#Fast API code
#app = FastAPI()
#app.add_middleware(
  #  CORSMiddleware,
  #  allow_origins=["*"],
  #  allow_credentials=True,
   # allow_methods=["*"],
  ##  allow_headers=["*"],
#)

# below is the code in Fast API
#@app.get("/")
#async def root(amount:int=10,category:str="SAP AI",difficulty:str="hard",type:str="multiple"):
 #   return {"response_code": 0,
  #  "results": list(filter(lambda a: True if a["category"]==category and a["difficulty"]==difficulty and a["type"]==type else False,a["results"]))[:amount]
  #  }

#if __name__ == "__main__":
 #   uvicorn.run(app, port=8080)



    
