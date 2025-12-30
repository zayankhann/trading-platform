from sqlalchemy.orm import Session
from app.core.config import settings as env
from app.models.settings import AppSettings

def ensure_default_settings(db: Session) -> AppSettings:
    row = db.query(AppSettings).order_by(AppSettings.id.asc()).first()
    if row:
        return row

    row = AppSettings(
        scan_time_et=env.DEFAULT_SCAN_TIME,
        lookback_days=env.DEFAULT_LOOKBACK_DAYS,
        lookback_type=env.DEFAULT_LOOKBACK_TYPE,
        long_threshold=env.DEFAULT_LONG_THRESHOLD,
        short_threshold=env.DEFAULT_SHORT_THRESHOLD,
        min_price=env.DEFAULT_MIN_PRICE,
        long_notional_usd=env.DEFAULT_LONG_NOTIONAL,
        short_qty=env.DEFAULT_SHORT_QTY,
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row
