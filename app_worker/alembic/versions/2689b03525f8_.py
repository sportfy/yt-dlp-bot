"""empty message.

Revision ID: 2689b03525f8
Revises: 0769fbebd121
Create Date: 2022-02-20 00:07:13.184353

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '2689b03525f8'
down_revision = '0769fbebd121'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('error', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'error')
    # ### end Alembic commands ###
