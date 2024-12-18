import flask
from flask import request,render_template
import joblib
import pandas as pd
from datetime import timedelta

app = flask.Flask(__name__)
model = joblib.load('flight_model.pkl')


@app.route('/',methods=['GET','POST'])
def doPredict():
  if request.method == 'POST':

    # Departure Date
    dep_date = request.form['dep_date']
    dep_datetime = pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M")

    # Arrival Date
    arr_date = request.form['arr_date']
    arr_datetime = pd.to_datetime(arr_date, format="%Y-%m-%dT%H:%M")

    # Journey Details
    journey_day = dep_datetime.day
    journey_month = dep_datetime.month

    # Departure Time
    dep_hour = dep_datetime.hour
    dep_min = dep_datetime.minute
    
    # Arrival Time
    arr_hour = arr_datetime.hour
    arr_min = arr_datetime.minute

    # Duration
    duration = arr_datetime - dep_datetime

    # Handling duration(for overnight flights)
    if duration.days < 0:
       duration += timedelta(days=1)
    
    # Dur_hour and Dur_minutes
    dur_hour,dur_min = divmod(duration.seconds // 60,60)

    # Source
    sources = {'Kolkata':0,'Delhi':0,'Chennai':0,'Mumbai':0}
    source = request.form['source']
    if source in sources:
        sources[source] = 1

    # Destination
    destinations = {'New_Delhi':0,'Cochin':0,'Kolkata':0,'Delhi':0,'Hyderabad':0}
    destination = request.form['destination']
    if destination in destinations:
        destinations[destination] = 1

    # Total Stops
    total_stops = int(request.form['stops'])

    # Airline
    airlines = {
        'Jet_Airways':0,
        'IndiGo':0,
        'Air_India':0,
        'Multiple_carriers':0,
        'SpiceJet':0,
        'Vistara':0,
        'GoAir':0,
        'Multiple_carriers_Premium_economy':0,
        'Jet_Airways_Business':0,
        'Vistara_Premium_economy':0,
        'Trujet':0
    }
    airline = request.form['airline']
    if airline in airlines:
        airlines[airline] = 1

    # Features
    features = [
      journey_day,
      journey_month,
      dep_hour,
      dep_min,
      arr_hour,
      arr_min,
      dur_hour,
      dur_min,
      total_stops, 
     *sources.values(),
     *destinations.values(),
     *airlines.values()
    ]

    # Prediction
    try:
      prediction = model.predict([features])
      output = f'Estimated flight price: ₹{round(prediction[0], 2)}'
    except Exception as e:
      output = f"Error in prediction: {str(e)}"


    return render_template('index.html',prediction = output)
  
  return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)