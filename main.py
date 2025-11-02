from fastapi import FastAPI
from database import table
from routes import users, companies, expenses, parser

app = FastAPI(title="AI Financial Companion Backend")

# include routers
app.include_router(users.router)
app.include_router(companies.router)
app.include_router(expenses.router)
app.include_router(parser.router)

@app.get("/")
def read_root():
    return {"message": "AI Financial Companion Backend is running!"}

@app.get("/health")
def health_check():
    try:
        response = table("users").select("*").limit(1).execute()
        return {"message": "Connected to Supabase!", "data": response.data}
    except Exception as e:
        return {"error": str(e)}
