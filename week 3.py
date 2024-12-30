def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage.

  Returns:
    The final price after applying the discount, or the original price if the discount is less than 20%.
  """
  if discount_percent >= 20:
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount
  else:
    final_price = price
  return final_price

if __name__ == "__main__":
  original_price = float(input("Enter the original price: "))
  discount_percentage = float(input("Enter the discount percentage: "))

  final_price = calculate_discount(original_price, discount_percentage)

  print(f"Final price: ${final_price:.2f}")