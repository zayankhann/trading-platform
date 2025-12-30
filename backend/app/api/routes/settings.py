from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.init_db import ensure_default_settings

router = APIRouter()

class SettingsOut(BaseModel):
    scan_time_et: str
    lookback_days: int
    lookback_type: str
    long_threshold: float
    short_threshold: float
    min_price: float
    long_notional_usd: float
    short_qty: int

class SettingsUpdate(BaseModel):
    scan_time_et: str | None = Field(default=None, pattern=r"^\d{2}:\d{2}$")
    lookback_days: int | None = None
    lookback_type: str | None = None
    long_threshold: float | None = None
    short_threshold: float | None = None
    min_price: float | None = None
    long_notional_usd: float | None = None
    short_qty: int | None = None

@router.get("/settings", response_model=SettingsOut)
def get_settings(db: Session = Depends(get_db)):
    row = ensure_default_settings(db)
    return SettingsOut(**row.__dict__)

@router.put("/settings", response_model=SettingsOut)
def update_settings(payload: SettingsUpdate, db: Session = Depends(get_db)):
    row = ensure_default_settings(db)

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(row, field, value)

    db.commit()
    db.refresh(row)
    return SettingsOut(**row.__dict__)
