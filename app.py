'''
@author RIT GDSC.
@brief User-friendly interface.
Tools: Flask, pandas, Scikit-learn, and joblib.
'''
from flask import Flask, request, render_template
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Import your modules for image processing and soil analysis
from image_processing.crop_scan import process_crop_image
from soil_analysis.analyze_soil import analyze_soil_samples

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('model/random_forest_model.pkl')

@app.route('/', methods=['GET', 'POST'])

def index():
    '''
    @brief the function to run the UI of the app.
    @return the template from the index.html.
    '''
    prediction = None
    if request.method == 'POST':
        # Get data from form
        pH = float(request.form['pH'])
        moisture = float(request.form['moisture'])
        nutrients = float(request.form['nutrients'])

        # Use soil analysis module (optional, for demonstration)
        soil_info = analyze_soil_samples(pH, moisture, nutrients)

        # Create a DataFrame for the input
        input_data = pd.DataFrame([[pH, moisture, nutrients]], columns=['pH', 'Moisture', 'Nutrients'])

        # Make prediction
        prediction = model.predict(input_data)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    '''
    This is our main program to run the function above.
    '''
    app.run(debug=True)