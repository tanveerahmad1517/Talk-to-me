"""Initial Migration

Revision ID: cacc030e30b8
Revises: 06f570dd7331
Create Date: 2018-02-14 10:56:58.935709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cacc030e30b8'
down_revision = '06f570dd7331'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patienttalks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('patient', sa.Column('category', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patient', 'category')
    op.drop_table('patienttalks')
    # ### end Alembic commands ###
