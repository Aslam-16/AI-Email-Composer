# ✉️ AI Email Composer

An AI-powered email composition application built with **Python and Streamlit**, integrating OpenAI and Google Gemini to generate professional emails based on user preferences.

The application allows users to compose emails by specifying the purpose, desired tone, and recipient. Users can choose between OpenAI and Gemini as their AI provider.

## 🚀 Features

- **Multiple AI Providers:** Choose between OpenAI and Google Gemini.
- **Custom Email Generation:** Generate emails based on the purpose provided by the user.
- **Tone Selection:** Choose from:
  - Formal
  - Informal
  - Friendly
  - Professional
- **Recipient Selection:** Customize emails for:
  - Client
  - Colleague
  - Manager
  - Friend
- **Input Validation:** Checks whether the provided request is suitable for email composition.
- **Structured Responses:** Uses JSON responses with validation status and generated email content.
- **Email History:** View previously generated emails using expandable sections.
- **Secure API Configuration:** API keys are loaded through environment variables instead of being hardcoded.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| Streamlit | User interface |
| OpenAI API | AI-powered email generation |
| Google Gemini API | Alternative AI provider |
| python-dotenv | Environment variable management |
| JSON | Structured AI responses |

## 📂 Project Structure

```text
AI-Email-Composer/
│
├── app.py                 # Streamlit application
├── generate.py            # AI response generation logic
├── .env                   # API keys (not committed)
├── .gitignore             # Files excluded from Git
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

*Adjust the filenames above if your actual project structure differs.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Aslam-16/AI-Email-Composer.git
```

### 2. Navigate to the project directory

```bash
cd AI-Email-Composer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API keys

Create a `.env` file in the project root directory.

Add your API keys:

```env
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Get your API keys:

- OpenAI: https://platform.openai.com/api-keys
- Google Gemini: https://aistudio.google.com/apikey

**Important:** Never commit your `.env` file or expose your API keys in a public repository.

Ensure your `.gitignore` includes:

```gitignore
.env
venv/
.venv/
__pycache__/
*.pyc
```

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 How to Use

1. Launch the application.
2. Select your preferred AI provider (OpenAI or Gemini).
3. Enter the purpose of the email.
4. Select the desired email tone.
5. Choose the recipient.
6. Click **Compose Email**.
7. View your generated email.
8. Access previously generated emails through the History section.

## 🧠 Application Workflow

```text
       User Input
           |
           v
    Select AI Provider
           |
           v
   Validate Email Purpose
           |
           v
    Build AI Prompts
           |
           v
    +---------------+
    |               |
    v               v
  OpenAI          Gemini
    |               |
    v               v
    +-------+-------+
            |
            v
     Generate Response
            |
            v
       Parse JSON
            |
            v
    Validate Response
            |
       +----+----+
       |         |
       v         v
    Valid     Invalid
       |         |
       v         v
 Display Email  Show Message
       |
       v
  Store in History
```

## 🔐 Security Considerations

- API keys are managed through environment variables.
- Sensitive configuration files are excluded using `.gitignore`.
- User input is treated as untrusted content.
- System instructions define the application's email-composition boundaries.
- API credentials should never be exposed in frontend code or GitHub repositories.

*Note: Prompt instructions alone do not guarantee protection against prompt injection. Production deployments should include additional input validation, rate limiting, and appropriate API usage controls.*

## 🔮 Future Enhancements

- [ ] Support conversational email editing.
- [ ] Add email subject and body as separate fields.
- [ ] Allow users to copy generated emails.
- [ ] Add email download functionality.
- [ ] Introduce additional AI providers.
- [ ] Improve prompt-injection detection and input validation.
- [ ] Deploy the application publicly.

## 👨‍💻 Author

**Aslam Mohamed**

GitHub: https://github.com/Aslam-16

---

If you find this project useful, consider giving the repository a ⭐.