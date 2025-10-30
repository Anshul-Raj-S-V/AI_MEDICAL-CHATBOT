
# 🧠 AI Medical Chatbot — Voice + Vision + Intelligence

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/Gradio-4.x-orange.svg)](https://gradio.app)
[![OpenAI](https://img.shields.io/badge/Meta_LLaMA_4-Instruct-green.svg)](https://ai.meta.com/llama/)
[![Groq](https://img.shields.io/badge/Groq-Whisper_Large_V3-purple.svg)](https://groq.com)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-TTS-red.svg)](https://elevenlabs.io)

---

## 🩺 Overview

**AI Medical Chatbot** is an intelligent **voice-based healthcare assistant** that listens to the patient’s symptoms, analyzes uploaded **medical images (e.g., X-rays, skin scans)**, and responds **verbally like a real doctor**.  
It combines **speech recognition**, **computer vision**, and **text-to-speech synthesis** to create a natural, conversational medical analysis flow.

> ⚙️ Built for educational and research purposes to explore multimodal AI in medical diagnostics.

---

## 🧩 Core Features

- 🎙️ **Voice-to-Text (Speech Recognition)**  
  Uses **Groq’s Whisper-Large-V3** model for highly accurate and real-time medical speech transcription.

- 🖼️ **Image Understanding (Vision + LLM)**  
  Analyzes medical images via **Meta LLaMA 4 Scout 17B** to provide contextual health insights.

- 🧑‍⚕️ **AI Doctor Response Generation**  
  The system crafts a concise, empathetic doctor-like response—avoiding robotic or AI-style phrasing.

- 🔊 **Text-to-Speech (Doctor’s Voice)**  
  Uses **ElevenLabs TTS** or **Google TTS (fallback)** to deliver lifelike medical advice in a natural tone.

- 💬 **Interactive Gradio Interface**  
  A clean web UI for recording voice, uploading images, and listening to the AI doctor’s spoken feedback.

---

## 🧠 System Architecture

```mermaid
graph TD;
    A[🎤 Patient Speech] -->|Groq Whisper| B[🧾 Text Transcript]
    B --> C[🩺 Meta LLaMA 4 - Vision + Text Analysis]
    C --> D[🧑‍⚕️ Doctor-like Response]
    D -->|ElevenLabs / gTTS| E[🔊 Audio Output]
    E --> F[💻 Gradio UI Display]
````

---

## ⚙️ Tech Stack

| Component                    | Technology Used                 |
| ---------------------------- | ------------------------------- |
| **Frontend (UI)**            | Gradio 4.x                      |
| **Speech Recognition (STT)** | Groq API – Whisper Large V3     |
| **Vision + Reasoning**       | Meta LLaMA 4 Scout 17B Instruct |
| **Text-to-Speech (TTS)**     | ElevenLabs API / Google gTTS    |
| **Environment Variables**    | python-dotenv                   |
| **Audio Processing**         | pydub                           |
| **Language**                 | Python 3.11+                    |

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/AI_MEDICAL_CHATBOT.git
cd AI_MEDICAL_CHATBOT
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # for Windows
# source venv/bin/activate  # for Linux/Mac
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the project root and add:

```bash
GROQ_API_KEY=your_groq_api_key
ELEVEN_API_KEY=your_elevenlabs_api_key
```

### 5️⃣ Run the App

```bash
python main.py
```

Then open the Gradio UI at:
👉 [http://127.0.0.1:7860](http://127.0.0.1:7860)

---

## 🧑‍💻 Project Structure

```bash
AI_MEDICAL_CHATBOT/
│
├── brain.py                  # Image encoding + AI analysis logic
├── voice_of_patient.py       # Records + transcribes patient speech
├── voice_of_doctor.py        # Generates and plays doctor's voice
├── main.py                   # Gradio UI integration
├── .env                      # API keys (keep private)
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
└── venv/                     # Virtual environment (ignored in Git)
```

---

## 🧬 Example Flow

1. 🎤 The patient speaks their symptoms (recorded via microphone).
2. 🧠 The system transcribes speech → interprets image → generates a concise diagnosis.
3. 🔊 The doctor’s response is converted to natural voice using ElevenLabs and played automatically.

---

## ⚠️ Disclaimer

> ⚕️ **This project is for learning and demonstration purposes only.**
> It is **not intended for real medical use or diagnosis.**
> Always consult a licensed medical professional for any health concerns.

---


> *“AI won’t replace doctors, but doctors who use AI will replace those who don’t.”*

---

```

