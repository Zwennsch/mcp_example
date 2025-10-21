# libraries:
from fastmcp import FastMCP

mcp = FastMCP("example")

# @server.tool


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers

    args:   a (float): The first number.
            b (float): The second number.

    returns: float: The product of the two numbers.

    """
    return a*b


@mcp.tool(name="add_numbers",
          description="Add two numbers",
          tags=["math", "addition"])
def add(a: float, b: float) -> float:
    """Add two numbers

    args:   a (float): The first number.
            b (float): The second number.

    returns: float: The sum of the two numbers.

    """
    return a + b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers

    args:   a (float): The numerator.
            b (float): The denominator.

    returns: float: The quotient of the two numbers.

    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers

    args:   a (float): The first number.
            b (float): The second number.

    returns: float: The difference of the two numbers.

    """
    return a - b


if __name__ == "__main__":
    mcp.run()  # STDIO by default
