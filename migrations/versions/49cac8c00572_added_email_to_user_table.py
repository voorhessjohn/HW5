"""added email to user table

Revision ID: 49cac8c00572
Revises: 
Create Date: 2017-11-25 14:07:17.982983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49cac8c00572'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
