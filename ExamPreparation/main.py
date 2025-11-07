"""
This module holds main program
"""
import pandas as pd
import matplotlib.pyplot as plt

drugs = pd.read_csv('drugs.csv')
price = pd.read_csv('price.csv')
sales1 = pd.read_csv('sales1.csv')


"""
Merged data by id
"""
merged_df = pd.merge(drugs, sales1, on='id')
print()
print(merged_df)

merged_data = sales1.merge(price, on='id')
merged_data['revenue'] = merged_data['quantity'] * merged_data['price']
total_revenue = merged_data['revenue'].sum()
print()
print(f"Загальна вартість медикаментів: {total_revenue}")


"""
Sum for all categories
"""
print()
category_name = drugs.groupby('category')['name'].sum()
print(category_name)


"""
Category sum
"""
print()
drugs_prices = drugs.merge(price, on='id')
merged_data = sales1.merge(drugs_prices, on='id')
category_totals = {}
for _, row in merged_data.iterrows():
    category = row['category']
    revenue = row['price'] * row['quantity']
    if category not in category_totals:
        category_totals[category] = 0
    category_totals[category] += revenue
print("Виручка за категоріями:")
for category, total in category_totals.items():
    print(f"{category}: {total} грн")


"""
Diagram
"""
categories = list(category_totals.keys())
values = list(category_totals.values())
plt.bar(categories, values)
plt.xlabel('Категорії ліків')
plt.ylabel('Загальна виручка, грн')
plt.show()


"""
The most profitable category by vip
"""
corporate_sales = sales1[sales1['corporate'] == 'yes']
merged_corporate = corporate_sales.merge(drugs).merge(price)
merged_corporate['revenue'] = merged_corporate['price'] * merged_corporate['quantity']
drug_revenue = merged_corporate.groupby('name')['revenue'].sum()
top_drug = drug_revenue.idxmax()
max_revenue = drug_revenue.max()
drug_category = drugs[drugs['name'] == top_drug]['category'].iloc[0]
print()
print("The most profitable drug: ")
print(f"{top_drug} ({drug_category}): {max_revenue} грн")



"""
Profit by categories by vip
"""
category_revenue = merged_corporate.groupby('category')['revenue'].sum()
print()
print("Виручка по категоріях від корпоративних клієнтів: ")
for category, revenue in category_revenue.items():
    print(f"{category}: {revenue} грн")



"""
Total profit by vip
"""
total_corporate_revenue = merged_corporate['revenue'].sum()
print()
print("Загальна сума продажів корпоративним клієнтам: ")
print(f"Загальна виручка: {total_corporate_revenue} грн")



"""
Drugs not bought by vip with categories
"""
all_categories = drugs['category'].unique()
print()
print("Ліки не куплені корпоративними клієнтами по категоріях: ")
for category in all_categories:
    all_drugs_in_category = set(drugs[drugs['category'] == category]['name'])
    corporate_drugs_in_category = set(merged_corporate[merged_corporate['category'] == category]['name'])
    not_purchased_drugs = all_drugs_in_category - corporate_drugs_in_category

    if not_purchased_drugs:
        print(f"{category}:")
        for drug in not_purchased_drugs:
            print(f"  - {drug}")
    else:
        print(f"{category}: всі ліки куплювались корпоративними клієнтами")

