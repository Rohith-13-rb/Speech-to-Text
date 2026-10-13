"""
Sample WAV Audio Generator Helper
Subject: Text and Speech Analysis
Description: Generates a test audio WAV file using pyttsx3 or creates a tone WAV
             so students can test 02_Speech_to_Text without needing a microphone.
"""

import os
import sys

def generate_with_tts(text="Hello world, this is a speech to text demonstration.", filename="sample.wav"):
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        output_path = os.path.abspath(filename)
        engine.save_to_file(text, output_path)
        engine.runAndWait()
        print(f"[SUCCESS] Generated sample speech WAV file at: {output_path}")
        print(f"Spoken content: \"{text}\"")
        return output_path
    except ImportError:
        print("[INFO] 'pyttsx3' is not installed. To generate speech WAV automatically, run:")
        print("       pip install pyttsx3")
        return None
    except Exception as e:
        print(f"[ERROR] Could not synthesize speech: {e}")
        return None

if __name__ == "__main__":
    print("=" * 60)
    print("      SAMPLE AUDIO GENERATOR FOR SPEECH TO TEXT")
    print("=" * 60)
    user_text = input("Enter phrase to synthesize into sample.wav (Press Enter for default): ").strip()
    if not user_text:
        user_text = "Hello world, this is a speech to text demonstration for text and speech analysis."
    generate_with_tts(user_text, "sample.wav")
