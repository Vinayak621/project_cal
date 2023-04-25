from flask import Flask, render_template, request
from flask_cors import cross_origin
app = Flask(__name__,template_folder="templates")

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
@cross_origin()
def calculate():
    cereal_yield = float(request.form['cereal_yield'])
    energy_use_gdp = float(request.form['energy_use_gdp'])
    energy_use_capita = float(request.form['energy_use_capita'])
    co2_gdp = float(request.form['co2_gdp'])

    green_credits = cereal_yield * energy_use_gdp * energy_use_capita / co2_gdp

    return render_template('result.html', green_credits=green_credits)
