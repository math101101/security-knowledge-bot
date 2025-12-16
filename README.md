# Security Knowledge Bot 🔐

A local **Python-based chatbot** focused on **cybersecurity**, using a structured knowledge base (JSON) and textual similarity search (**TF-IDF**). This project was designed for **educational purposes**, **security labs**, and as a **technical portfolio project**.

It answers questions about **OWASP**, **ISO/IEC 27001**, **GDPR/LGPD**, **IAM**, and general **security best practices** — fully **offline**, without external APIs or LLMs.

---

## 🎯 Project Objective

* Build a **local information security chatbot**
* Centralize security knowledge in a simple and extensible format
* Demonstrate skills in:

  * Python
  * Text processing
  * Project structuring
  * Information security fundamentals
* Serve as a **portfolio project** for **SOC, Blue Team, Red Team, and DevSecOps** roles

---

## 🧠 How It Works

1. Knowledge is stored in a `kb.json` file
2. Each entry contains:

   * ID
   * Title
   * Tags
   * Explanatory content
   * Reference source
3. All content is converted into TF-IDF vectors
4. User queries are compared against the knowledge base
5. The system returns:

   * The most relevant answer
   * Reference/source information
   * Related topic suggestions

---

## 🗂 Project Structure

```
security-knowledge-bot/
├─ app.py              # Chatbot (CLI)
├─ kb.json             # Knowledge base
├─ requirements.txt    # Dependencies
└─ README.md           # Documentation
```

---

## ⚙️ Technologies Used

* **Python 3.10+**
* **scikit-learn** – TF-IDF and cosine similarity
* **NumPy** – numerical support
* **JSON** – structured knowledge base

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/security-knowledge-bot.git
cd security-knowledge-bot
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the chatbot

```bash
python app.py
```

---

## 💬 Example Questions

You can ask questions such as:

* `What is XSS?`
* `How to mitigate SQL Injection?`
* `What does ISO 27001 say about risk management?`
* `What is MFA and why is it important?`
* `Explain the main GDPR principles`

---

## 🧩 Knowledge Base Structure (`kb.json`)

Example entry:

```json
{
  "id": "owasp-xss",
  "title": "XSS (Cross-Site Scripting)",
  "tags": ["owasp", "xss", "web"],
  "content": "XSS is a vulnerability where malicious scripts are injected into web pages...",
  "source": "OWASP Top 10"
}
```

📌 Simply add new objects following this structure to expand the chatbot knowledge.

---

## 🔒 Legal Disclaimer

This project is **strictly educational**.

* It must not be used for malicious activities
* The content focuses on **awareness, learning, and best practices**
* No real attacks or exploitation are performed

---

## 🚀 Possible Improvements

* Web interface using **Streamlit**
* Local **PDF indexing** (standards, policies, documentation)
* Study / quiz mode for security topics
* Export answers to Markdown or HTML
* Logging and analytics for most frequent questions
* Topic difficulty levels (beginner / intermediate / advanced)

---

## 👨‍💻 Author

**Matheus Costa Silva**
Cybersecurity Student | Python | Automation | Offensive & Defensive Security

🔗 GitHub: [https://github.com/YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

⭐ If this project helped you or inspired you, consider giving it a star!
