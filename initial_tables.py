from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'restaurants',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('price', sa.Integer)
    )

    op.create_table(
        'customers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String),
        sa.Column('last_name', sa.String)
    )

    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('star_rating', sa.Integer),
        sa.Column('restaurant_id', sa.Integer, sa.ForeignKey('restaurants.id')),
        sa.Column('customer_id', sa.Integer, sa.ForeignKey('customers.id'))
    )

def downgrade():
    op.drop_table('reviews')
    op.drop_table('customers')
    op.drop_table('restaurants')
