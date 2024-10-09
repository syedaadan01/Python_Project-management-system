from load import products, sales

# Helper functions for filtering and reporting
def filter_by_category(category):
    return [product['name'] for product in products if product['category'] == category]

def low_stock_alert(threshold):
    for product in products:
        if product['stock'] < threshold:
            yield product

def display_products():
    for idx, product in enumerate(products):
        print(f"Index: {idx}, Product: {product['name']}, Stock: {product['stock']}")

def generate_report():
    # Total items sold and revenue
    total_items_sold = sum(sale['quantity_sold'] for sale in sales)
    total_revenue = sum(product['price'] * sale['quantity_sold'] for sale in sales for product in products if product['product_id'] == sale['product_id'])
    
    # Updated prices after 10% increase
    print("--- Product Report ---")
    for product in products:
        updated_price = product['price'] * 1.10
        print(f"Product: {product['name']}, Price: ${updated_price:.2f}, Stock: {product['stock']}")

    print(f"Total Items Sold: {total_items_sold}")
    print(f"Total Revenue: ${total_revenue:.2f}")

    print("Low Stock Products:")
    for product in low_stock_alert(20):
        print(f"{product['name']} - Only {product['stock']} left in stock.")
