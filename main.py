from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz", methods=["POST"])
def quiz():
    # extract data from form
    if request.method == "POST":
        # get answers from form 
        question1 = request.form.get("question1")
        question2 = request.form.get("question2")
        question3 = request.form.get("question3")
        question4 = request.form.get("question4")
        question5 = request.form.get("question5")
        question6 = request.form.get("question6")
        question7 = request.form.get("question7")
        question8 = request.form.get("question8")
        question9 = request.form.get("question9")
        question10 = request.form.get("question10")

        # validate answers 

        # question 1 validations
        if question1 == "pasta":
            question1_answer = "CORRECT! My favourite food is pasta with meatballs."
        else:
            question1_answer = "INCORRECT! My favourite food is pasta."

        # question 2 validations 
        
        if question2 == "purple":
            question2_answer = "CORRECT! Purple is my favourite colour"
        else:
            question2_answer = "INCORRECT! My favourite colour is actually purple"


        # question 3 validations
        if question3 == "diary of a wimpy kid":
            question3_answer = "CORRECT! My favourite book in the series is old school"
        else:
            question3_answer = "INCORRECT! My favourite series is diary of a wimpy kid"

        # question 4 validations
        if question4 == "super mario galaxy":
            question4_answer = "CORRECT! This was my childhood game"
        else:
            question4_answer = "INCORRECT! It was actually super mario galaxy"

        # question 5 validations
        if question5 == "wii":
            question5_answer = "CORRECT! The WII is my favourite console, containing super mario galaxy."
        else:
            question5_answer = "INCORRECT! My favourite is actually the WII!"

        # question 6 validations
        if question6 == "basketball":
            question6_answer = "CORRECT! I want to learn basketball, I used to preform for a basketball club!"
        else:
            question6_answer = "INCORRECT! I really want to get back into basketball"


        # question 7 validations
        if question7 == "japan":
            question7_answer = "CORRECT! I would love to go to japan!"
        else:
            question7_answer = "INCORRECT!, I would prefer to go to japan."

        
        # question 8  validations
        if question8 == "arsenal":
            question8_answer = "CORRECT!, I love arsenal"
        else:
            question8_answer = "INCORRECT!, I support arsenal"


        # question 9 validations
        if question9 == "Ratotouie":
            question9_answer = "CORRECT!, I love this movie"
        else:
            question9_answer = "INCORRECT! Ratotouie is by far my favourite"

        
        # question 10 validations
        if question10 == "deadpool":
            question10_answer = "CORRECT!, By far my favourite hero!"
        else:
            question10_answer = "INCORRECT! I love Deadpool"



    



    return render_template(
        "index.html", 
        answer1=question1_answer, 
        answer2=question2_answer, 
        answer3=question3_answer,
        answer4=question4_answer,
        answer5=question5_answer,
        answer6=question6_answer,
        answer7=question7_answer,
        answer8=question8_answer,
        answer9=question9_answer,
        answer10=question10_answer,

    )
    


if "__main__" == __name__:
    app.run(debug = True)
