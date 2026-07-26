"""add foreing-key to the post tabel

Revision ID: fba2229dd5e3
Revises: 3a91a39ccf7f
Create Date: 2026-07-24 10:23:36.871449

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fba2229dd5e3'
down_revision: Union[str, Sequence[str], None] = '3a91a39ccf7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('post_usres_fk', source_table = 'posts', referent_table = 'users',
                          local_cols = ['owner_id'], remote_cols = ['id'], ondelete = 'CASCADE')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_users_fk', table_name = 'posts')
    op.drop_column('posts', 'owner_id') 
    pass
