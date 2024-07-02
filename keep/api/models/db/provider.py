from datetime import datetime
from typing import Optional

from sqlalchemy import UniqueConstraint
from sqlmodel import JSON, Column, Field, SQLModel


class Provider(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("tenant_id", "name"),)

    id: str = Field(default=None, primary_key=True, max_length=256)
    tenant_id: str = Field(foreign_key="tenant.id", max_length=36)
    name: str = Field(max_length=255)
    description: Optional[str]
    type: str = Field(max_length=255)
    installed_by: str = Field(max_length=255)
    installation_time: datetime
    configuration_key: str = Field(max_length=255, default="")
    validatedScopes: dict = Field(
        sa_column=Column(JSON)
    )  # scope name is key and value is either True if validated or string with error message, e.g: {"read": True, "write": "error message"}
    consumer: bool = False

    class Config:
        orm_mode = True
        unique_together = ["tenant_id", "name"]
