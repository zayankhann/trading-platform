from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    DATABASE_URL: str

    DEFAULT_SCAN_TIME: str = "09:35"
    DEFAULT_LOOKBACK_DAYS: int = 7
    DEFAULT_LOOKBACK_TYPE: str = "calendar"
    DEFAULT_LONG_THRESHOLD: float = -0.05
    DEFAULT_SHORT_THRESHOLD: float = 0.10
    DEFAULT_MIN_PRICE: float = 5.00
    DEFAULT_LONG_NOTIONAL: float = 5.00
    DEFAULT_SHORT_QTY: int = 1


settings = Settings()
