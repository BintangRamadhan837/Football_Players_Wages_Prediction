from flask import Flask, request, jsonify
import pickle
import pandas as pd


app = Flask(__name__)

with open('model_ridge.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

columns = ['preferred_foot','age','overall','potential','value','international_reputation','weak_foot','skill_moves','height','weight','crossing','finishing','headingaccuracy','shortpassing','volleys','dribbling','curve','fkaccuracy','longpassing','ballcontrol','acceleration','sprintspeed','agility','reactions','balance','shotpower','jumping','stamina','strength','longshots','aggression','interceptions','positioning','vision','penalties','composure','marking','standingtackle','slidingtackle']

@app.route("/") #homepage
def hello_world():
    return '<h1>It Works</h1>'

@app.route("/predict", methods=['GET','POST']) #homepage
def model_prediction():
    if request.method == 'POST':
        content = request.json

        try:
            data =  [content['preferred_foot'],
                    content['age'],
                    content['overall'],
                    content['potential'],
                    content['value'],
                    content['international_reputation'],
                    content['weak_foot'],
                    content['skill_moves'],
                    content['height'],
                    content['weight'],
                    content['crossing'],
                    content['finishing'],
                    content['headingaccuracy'],
                    content['shortpassing'],
                    content['volleys'],
                    content['dribbling'],
                    content['curve'],
                    content['fkaccuracy'],
                    content['longpassing'],
                    content['ballcontrol'],
                    content['acceleration'],
                    content['sprintspeed'],
                    content['agility'],
                    content['reactions'],
                    content['balance'],
                    content['shotpower'],
                    content['jumping'],
                    content['stamina'],
                    content['strength'],
                    content['longshots'],
                    content['aggression'],
                    content['interceptions'],
                    content['positioning'],
                    content['vision'],
                    content['penalties'],
                    content['composure'],
                    content['marking'],
                    content['standingtackle'],
                    content['slidingtackle']]
            data = pd.DataFrame([data], columns=columns)
            res = model.predict(data)
            response = {'code':200,
                        'status':"Success",
                        'data':{'result':str(res[0])}
                        }
            return jsonify (response)
        except Exception as e:
            response = {'code':500,
                        'status':"error",
                        'summary': str(e)}
            return jsonify (response)
        
    return "silahkan gunakan method post"
    