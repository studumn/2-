from blessed import Terminal

term = Terminal()

fruits = ['Apple', 'Banana', 'Orange', 'Grape', 'Blueberry', 'Lemon', 'Watermelon']
colors = ['red', 'yellow', 'darkorange', 'purple', 'blue', 'lightyellow', 'green']

for fruit, color in zip(fruits, colors):
    print(getattr(term, color) + fruit + term.normal)
