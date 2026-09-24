from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="LegalTech-Invest API")

# Frontend bilan ulanish uchun CORS sozlamalari
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CompanyRequest(BaseModel):
    company_name: str
    tin: str  # STIR / INN
    sector: str

class RiskFactor(BaseModel):
    category: str
    description: str
    risk_level: str  # High, Medium, Low

class AuditReport(BaseModel):
    company_name: str
    tin: str
    sector: str
    status: str
    overall_score: int
    risks: List[RiskFactor]
    recommendation: str

@app.get("/")
def home():
    return {"message": "LegalTech-Invest API ishlamoqda!"}

@app.post("/api/analyze", response_model=AuditReport)
def analyze_company(data: CompanyRequest):
    # Demotsion legal-tech tahlil simulyatsiyasi
    mock_risks = [
        RiskFactor(
            category="Soliq va Moliya",
            description="So'nggi 12 oyda soliq qardorligi bo'yicha kichik kechikishlar mavjud.",
            risk_level="Medium"
        ),
        RiskFactor(
            category="Sud va Huquqiy",
            description="Iqtisodiy sudda da'vogar yoki javobgar sifatida ochiq ishlar topilmadi.",
            risk_level="Low"
        ),
        RiskFactor(
            category="Ustav Kapitali",
            description="Ta'sischilar tarkibi va ustav kapitali to'liq shakllantirilgan.",
            risk_level="Low"
        )
    ]
    
    return AuditReport(
        company_name=data.company_name,
        tin=data.tin,
        sector=data.sector,
        status="Muvaffaqiyatli tahlil qilindi",
        overall_score=85,
        risks=mock_risks,
        recommendation="Kompaniya investitsiya kiritish uchun huquqiy va moliyaviy jihatdan barqaror deb baholandi."
    )