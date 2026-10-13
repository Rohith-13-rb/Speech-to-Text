"""
Speech to Text (STT) Mini Application
Subject: Text and Speech Analysis
Description: Transcribes spoken speech into text using the SpeechRecognition library.
             Supports transcribing pre-recorded .wav files and live microphone input.
"""

import os
import sys

try:
    import speech_recognition as sr
except ImportError:
    print("\n[ERROR] The 'SpeechRecognition' package is not installed.")
    print("Please install it by running: pip install -r requirements.txt\n")
    sys.exit(1)


def transcribe_audio_file(file_path):
    """
    Transcribes speech from a given audio file (WAV format recommended).
    Uses Google Web Speech API (free, no API key required).
    """
    if not os.path.exists(file_path):
        print(f"[ERROR] Audio file not found at: {file_path}")
        return None

    recognizer = sr.Recognizer()
    print(f"\n[Processing] Loading and analyzing audio file: {file_path}")

    try:
        with sr.AudioFile(file_path) as source:
            # Adjust for background noise in the recorded file
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio_data = recognizer.record(source)

        print("[Processing] Recognizing speech via Google Speech API...")
        text = recognizer.recognize_google(audio_data)
        print("\n" + "=" * 50)
        print("  TRANSCRIPTION RESULT")
        print("=" * 50)
        print(text)
        print("=" * 50)
        return text

    except sr.UnknownValueError:
        print("[RESULT] Speech was unintelligible or no speech was detected in the audio file.")
        return None
    except sr.RequestError as e:
        print(f"[ERROR] Could not request results from Google Speech Recognition service: {e}")
        print("Please check your internet connection.")
        return None
    except Exception as e:
        print(f"[ERROR] Failed to process audio file: {e}")
        return None


def transcribe_microphone():
    """
    Captures live audio from the microphone and converts it to text.
    Requires PyAudio to be installed on the system.
    """
    recognizer = sr.Recognizer()

    try:
        # Check if microphone is accessible
        with sr.Microphone() as source:
            print("\n[Mic Ready] Calibrating for ambient background noise... (Please be quiet for 1s)")
            recognizer.adjust_for_ambient_noise(source, duration=1.0)
            print("[Listening] Please speak clearly into your microphone now (5 seconds timeout)...")

            try:
                audio_data = recognizer.listen(source, timeout=6, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                print("[WARNING] Listening timed out. No speech was detected.")
                return None

        print("[Processing] Transcribing your speech...")
        text = recognizer.recognize_google(audio_data)
        print("\n" + "=" * 50)
        print("  MICROPHONE TRANSCRIPTION RESULT")
        print("=" * 50)
        print(text)
        print("=" * 50)
        return text

    except (AttributeError, OSError) as e:
        print("\n[ERROR] Microphone access failed.")
        print("Details:", e)
        print("Hint: 'PyAudio' is required for live microphone capture.")
        print("On Windows, you can install it via: pip install pyaudio")
        print("Alternatively, you can test pre-recorded .wav files using Option 1.\n")
        return None
    except sr.UnknownValueError:
        print("[RESULT] Could not understand the audio. Please speak louder and clearly.")
        return None
    except sr.RequestError as e:
        print(f"[ERROR] Speech recognition service unreachable: {e}")
        print("Please ensure your computer is connected to the internet.")
        return None
    except Exception as e:
        print(f"[ERROR] Unexpected error during microphone transcription: {e}")
        return None


def main():
    print("=" * 60)
    print("    SPEECH TO TEXT (STT) APPLICATION - MINI LAB")
    print("=" * 60)
    print("This app converts spoken speech into written text using SpeechRecognition.")

    while True:
        print("\nMain Menu:")
        print("1. Transcribe speech from an audio file (.wav)")
        print("2. Transcribe speech from live microphone")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            file_path = input("\nEnter the path to your .wav audio file: ").strip()
            # Strip surrounding quotes if dragged-and-dropped into terminal
            file_path = file_path.strip("\"'")
            if not file_path:
                print("[WARNING] File path cannot be empty.")
                continue
            transcribe_audio_file(file_path)

        elif choice == "2":
            transcribe_microphone()

        elif choice == "3":
            print("\nExiting Speech-to-Text application. Goodbye!\n")
            break

        else:
            print("[ERROR] Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
