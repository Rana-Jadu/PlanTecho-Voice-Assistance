require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { Speech } = require('@google-cloud/speech');
const textToSpeech = require('@google-cloud/text-to-speech');
const { GoogleGenerativeAI } = require('@google/generative-ai');

const app = express();
app.use(cors());
app.use(express.json());

// Google Services Setup
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: 'gemini-pro' });
const sttClient = new Speech.SpeechClient();
const ttsClient = new textToSpeech.TextToSpeechClient();

// API Endpoint
app.post('/chat', async (req, res) => {
  try {
    // Add your chat handling logic here
    res.json({ response: "Backend working!" });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Server error" });
  }
});

// Start Server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});