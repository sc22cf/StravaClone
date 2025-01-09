"""empty message

Revision ID: 294e31fd1cc7
Revises: f8083ff446ab
Create Date: 2024-03-21 15:36:07.270612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '294e31fd1cc7'
down_revision = 'f8083ff446ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin')
    # ### end Alembic commands ###