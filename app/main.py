import ast
import os

def evaluate_expression(expr: str):
    def eval_node(node):
        if isinstance(node, ast.BinOp):
            left = eval_node(node.left)
            right = eval_node(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            elif isinstance(node.op, ast.Sub):
                return left - right
            elif isinstance(node.op, ast.Mult):
                return left * right
            elif isinstance(node.op, ast.Div):
                return left / right
        elif isinstance(node, ast.Num):  # For Python <3.14
            return node.n
        elif isinstance(node, ast.Constant):  # For Python >=3.8
            return node.value
        else:
            raise ValueError("Unsupported operation")

    return eval_node(ast.parse(expr, mode='eval').body)

if __name__ == "__main__":
    # Get math expression from ENV, fallback to default
    expr = os.getenv("MATH_EXPRESSION", "2+3*4/2")
    print(f"Evaluating: {expr}")
    result = evaluate_expression(expr)
    print(f"Result: {result}")

