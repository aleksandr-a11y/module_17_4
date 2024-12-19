"""empty message

Revision ID: 51a9162168d1
Revises: 52257a125067
Create Date: 2024-12-16 18:58:52.386360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51a9162168d1'
down_revision: Union[str, None] = '52257a125067'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
