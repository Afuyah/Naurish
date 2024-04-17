"""empty message

Revision ID: f0980a353860
Revises: 412015b1fac4
Create Date: 2024-04-17 05:35:15.001296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0980a353860'
down_revision = '412015b1fac4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('day_of_week')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('day_of_week', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
