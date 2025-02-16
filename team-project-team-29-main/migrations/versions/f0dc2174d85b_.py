"""empty message

Revision ID: f0dc2174d85b
Revises: 36ab28b30067
Create Date: 2024-02-26 18:05:26.757744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0dc2174d85b'
down_revision = '36ab28b30067'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street_address', sa.String(length=150), nullable=True),
    sa.Column('city', sa.String(length=150), nullable=True),
    sa.Column('postcode', sa.String(length=20), nullable=True),
    sa.Column('country_code', sa.String(length=2), nullable=True),
    sa.Column('stripe_token', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment_details')
    # ### end Alembic commands ###
