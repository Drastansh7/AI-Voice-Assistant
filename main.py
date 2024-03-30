import speech_recognition as sr
import webbrowser
import os
import datetime
import geocoder
from openai import OpenAI


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/drastanshnadola/Downloads/my-project-enog-5c5831b3e23e.json"

def ai(prompt):
    # Initialize the OpenAI client
    client = OpenAI(api_key='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')

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    text = response.choices[0].message.content

    if not os.path.exists("NABRI_OUTPUTS"):
        os.mkdir("NABRI_OUTPUTS")

    with open(f"NABRI_OUTPUTS/{(prompt[:])}.txt", "w") as f:
        f.write(text)


def say(text):
    os.system("say " + text)

def takeCommand():
    user_voice_input = sr.Recognizer()

    with sr.Microphone() as source:
        # user_voice_input.pause_threshold = 0.5
        audio = user_voice_input.listen(source)

        try:
            query = user_voice_input.recognize_google_cloud(audio, language="en-US")
            print("user said:", query)
            return query

        except sr.RequestError as e:
            return f"Sorry, there was an error with speech to text: {e}"



if __name__ == '__main__':
    say("Hello I am Jarvis")
    while True:
        print("listening...")
        query = takeCommand()

        #todo: Add more sites
        sites = [['YouTube',"https://www.youtube.com"], ['Instagram',"https://www.instagram.com"], ['Wikipedia', "https://www.wikipedia.com"], ['Google',"https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f"Opening {site[0]} ")

        # greetings = ['Hello', 'Hi', 'Hey']
        # for greeting in greetings:
        #     if greeting.lower() in query:
        #         say('Hey There!')

        #todo: configure it for all the countries in the world
        if "the time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            say(f"The current time is {current_time}")

        if "where are we" in query or "my location" in query:
            current_city = geocoder.ip("me").city
            current_country = geocoder.ip("me").country
            say(f"We are current in {current_city}, {current_country}")

        #todo: add more apps
        apps = [['Music', '/System/Applications/Music.app'], ['FaceTime', '/System/Applications/FaceTime.app'], ['Whatsapp', '/Applications/WhatsApp.app']]
        for app in apps:
            if app[0].lower() in query.lower():
                os.system(f"open {app[1]}")
                say(f"opening {app[0]}")

        if "Jarvis".lower() in query.lower():
            ai(prompt=query)





















