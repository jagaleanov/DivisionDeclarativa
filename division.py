
def div( m, n ):

    if n > m :
        return 0
    else:
        return div( ( m - n ), n ) + 1

n = int( input( "Ingrese el divedendo: " ) )
m = int( input( "Ingrese el divisor: " ) )

numero_div = div( m, n )
print( "El cociente entre " + repr( m ) + " y " + repr( n ) + " es " + repr( numero_div ) )
