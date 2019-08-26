"""empty message

Revision ID: cd6d78879262
Revises: 017b88e7d5d5
Create Date: 2019-08-23 15:28:17.415746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd6d78879262'
down_revision = '017b88e7d5d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('age', sa.String(length=3), nullable=True))
    op.create_unique_constraint(None, 'students', ['age'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'students', type_='unique')
    op.drop_column('students', 'age')
    # ### end Alembic commands ###