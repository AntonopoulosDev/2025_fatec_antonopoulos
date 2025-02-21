def calculadora (
    a: float,
    b: float,
    operacion: str = 'soma'
) -> float:
    if operacion == 'soma':
        return a + b
    elif operacion == 'subtração':
        return a - b
    elif operacion == 'multiplicação':
        return a * b
    elif operacion == 'divisão':
        return a / b
    else:
        return 'Operação inválida'
