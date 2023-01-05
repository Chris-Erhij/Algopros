import implementation
from typing import Dict, List


def match(o_par: str, c_par: str) -> bool:
    """Matches opening parenthesis with exact closing parenthesis
    """

    """Returns True is matched False otherwise
    """
    o_pars: str = '([{'
    c_pars: str = ')]}'
    return o_pars.index(o_par) == c_pars.index(c_par)


def symbol_checker(symbol_string: str) -> bool:
    """Takes a string of symbols and returns True if balanced False otherwise
    """
    stack_obj: implementation.Stack = implementation.Stack()
    index: int = 0
    balanced: bool = True

    # Access string of symbols using their indices
    while balanced and index < len(symbol_string):
        symbol: str = symbol_string[index]
        if symbol in '([{':
            stack_obj.push(symbol)

        elif stack_obj.is_empty():
            balanced = False

        else:
            top: str = stack_obj.pop()
            if not match(o_par=top, c_par=symbol):
                balanced = False
        index += 1
    if balanced and stack_obj.is_empty():
        return balanced
    else:
        return False


def base_x_conv(decimal_no: int, base: int) -> str:
    """Takes an integer decimal and returns a binary string
    """
    costm_hex: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPUV"
    base_x_string: str = str()
    stack_obj_1: implementation.Stack = implementation.Stack()

    while decimal_no > 0:
        decimal_no, remain = divmod(decimal_no, base)
        stack_obj_1.push(remain)

    while not stack_obj_1.is_empty():
        base_x_string += costm_hex[stack_obj_1.pop()]
    return base_x_string


def infix_to_postfix(infix_string: str) -> str:
    """Takes and infix expression, returns a postfix equivalent
    """
    operator_pred: Dict = {'*': 3, '/': 3, '-': 2, '+': 2, ')': 1}
    operator_stack: implementation.Stack = implementation.Stack()
    postfix_list = []
    token_list: List = infix_string.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)

        elif token == '(':
            operator_stack.push(token)

        elif token == ')':
            top_stack = operator_stack.pop()
            while top_stack != '(':
                postfix_list.append(top_stack)
                top_stack = operator_stack.pop()
        else:
            while (not operator_stack.is_empty()) and (operator_pred[operator_stack.peek()] >= operator_pred[token]):
                postfix_list.append(operator_stack.pop())
            operator_stack.push(token)

        while not operator_stack.is_empty():
            postfix_list.append(operator_stack.pop())
    return "".join(postfix_list)


if __name__ == '__main__':
    print("Import and use module functions\n" "If in interactive mode, no need import, just use functions")
