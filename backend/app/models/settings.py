from sqlalchemy import String, Integer, Float, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class AppSettings(Base):
    __tablename__ = "settings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    scan_time_et: Mapped[str] = mapped_column(String(5), nullable=False)
    lookback_days: Mapped[int] = mapped_column(Integer, nullable=False)
    lookback_type: Mapped[str] = mapped_column(String(16), nullable=False)

    long_threshold: Mapped[float] = mapped_column(Float, nullable=False)
    short_threshold: Mapped[float] = mapped_column(Float, nullable=False)
    min_price: Mapped[float] = mapped_column(Float, nullable=False)

    long_notional_usd: Mapped[float] = mapped_column(Float, nullable=False)
    short_qty: Mapped[int] = mapped_column(Integer, nullable=False)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
