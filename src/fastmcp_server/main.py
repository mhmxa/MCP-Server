from fastmcp import FastMCP

mcp = FastMCP("Demo-Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract the second number from the first number."""
    return a - b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide the first number by the second number."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    mcp.run()
