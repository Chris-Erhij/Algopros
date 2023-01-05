from typing import List, Any
# ## Implementing a stack ADT ##


class Stack(object):
    def __init__(self) -> None:
        self.items: List = list()

    def is_empty(self) -> bool:
        if self.items:
            return False
        else:
            return True

    def push(self, item: Any) -> None:
        self.items.insert(0, item)

    def pop(self) -> Any:
        return self.items.pop(0)

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> Any:
        result: int = self.size()
        return self.items[(result - 1) - (result - 1)]
