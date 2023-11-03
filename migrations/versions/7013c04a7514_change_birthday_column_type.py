"""change birthday column type

Revision ID: 7013c04a7514
Revises: 2e35bcc5fb34
Create Date: 2023-11-03 16:44:45.915141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7013c04a7514'
down_revision: Union[str, None] = '2e35bcc5fb34'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
