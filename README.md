# 🧠 AI Financial Companion — Backend (FastAPI + Supabase)

This is the backend for **Endless Moments LLC’s AI Financial Companion App**.  
It connects a **FastAPI** backend with **Supabase (PostgreSQL)** to manage companies, users, and financial data —
laying the foundation for future AI features like journal automation, OCR receipt reading, and financial insights.

---

## ⚙️ Tech Stack

- **FastAPI** – Python web framework for APIs  
- **Supabase** – PostgreSQL database + authentication  
- **Uvicorn** – ASGI web server for FastAPI  
- **python-dotenv** – Manages environment variables  
- **Supabase Python SDK** – Database queries and joins  
- **Tesseract OCR** – Optical character recognition for receipt parsing  
- **SQLAlchemy** – ORM for OCR data persistence  
- **Pillow** – Image processing for OCR  
- **PyPDF** – PDF document handling  

---

## 📁 Project Structure

```
main.py
database.py
smart_parser.py
requirements.txt
.env
/routes
    ├── users.py
    ├── companies.py
    ├── expenses.py
    └── parser.py
```

### What each file does

| File | Purpose |
|------|----------|
| `main.py` | Runs the FastAPI server and connects all routes |
| `database.py` | Handles connection to Supabase |
| `smart_parser.py` | OCR text extraction and field parsing logic |
| `requirements.txt` | Lists all Python dependencies |
| `.env` | Stores the Supabase URL and service key |
| `/routes/users.py` | Handles user creation, editing, and linking to companies |
| `/routes/companies.py` | Handles company creation, editing, and linking users |
| `/routes/expenses.py` | Handles manual expense entry with journal entries and listing |
| `/routes/parser.py` | Handles receipt parsing (images, PDFs, CSV) |

---

## 🚀 Setup & Run

### 1️⃣ Clone the repo
```bash
git clone https://github.com/yourusername/ai-financial-companion-backend.git
cd ai-financial-companion-backend
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

**Install EasyOCR (for receipt parsing):**
```bash
# EasyOCR dependencies
pip install easyocr pillow pdf2image

# Ubuntu/Debian - Install Poppler for PDF processing
sudo apt-get install poppler-utils

# macOS - Install Poppler
brew install poppler
```

### 3️⃣ Add your environment variables
Create a `.env` file in the root:
```bash
# Supabase Configuration
SUPABASE_URL=https://yourproject.supabase.co
SUPABASE_KEY=your_service_role_key
```

> ⚠️ Use the **service_role key** from Supabase — it allows full backend access (don't expose it publicly).

### 4️⃣ Start the server
```bash
uvicorn main:app --reload
```

Your app will run at:  
👉 **http://127.0.0.1:8000**

Swagger docs:  
👉 **http://127.0.0.1:8000/docs**

---

## 🔗 API Overview

### 🧱 Users (`/users`)
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/users/` | Get all users |
| GET | `/users/{user_id}` | Get one user |
| POST | `/users/` | Create a new user |
| PATCH | `/users/{user_id}` | Update user details |
| DELETE | `/users/{user_id}` | Delete a user |
| POST | `/users/company/{company_id}` | Create a user linked to a company |

---

### 🏢 Companies (`/companies`)
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/companies/` | Get all companies |
| GET | `/companies/with-users` | Get all companies with their users |
| GET | `/companies/{company_id}` | Get one company (with users) |
| GET | `/companies/{company_id}/users` | Get users in a company |
| POST | `/companies/` | Create a new company |
| PATCH | `/companies/{company_id}` | Update company details |
| DELETE | `/companies/{company_id}` | Delete a company |

---

### 💰 Expenses (`/expenses`)
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/expenses/` | Get all expenses (bills with vendor info) |
| GET | `/expenses/company/{company_id}` | Get expenses for a specific company |
| POST | `/expenses/manual_entry` | Create a manual expense with automatic vendor linking, bill creation, and journal entry |

**Example Request:**
```json
{
  "company_id": "uuid",
  "user_id": "uuid",
  "vendor_name": "Office Supplies Inc",
  "amount": 150.00,
  "category": "Office Supplies",
  "payment_method": "credit_card",
  "memo": "Paper and pens",
  "date": "2025-10-21"
}
```

---

### 📄 Receipt Parser (`/parse`)
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/parse/` | Parse receipt image, PDF, or CSV and extract structured data |

**Extracted Fields:**
- Vendor name
- Transaction date
- Total amount
- Description

**Example Usage:**
```bash
curl -X POST http://localhost:8000/parse/ -F "file=@receipt.png"
```

---

## 🧩 Example

### Create a new user linked to a company
**POST** → `http://127.0.0.1:8000/users/company/d3d5e6c5-e1c2-4abc-9cce-5cbdcd0db575`
```json
{
  "full_name": "Jane Doe",
  "email": "jane@ai-finance.com",
  "role": "accountant",
  "user_type": "company"
}
```

### Get a company with all its users
**GET** → `http://127.0.0.1:8000/companies/d3d5e6c5-e1c2-4abc-9cce-5cbdcd0db575`

---

## 💡 Notes

- Backend uses the **Service Role key** — only for secure backend environments.  
- Database joins use **Supabase's PostgREST** syntax like `select("*, users(full_name, email)")`.  
- **Receipt parser** uses EasyOCR to extract text from images and PDFs with smart field parsing.
- **Expense tracking** automatically creates vendors, bills, and journal entries for proper double-entry accounting.
- API is modular and ready to scale — receipt parsing and expense automation are fully integrated!  

---

## 📍 Roadmap

| Feature | Status |
|----------|---------|
| Database setup (Supabase) | ✅ Done |
| User & Company CRUD | ✅ Done |
| Link users ↔ companies | ✅ Done |
| Manual Expense Entry | ✅ Done |
| Receipt Parsing | ✅ Done |
| Automated Journal Entries | ✅ Done (via expenses) |
| AI-Enhanced Categorization | 🔜 Planned |
| RAG Document Indexing | 🔜 Planned |
| Real-time Financial Insights | 🔜 Planned |

---

## 👨‍💻 Author
Endless Moments LLC  

---

🧱 _Built with FastAPI + Supabase for a future-ready AI accounting platform._
