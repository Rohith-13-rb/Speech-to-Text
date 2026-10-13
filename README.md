# 02 - Speech to Text (STT) Application

## Overview
This application is part of the **Text and Speech Analysis** college lab curriculum. It demonstrates **Automatic Speech Recognition (ASR)**, the computational process of translating spoken audio signals into machine-readable text transcripts.

It uses the `SpeechRecognition` Python library, interfacing with the Google Web Speech API to perform acoustic-to-linguistic transcription.

---

## Features
- **WAV Audio File Transcription**: Transcribe pre-recorded `.wav` audio files without needing a live microphone.
- **Live Microphone Transcription**: Real-time voice capture and speech recognition from an active microphone input.
- **Ambient Noise Calibration**: Automatically adjusts for room background noise before listening.
- **Sample Audio Helper**: Includes `generate_sample_wav.py` to synthesize test audio files for quick verification.
- **Robust Error Handling**: Gracefully handles network interruptions, unintelligible audio, and missing audio drivers.

---

## Prerequisites & Installation

1. Navigate to this folder:
   ```bash
   cd 02_Speech_to_Text
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

> **Note regarding PyAudio on Windows:**
> - `SpeechRecognition` works immediately for audio files without `pyaudio`.
> - If you want to use the live microphone, `pyaudio` is required. On Windows, run:
>   ```bash
>   pip install pyaudio
>   ```
> - If `pip install pyaudio` fails due to missing C++ build tools on older systems, download the matching pre-compiled `.whl` wheel for your Python version from official PyPI or Christoph Gohlke's Python Wheels repository, or simply use Option 1 (audio file mode).

---

## How to Run

### Step 1: (Optional) Generate a Sample WAV file
If you do not have a pre-recorded audio file or microphone, generate a test audio file:
```bash
python generate_sample_wav.py
```
This creates `sample.wav` in the current folder.

### Step 2: Run the Main Application
```bash
python speech_to_text.py
```

### Example Usage:
```text
Main Menu:
1. Transcribe speech from an audio file (.wav)
2. Transcribe speech from live microphone
3. Exit

Enter your choice (1-3): 1
Enter the path to your .wav audio file: sample.wav

[Processing] Loading and analyzing audio file: sample.wav
[Processing] Recognizing speech via Google Speech API...

==================================================
  TRANSCRIPTION RESULT
==================================================
hello world this is a speech to text demonstration
==================================================
```

---

## Technical Notes & Limitations
- **Audio Format**: The Google Speech Recognizer natively handles uncompressed PCM WAV files (16kHz or 44.1kHz mono recommended).
- **Network Requirement**: Google Web Speech API requires an active internet connection. It is free and does not require an API key for modest request volumes.
- **Background Noise**: High ambient noise or microphone clipping can lower transcription accuracy; ambient noise adjustment helps mitigate this.
