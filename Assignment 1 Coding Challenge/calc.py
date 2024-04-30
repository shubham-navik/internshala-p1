# import click

# @click.command()
# @click.option('--num1', prompt='Enter the first number', type=float)
# @click.option('--num2', prompt='Enter the second number', type=float)
# @click.option('--operation', prompt='Enter the operation (+, -, *, /)', type=str)
# def calculator(num1, num2, operation):
#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif operation == '*':
#         result = num1 * num2
#     elif operation == '/':
#         if num2 == 0:
#             click.echo("Error: Division by zero is not allowed")
#             return
#         result = num1 / num2
#     else:
#         click.echo("Error: Invalid operation. Please enter one of '+', '-', '*', or '/'")
#         return

#     click.echo(f"Result: {result}")

# if __name__ == "__main__":
#     calculator()
import click
import math

def evaluate_expression(expression):
    try:
        result = eval(expression, {'__builtins__': None}, {'math': math})
        return result
    except Exception as e:
        raise ValueError(f"Invalid expression: {str(e)}")

@click.command()
def calculator():
    previous_result = None

    while True:
        click.echo("Enter a mathematical expression (e.g., 2 + 3 * (4 - 1)):")
        expression = click.prompt("Expression", type=str)

        if expression.lower() == 'h':
            click.echo("To enter a mathematical expression, simply type it and press Enter.")
            click.echo("To compute the result, press Enter without typing anything.")
            click.echo("To compute another expression, press 'y'. To exit, press 'q'.")
            click.echo("To show the result of the previously computed expression, press 'p'.")
            continue

        if expression.lower() == 'p':
            if previous_result is not None:
                click.echo(f"Previous result: {previous_result}")
            else:
                click.echo("No previous result available.")
            continue

        if expression.lower() == 'q':
            click.echo("Exiting...")
            break

        try:
            result = evaluate_expression(expression)
            click.echo(f"Result: {result}")
            previous_result = result
        except ValueError as e:
            click.echo(f"Error: {str(e)}")
        except Exception as e:
            click.echo(f"An unexpected error occurred: {str(e)}")

        choice = click.prompt("Do you want to compute another expression? [Y/n/h/p/q]", type=str, default='y')

        if choice.lower() == 'n':
            click.echo("Exiting...")
            break
        elif choice.lower() == 'h':
            click.echo("To enter a mathematical expression, simply type it and press Enter.")
            click.echo("To compute the result, press Enter without typing anything.")
            click.echo("To compute another expression, press 'y'. To exit, press 'q'.")
            click.echo("To show the result of the previously computed expression, press 'p'.")
        elif choice.lower() == 'p':
            if previous_result is not None:
                click.echo(f"Previous result: {previous_result}")
            else:
                click.echo("No previous result available.")

if __name__ == "__main__":
    calculator()
