import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  apiKey: process.env.GEMINI_API_KEY,
});

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ reply: "Method not allowed" });
  }

  try {
    const { message } = req.body;

    if (!message) {
      return res.status(400).json({
        reply: "Message is required."
      });
    }

    const response = await ai.models.generateContent({
      model: "gemini-2.5-flash",
      contents: message,
    });

    res.status(200).json({
      reply: response.text,
    });

  } catch (error) {
    console.error(error);

    res.status(500).json({
      reply: "❌ Error yeroo AI wajjin wal qunnamtii uumamu."
    });
  }
}
