from flask import Flask, jsonify, render_template, request
from project_app.utils import FloType

# Creating instance here
# 'app' is standard variable
app = Flask(__name__)

# @app.route("/") --> USED TO GET HOME API
# @app.route("/furniture") --> You will get 'Furniture' Page here

@app.route("/")
def hello_flask():
    print("Welcome to Product Sales Prediction")
    return render_template("index.html")


@app.route("/predict_charges",methods=["POST","GET"])
def get_flo_pre():
    if request.method =="GET":
        print("We are in a GET Method")
                
    
        SepalLengthCm=float(request.args.get("SepalLengthCm"))
        SepalWidthCm=float(request.args.get("SepalWidthCm"))
        PetalLengthCm=float(request.args.get("PetalLengthCm"))
        PetalWidthCm=float(request.args.get("PetalWidthCm"))
        

    
    else:
        print("error in if block")
        


    flo_pri=FloType(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    charges=flo_pri.get_predicted()
    if charges == 1:
        charges_text = "Iris-versicolor"
    else:
        charges_text = "Iris-virginica"
    return render_template("index.html",prediction=charges_text)


print("__name__-->",__name__)
if __name__=="__main__":
    #app.run(host="0.0.0.0",post=5000,debug=false)
    app.run()



