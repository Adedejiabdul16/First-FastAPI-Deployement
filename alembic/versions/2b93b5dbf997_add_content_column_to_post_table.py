"""add content column to post table

Revision ID: 2b93b5dbf997
Revises: 38f380614297
Create Date: 2026-07-20 11:02:55.431825

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b93b5dbf997'
down_revision: Union[str, Sequence[str], None] = '38f380614297'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
