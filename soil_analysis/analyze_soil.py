'''
@author RIT GDSC
@brief This is where we analyze soil sample.
Data Input: Allow users to input soil sample data manually or through sensors.
Data Analysis: Analyze soil properties such as pH, moisture, and nutrient levels.
Tool: Pandas for data manipulation.
'''

def analyze_soil_samples(pH, moisture, nutrients):
    '''
    @brief this is the function where we analyze the soil properties.
    @param pH the given pH, in float.
    @param moisture the moisture level, in float.
    @param nutrients the nutrient levels, in float.
    @return the analysis result, as an array (possibly, I'm not so sure).
    '''
    analysis = {}
    
    if pH < 6.0:
        analysis['pH'] = "Soil is too acidic."
    elif pH > 7.5:
        analysis['pH'] = "Soil is alkaline."
    else:
        analysis['pH'] = "Soil pH is optimal."

    if moisture < 15:
        analysis['Moisture'] = "Soil moisture is too low."
    elif moisture > 35:
        analysis['Moisture'] = "Soil is too wet."
    else:
        analysis['Moisture'] = "Soil moisture is optimal."

    if nutrients < 40:
        analysis['Nutrients'] = "Nutrient levels are low."
    elif nutrients > 70:
        analysis['Nutrients'] = "Nutrient levels are high."
    else:
        analysis['Nutrients'] = "Nutrient levels are optimal."

    return analysis

