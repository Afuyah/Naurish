"""empty message

Revision ID: 966fd7437766
Revises: f82d19b74b8f
Create Date: 2024-08-04 07:20:13.453135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '966fd7437766'
down_revision = 'f82d19b74b8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('promotions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('promotions', schema=None) as batch_op:
        batch_op.drop_column('active')

    # ### end Alembic commands ###
