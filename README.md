# PolyglotBot - Multilingual Translation & Learning Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

## Table of Contents
1. [Project Overview](#project-overview-)
2. [Features](#features-)
3. [Implementation Details](#implementation-details-)
4. [Installation](#installation-)
5. [Usage](#usage-)
6. [API Reference](#api-reference-)
7. [Contributing](#contributing-)
8. [License](#license-)

## Project Overview <a name="project-overview"></a>
PolyglotBot is a Flask-based web application that provides:
- Real-time text translation using Google Translate API
- Text-to-speech conversion in multiple languages
- Simple REST API endpoints for integration

## Features <a name="features"></a>
### Core Translation Features
- **Text Translation** between 100+ languages
- **Text-to-Speech** output in translated language
- **Temporary Audio Files** management
- **Asynchronous Playback** of translated speech

## Implementation Details <a name="implementation-details"></a>
The translator is built using the following core components:

```python
from flask import Flask, render_template, request, jsonify
from gtts import gTTS
from playsound import playsound
import tempfile
import threading
from deep_translator import GoogleTranslator
```
Key Components
Flask Web Framework: Handles HTTP requests and responses

GoogleTranslator: Provides the translation functionality

gTTS (Google Text-to-Speech): Converts translated text to speech

Tempfile: Manages temporary audio storage

Threading: Enables non-blocking audio playback

Installation <a name="installation"></a>
Requirements
Python 3.8+

pip package manager

Setup
bash
Copy
# Clone repository
git clone https://github.com/yourusername/PolyglotBot.git
cd PolyglotBot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Required Packages
The requirements.txt file includes:

text
Copy
flask==2.0.1
gtts==2.2.3
playsound==1.2.2
deep-translator==1.9.1
python-dotenv==0.19.0
Usage <a name="usage"></a>
Running the Application
bash
Copy
python app.py
Example Requests
Translate text from English to Spanish:
![Screenshot 2025-04-05 214129](https://github.com/user-attachments/assets/0c78d5fa-769c-4016-8c31-65ea4a6f153d)

![Screenshot 2025-04-05 213231](https://github.com/user-attachments/assets/9c084423-4990-457b-a31a-560749ed273a)

![Screenshot 2025-04-05 213500](https://github.com/user-attachments/assets/2483befe-830f-4c67-a49a-e5ba77c1d2c3)
![Screenshot 2025-04-05 213832](https://github.com/user-attachments/assets/b39cc13e-74cb-49c0-aabf-accceb8c699f)
![Screenshot 2025-04-05 213701](https://github.com/user-attachments/assets/ba07b541-1534-4f86-a5e3-14e86f4ef1da)

![Screenshot 2025-04-05 213450](https://github.com/user-attachments/assets/bf012456-90b5-497c-a2fc-c08617594447)


![Screenshot 2025-04-05 214021](https://github.com/user-attachments/assets/1127f030-37d7-48d5-9e9b-a177b096709b)



http
Copy
POST /translate
Content-Type: application/json

{
    "text": "Hello world",
    "target_lang": "es",
    "speak": true
}
Response:

json
Copy
{
    "translated_text": "Hola mundo",
    "audio_file": "/temp/audio_12345.mp3",
    "status": "success"
}
API Reference <a name="api-reference"></a>
Endpoints
Endpoint	Method	Parameters	Description
/translate	POST	text, target_lang, [speak]	Translates text and optionally generates speech
/languages	GET	-	Returns supported languages
Language Codes
The API uses standard ISO 639-1 language codes (e.g., 'es' for Spanish, 'fr' for French).

Contributing <a name="contributing"></a>
Contributions are welcome! Please follow these guidelines:

Fork the repository

Create a feature branch

Submit a pull request

License <a name="license"></a>
This project is licensed under the MIT License - see the LICENSE file for details.

File Hashes (latest version):

app.py: sha256: a1b2... (replace with actual hash)

requirements.txt: sha256: c3d4... (replace with actual hash)

README.md: sha256: e5f6... (replace with actual hash)

For verification:

bash
Copy
sha256sum app.py requirements.txt README.md
Copy

This README includes:

1. Proper Markdown formatting with headers (##, ###)
2. Code blocks with syntax highlighting
3. Tables for API documentation
4. Badges at the top
5. File hashes section at the bottom
6. Clear section organization with anchor links
7. Installation and usage instructions
8. Implementation details showing the core imports you mentioned

The hashes shown are placeholders - you should replace them with actual SHA-256 hashes of your files after creating them.
