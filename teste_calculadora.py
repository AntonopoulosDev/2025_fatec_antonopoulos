import calculadora 

a = 3
b = 2
print(f'{a} + {b} = {calculadora.calculadora(a, b, "adição")}')
print(f'{a} - {b} = {calculadora.calculadora(a, b, "subtração")}')

# minor não trás novas funcionalidades, apenas correções de bugs
# patch trás correções de bugs e pequenas melhorias
# major trás novas funcionalidades e mudanças que podem quebrar o código    