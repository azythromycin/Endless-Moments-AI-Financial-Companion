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
requirements.txt
.env
/routes
    ├── users.py
    ├── companies.py
    ├── expenses.py
    └── ocr.py
```

### What each file does

| File | Purpose |
|------|----------|
| `main.py` | Runs the FastAPI server and connects all routes |
| `database.py` | Handles connection to Supabase |
| `requirements.txt` | Lists all Python dependencies |
| `.env` | Stores the Supabase URL and service key |
| `/routes/users.py` | Handles user creation, editing, and linking to companies |
| `/routes/companies.py` | Handles company creation, editing, and linking users |
| `/routes/expenses.py` | Handles manual expense entry with journal entries |
| `/routes/ocr.py` | Handles OCR receipt upload and data extraction |

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

Or manually:
```bash
pip install fastapi uvicorn python-dotenv supabase sqlalchemy pytesseract pillow pdfminer.six pypdfium2 python-multipart python-dateutil
```

**Install Tesseract OCR:**
```bash
# Ubuntu/Debian
sudo apt-get install tesseract-ocr

# macOS
brew install tesseract
```

### 3️⃣ Add your environment variables
Create a `.env` file in the root:
```bash
# Supabase Configuration
SUPABASE_URL=https://yourproject.supabase.co
SUPABASE_KEY=your_service_role_key

# OCR Configuration (optional - these are defaults)
OCR_ENGINE=tesseract
DATABASE_URL=sqlite:///./receipts.db
DEFAULT_CURRENCY=USD
MAX_PDF_PAGES=10
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

### 📄 OCR Receipt Processing (`/ocr`)
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/ocr/upload` | Upload a receipt image or PDF for processing |
| POST | `/ocr/extract?raw_id={id}&commit={bool}` | Extract data from uploaded receipt using OCR |
| GET | `/ocr/receipt/{raw_id}` | Get metadata about an uploaded receipt |

**OCR Workflow:**
1. **Upload** a receipt image (PNG, JPEG) or PDF → Returns `raw_id`
2. **Extract** data using Tesseract OCR → Returns structured fields
3. Optionally **commit** to create a transaction record automatically

**Extracted Fields:**
- Vendor name
- Transaction date
- Total amount
- Tax amount
- Currency (USD, EUR, GBP, INR, CAD, AUD)
- Payment card last 4 digits
- Confidence score (0-100)

**Example Usage:**
```bash
# Upload receipt
curl -X POST http://localhost:8000/ocr/upload -F "file=@receipt.png"

# Extract data
curl -X POST "http://localhost:8000/ocr/extract?raw_id=abc-123&commit=false"
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
- **OCR Pipeline** uses a separate SQLite database by default (`receipts.db`) for receipt data.
- **Tesseract OCR** automatically detects and extracts text from receipts with smart field parsing.
- **Expense tracking** automatically creates vendors, bills, and journal entries for proper double-entry accounting.
- API is modular and ready to scale — OCR and expense automation are now fully integrated!  

---

## 📍 Roadmap

| Feature | Status |
|----------|---------|
| Database setup (Supabase) | ✅ Done |
| User & Company CRUD | ✅ Done |
| Link users ↔ companies | ✅ Done |
| Manual Expense Entry | ✅ Done |
| OCR Receipt Parsing | ✅ Done |
| Automated Journal Entries | ✅ Done (via expenses) |
| AI-Enhanced Categorization | 🔜 Planned |
| RAG Document Indexing | 🔜 Planned |
| Real-time Financial Insights | 🔜 Planned |

---

## 👨‍💻 Author
Endless Moments LLC  

---

🧱 _Built with FastAPI + Supabase for a future-ready AI accounting platform._
