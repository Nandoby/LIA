"""Fix Philips Hue connector_type stored as enum value instead of enum name.

hue_global_config_001 inserted 'philips_hue', but ConnectorType is mapped with
Enum(native_enum=False), which persists the member NAME ('PHILIPS_HUE').
Loading the row raised LookupError and broke GET /connectors/admin/global-config.

Revision ID: hue_global_config_fix_001
Revises: usage_limits_001
Create Date: 2026-11-19
"""

from alembic import op

revision: str = "hue_global_config_fix_001"
down_revision: str | None = "usage_limits_001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Rewrite 'philips_hue' to 'PHILIPS_HUE' (or drop it if both exist)."""
    op.execute("""
        DELETE FROM connector_global_config
        WHERE connector_type = 'philips_hue'
          AND EXISTS (
              SELECT 1 FROM connector_global_config WHERE connector_type = 'PHILIPS_HUE'
          )
    """)
    op.execute("""
        UPDATE connector_global_config
        SET connector_type = 'PHILIPS_HUE'
        WHERE connector_type = 'philips_hue'
    """)


def downgrade() -> None:
    """No-op: the lowercase value was never readable by the ORM."""
