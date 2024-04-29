import click

@click.command()
@click.option('--num1', prompt='Enter the first number', type=float)
@click.option('--num2', prompt='Enter the second number', type=float)
@click.option('--operation', prompt='Enter the operation (+, -, *, /)', type=str)
def calculator(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            click.echo("Error: Division by zero is not allowed")
            return
        result = num1 / num2
    else:
        click.echo("Error: Invalid operation. Please enter one of '+', '-', '*', or '/'")
        return

    click.echo(f"Result: {result}")

if __name__ == "__main__":
    calculator()
