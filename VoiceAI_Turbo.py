from colorama import Fore, Style
import speech_recognition as sr
from AppOpener import open as open_app
import webbrowser
import pyttsx3
import random
import os
import threading  # Import the threading module

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[0].id)
engine.setProperty('rate', 200)
engine.setProperty("volume", 1.0)

# Function to speak out the given text
def say(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech input from the microphone
def takeCommand():
    r = sr.Recognizer()
    r.energy_threshold = 3000
    r.pause_threshold = 0.5

    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print(Fore.LIGHTMAGENTA_EX + "\nTry again" + Style.RESET_ALL)
        except sr.RequestError as e:
            print(Fore.RED + f"Assistant: Error with the speech recognition service; {e}" + Style.RESET_ALL)
            say("An error occurred")
        except Exception as e:
            print(Fore.RED + f"Assistant: An unexpected error occurred: {e}" + Style.RESET_ALL)
            say("An error occurred")
    return ""

# Function to handle speech recognition in a separate thread
def recognize_speech():
    try:
        while True:
            text = takeCommand().lower()
            # Your existing code for websites
            for site in sites:
                if text == f"open {site[0]}" or text == f"{site[0]} lava":
                    try:
                        # Open the website in a web browser
                        # webbrowser.open(f"{site[1]}")
                        print(Fore.GREEN + f"Assistant: Opening {site[0]} sir." + Style.RESET_ALL)
                        say(f"Opening {site[0]} sir.")
                    except:
                        pass

            # Your existing code for applications
            for i in range(0, 50):
                if text == f"open {applications[i]}" or text == f"{applications[i]} lava":
                    # open_app(applications[i])
                    say(f"Opening {applications[i]} sir.")
                    break
                elif text == "open monkey type" or text == "monkey type lava":
                    # open_app("monkeytype")
                    say("Opening monkeytype sir.")
                    break
                elif text == "open notepad plus plus" or text == "notepad plus plus lava":
                    # open_app("notepad++")
                    say("Opening notepad++ sir.")
                    break

            # Your existing code for playing music
            if "play" in text and "music" in text or "change" in text and "music" in text or text == "gane lava" or text == "gane badla":
                randNum = random.randint(0, 23)
                # os.system(f"start Music\{Songs[randNum]}.mp3")
                say(f"Starting music sir.")
                print(Fore.GREEN + f"Playing {Songs[randNum]} sir." + Style.RESET_ALL)

            # Your existing code for stopping listening
            elif text == "stop listening":
                say("Stopped listening sir.")
                while True:
                    print(Fore.GREEN + "Assistant: Say, 'start listening' to start listening" + Style.RESET_ALL)
                    text = takeCommand()
                    if text.lower() == "start listening":
                        break
                    elif text == "band kar" or text == "exit":
                        say("Terminated")
                        print(Fore.RED + "\n\n---------TERMINATED!---------\n\n" + Style.RESET_ALL)
                        exit()

            # Your existing code for terminating the program
            elif text == "band kar" or text == "exit":
                say("Terminated")
                print(Fore.RED + "\n\n---------TERMINATED!---------\n\n" + Style.RESET_ALL)
                exit()
    except:
        pass

# Create a thread for speech recognition
speech_thread = threading.Thread(target=recognize_speech, daemon=True)
speech_thread.start()

if __name__ == "__main__":
    try:
        print(Fore.GREEN + "\nHello, I am AI Voice Assistant" + Style.RESET_ALL)
        say("Hello, I am AI Voice Assistant")

        # List of websites to be opened with voice command
        sites = [["google", "https://google.com"], ["flipkart", "https://flipkart.com"],
                ["amazon", "https://amazon.in"], ["microsoft edge", "file:///F:/Documents/StartPage/index.html"],
                ["new tab", "file:///F:/Documents/StartPage/index.html"], ["youtube studio", "https://studio.youtube.com"]]

        # List of applications to be opened with voice command
        applications = ["android studio", "blender", "bluestacks", "calculator", "calendar", "camera", "chatgpt",
                        "copilot", "cortana", "discord", "duolingo", "droidcam", "excel", "foxit pdf reader", "gimp",
                        "github desktop", "google translate", "hitfilm", "inkscape", "pycharm community edition", "mail",
                        "maps", "microsoft clipchamp", "microsoft forms", "microsoft store", "microsoft to do",
                        "monkeytype", "notepad++", "obs studio", "onenote", "outlook", "paint3d", "photos", "powerpoint",
                        "publisher", "rapidtyping 5", "settings", "spotify", "terminal", "tlauncher", "unity hub",
                        "visual studio code", "voice recorder", "whatsapp", "winrar", "word", "wps office",
                        "file explorer", "control panel", "youtube"]

        # List of songs to be played with voice command
        Songs = ["Bhool_Bhulaiyya", "Brown_rung", "Char_botal_vodka", "Company", "Grind", "JagPal", "Jehde_nashe", "Jugnu",
                "Kalaastaar", "Kamariya", "Koshish", "Laaree_chootee", "Love_Dose", "Machayenge", "Matargashti",
                "Mera_safar", "Noor_2.0", "O'Meri_laila", "Paisa_hai_toh", "Party_all_night", "Sasta_bawandar",
                "Tera_ghata", "Tu_hai_kahan", "Why_this_kolavari_di"]

        while True:
            print("\nListening...")
            # Get the user's voice command
            text = takeCommand().lower()

            # Check if the voice command matches a website to be opened
            for site in sites:
                if text == f"open {site[0]}" or text == f"{site[0]} lava":
                    try:
                        # Open the website in a web browser
                        webbrowser.open(f"{site[1]}")
                        print(Fore.GREEN + f"Assistant: Opening {site[0]} sir." + Style.RESET_ALL)
                        say(f"Opening {site[0]} sir.")
                    except:
                        pass

            # Check if the voice command matches an application to be opened
            for i in range(0, 50):
                if text == f"open {applications[i]}" or text == f"{applications[i]} lava":
                    # Open the application
                    open_app(applications[i])
                    say(f"Opening {applications[i]} sir.")
                    break
                elif text == "open monkey type" or text == "monkey type lava":
                    open_app("monkeytype")
                    say("Opening monkeytype sir.")
                    break
                elif text == "open notepad plus plus" or text == "notepad plus plus lava":
                    open_app("notepad++")
                    say("Opening notepad++ sir.")
                    break

            # Check if the voice command is related to playing or changing music
            if "play" in text and "music" in text or "change" in text and "music" in text or text == "gane lava" or text == "gane badla":
                # Play a random song from the list
                randNum = random.randint(0, 23)
                os.system(f"start Music\{Songs[randNum]}.mp3")
                say(f"Starting music sir.")
                print(Fore.GREEN + f"Playing {Songs[randNum]} sir." + Style.RESET_ALL)

            # Check if the voice command is to stop listening
            elif text == "stop listening":
                say("Stopped listening sir.")
                while True:
                    print(Fore.GREEN + "Assistant: Say, 'start listening' to start listening" + Style.RESET_ALL)
                    text = takeCommand()
                    if text.lower() == "start listening":
                        break
                    elif text == "band kar" or text == "exit":
                        say("Terminated")
                        print(Fore.RED + "\n\n---------TERMINATED!---------\n\n" + Style.RESET_ALL)
                        exit()

            # Check if the voice command is to terminate the program
            elif text == "band kar" or text == "exit":
                say("Terminated")
                print(Fore.RED + "\n\n---------TERMINATED!---------\n\n" + Style.RESET_ALL)
                exit()
    except:
        pass