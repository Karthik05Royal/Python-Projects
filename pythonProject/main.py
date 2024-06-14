import time
import speech_recognition as sr

# initialize recognizer
r = sr.Recognizer()

# set start and end keywords
start_keyword = "start"
end_keyword = "stop"

# use microphone as source
with sr.Microphone() as source:
    print(f"Say '{start_keyword}' to start the program and '{end_keyword}' to stop")
    start_time = None
    while True:
        # listen for audio and convert to text
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: ", text)
            # check if the start keyword was spoken
            if text.lower() == start_keyword and not start_time:
                start_time = time.time()
                print("Program started")
            # check if the end keyword was spoken
            elif text.lower() == end_keyword and start_time:
                end_time = time.time()
                print("Program stopped. Elapsed time: {:.2f} seconds".format(end_time - start_time))
                break
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Speech Recognition service; {0}".format(e))
