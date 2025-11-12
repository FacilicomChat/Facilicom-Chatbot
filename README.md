# 💬 Facilicom Chatbox — One-Click Deploy 🚀

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Facilicom-Chatbot/facilicom-chatbox)

A ready-to-deploy chatbot for Facilicom — powered by FastAPI (Python) and a clean HTML/CSS/JS frontend.

---

## 🌍 About
The Facilicom Chatbox is a professional, friendly Dutch-language assistant that can answer questions, assist employees or customers, and be extended with your own company knowledge.

---

## 🚀 Quick Deploy on Render

### One-Click
Click the **Deploy to Render** button above, connect your GitHub account, and watch your chatbot go live.

### Manual steps (if preferred)
1. Push this folder to GitHub as `facilicom-chatbox`.
2. Go to [https://render.com](https://render.com) → *New → Web Service*.
3. Connect your GitHub repo.
4. Render will auto-detect settings from `render.yaml`.  
   If not, set:
   - **Build command:** `pip install -r backend/requirements.txt`
   - **Start command:** `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables:
   ```bash
   OPENAI_API_KEY = your-key
   MODEL_NAME = gpt-4o-mini
   SYSTEM_PROMPT = Jij bent de Facilicom Chatbox, een vriendelijke, professionele Nederlandstalige assistent.
   ```

When done, your app will be live at a URL like:  
👉 `https://facilicom-chatbox.onrender.com`

---

## 🧪 Local Test

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add your OpenAI key
python main.py
```
Then open **http://localhost:8000**

---

## 🧰 Features
- ✅ Built with FastAPI (Python)
- 💡 Single-domain (frontend + backend served together)
- 🎨 Facilicom branding (logo, colors, tone of voice)
- 🔐 Environment-based secrets (no hardcoded keys)
- 🌐 Deployable with one click on Render

---

© 2025 Facilicom — Demo chatbot template.
