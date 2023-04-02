"""create users table

Revision ID: f586c7b95d22
Revises: 
Create Date: 2023-03-31 09:27:54.844180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f586c7b95d22'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.Unicode(50)),
        sa.Column('phone', sa.Unicode(50)),
        sa.Column('birthday', sa.Date()),
    )


def downgrade() -> None:
     op.drop_table('users')
