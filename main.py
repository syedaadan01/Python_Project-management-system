from load import products, sales
from output import display_products, filter_by_category, generate_report

# Display products
display_products()

# Filter by category
electronics = filter_by_category('Electronics')
print("Filtered Electronics: ", electronics)

# Generate the report
generate_report()
