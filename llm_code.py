# compute average from a list

data = []
total = 0

for d in data:
    total = total + d

if len(data) > 0:
    avg = total / len(data)
else:
    avg = None  # Handle the empty list case appropriately
print(f"Average: {avg}")
