"""initial migration

Revision ID: 991e2179916a
Revises: 0d4b0ba40b70
Create Date: 2017-01-16 20:04:53.379500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '991e2179916a'
down_revision = '0d4b0ba40b70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('spd', sa.PickleType(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'spd')
    # ### end Alembic commands ###
