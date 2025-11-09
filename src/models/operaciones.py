from spyne import ComplexModel, Unicode, Double, Integer, Array
from spyne.model.primitive import Boolean

class ResultadoCalculo(ComplexModel):
    __namespace__ = 'http://www.servicio.com/soa/calculadora'
    
    operacione = Unicode
    numero1 = Double
    numero2 = Double
    resultado = Double
    timestamp = Unicode
    exitoso = Boolean
    mensaje = Unicode
    
class OperacionCompleja(ComplexModel):
    __namespace__ = 'http://www.servicio.com/soa/calculadora'
    numeros = Array(Double)
    operacion = Unicode
    resultado = Double
    
class HistorialOperacion(ComplexModel):
    __namespace__ = 'http://www.servicio.com/soa/calculadora'
    id_operacion = Integer
    tipo_operacion = Unicode
    parametros = Unicode
    resultado = Double
    fecha_ejecucion = Unicode
    usuario = Unicode