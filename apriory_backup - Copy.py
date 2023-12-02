import csv
from apyori import apriori

# Read data from CSV file
with open('transaction_data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Apply Apriori algorithm to get frequent itemsets
min_support = 0.2  # Set min_support to 2 or any other value less than or equal to 2
results = list(apriori(data, min_support=min_support, min_confidence=0.5))


# Print the most frequent itemsets
# print(results)
print("Most Frequent Itemsets:")
len_x = []
for itemset in results:
    # print(list(itemset.items))
    tem = list(itemset.items)
    if len(tem) > len(len_x):
        len_x = tem
print(len_x)

# Print the association rules

# user_input = input("Enter items_base (comma-separated): ").strip()

# # Split the user input string into a list
# user_input_list = user_input.split(',')

# # Iterate through the results and find the corresponding items_add
# for itemset in results:
#     for rule in itemset['ordered_statistics']:
#         if rule['items_base'] == user_input_list:
#             print(f"items_base: {', '.join(rule['items_base'])} -> items_add: {', '.join(rule['items_add'])} (Confidence: {rule['confidence']:.2f})")

# user_input = input("Enter item_base (comma-separated): ").strip().split(',')

user_input_items = input("Enter desired itemset items (comma-separated): ").strip().split(',')

# Print the association rules that match the user input
print("\nAssociation Rules:")
a=[]
for itemset in results:
    if set(user_input_items).issubset(itemset.items):
        # print(list(itemset.items))
        for rule in itemset.ordered_statistics:
            # print("rule",rule)
            b= rule.items_base
            # print(b)
            if len(rule.items_base )> 0:
                for i in rule.items_base:
                    # print(i)
                    a.append(i)
            c= rule.items_add
            # print(b)
            if len(rule.items_add )> 0:
                for i in rule.items_add:
                    # print(i)
                    a.append(i)
            # print(f"{', '.join(rule.items_base)}")
            # print(f"{', '.join(rule.items_base)} -> {', '.join(rule.items_add)}")
            print(f"{', '.join(rule.items_base)} -> {', '.join(rule.items_add)} (Confidence: {rule.confidence:.2f})")
            # a.append(rule.items_base)
            # a.append(rule.items_add)

print("==")
print(set(a))