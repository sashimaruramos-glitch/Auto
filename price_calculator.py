def calculate_printing_prices(analysis_results, pricing_rules):
    """
    Calculate printing prices based on analysis results and pricing rules.
    
    Parameters:
    - analysis_results: A dictionary containing the analysis data.
    - pricing_rules: A dictionary containing pricing rules.
    
    Returns:
    A dictionary containing the calculated prices.
    """
    calculated_prices = {}
    
    for item in analysis_results:
        item_id = item['id']
        quantity = item['quantity']
        base_price = pricing_rules.get(item['type'], {}).get('base_price', 0)
        discount = pricing_rules.get(item['type'], {}).get('discount', 0)
        final_price = (base_price * quantity) * (1 - discount)
        calculated_prices[item_id] = round(final_price, 2)
    
    return calculated_prices

# Example usage:
# analysis = [{'id': 'item1', 'quantity': 10, 'type': 'standard'}, {'id': 'item2', 'quantity': 5, 'type': 'premium'}]
# rules = {'standard': {'base_price': 2.0, 'discount': 0.1}, 'premium': {'base_price': 3.0, 'discount': 0.2}}
# prices = calculate_printing_prices(analysis, rules)
# print(prices)
