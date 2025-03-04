from flask import render_template, request, flash
from app import app
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions

# Set up Watson NLU
authenticator = IAMAuthenticator('your_api_key')  # Replace with your API key

 
authenticator = IAMAuthenticator(MY_API_KEY)  # Replace with your API key

nlu = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)
# nlu.set_service_url('your_service_url')  # Replace with your service URL
nlu.set_service_url(SERVICE_URL)

print("API Key:", MY_API_KEY)
print("Service URL:", SERVICE_URL)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            try:
                response = nlu.analyze(
                    text=text,
                    features={'sentiment': {}}
                ).get_result()
                sentiment = response['sentiment']['document']['label']
            except Exception as e:
                flash(f"An error occurred: {str(e)}", 'error')
                print("Error Details:", str(e))  # Print detailed error
        else:
            flash("Please enter some text.", 'error')
    return render_template('index.html', sentiment=sentiment)