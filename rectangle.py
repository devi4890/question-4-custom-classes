class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Implementing the __iter__ method to make the class iterable
    def __iter__(self):
        # Yield the length and width as dictionaries in the required format
        yield {'length': self.length}
        yield {'width': self.width}


# Example usage:
if __name__ == "__main__":
    rect = Rectangle(10, 5)

    # Iterate over the instance
    for dimension in rect:
        print(dimension)
