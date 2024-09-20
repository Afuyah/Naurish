"""empty message

Revision ID: a41413b92f97
Revises: a27008a3d8eb
Create Date: 2024-09-20 13:28:58.576605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a41413b92f97'
down_revision = 'a27008a3d8eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_variety_id', sa.Integer(), nullable=True))
        batch_op.create_index(batch_op.f('ix_order_item_product_variety_id'), ['product_variety_id'], unique=False)
        # Provide a name for the foreign key constraint
        batch_op.create_foreign_key('fk_order_item_product_variety_id', 'product_variety', ['product_variety_id'], ['id'])
        batch_op.drop_column('custom_description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('custom_description', sa.VARCHAR(length=255), nullable=True))
        # Provide the foreign key constraint name to drop it
        batch_op.drop_constraint('fk_order_item_product_variety_id', type_='foreignkey')
        batch_op.drop_index(batch_op.f('ix_order_item_product_variety_id'))
        batch_op.drop_column('product_variety_id')
    # ### end Alembic commands ###
