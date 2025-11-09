from spyne import rpc, ServiceBase, Unicode, Double, Integer, Array
from spyne.model.primitive import Boolean
from datetime import datetime
import json
import math

from models.operaciones import ResultadoCalculo, OperacionCompleja, HistorialOperacion

class CalculadoraService(ServiceBase):
    __namespace__ = 'http://www.servicio.com/soa/calculadora'
    _contador_id = 1
    _historial = []
    
    @rpc(Double, Double, _returns=ResultadoCalculo)
    def sumar(ctx, numero1, numero2):
        try:
            resultado = numero1 + numero2
            operacion = HistorialOperacion(
				  id_operacion = CalculadoraService._contador_id,
				  tipo_operacion = "SUMA",
				  parametros =json.dumps({"numero1": numero2, "numero2": numero2}),
				  resultado = resultado,
				  fecha_ejecucion = datetime.now().isoformat(),
				  usuario = "SOAP_CLIENT"
      		)
            CalculadoraService._historial.append(operacion)
            CalculadoraService._contador_id += 1
            return ResultadoCalculo(
				 operacion = "SUMA",
				 numero1 = numero1,
				 numero2 = numero2,
				 resultado = resultado,
				 timestamp = datetime.now().isoformat(),
				 exitoso = True,
				 mensaje = "Operación exitosa"
     		)
        except Exception as e:
            return ResultadoCalculo(
				operacion="SUMA",
				numero1=numero1,
				numero2=numero2,
				resultado=0,
				timestamp=datetime.now().isoformat(),
				exitoso=False,
				mensaje=f"Error: {str(e)}"
			)
    
    @rpc(Double, Double, _returns=ResultadoCalculo)
    def restar(ctx, numero1, numero2):
        try:
            resultado = numero1 - numero2
            
            operacion = HistorialOperacion(
                id_operacion=CalculadoraService._contador_id,
                tipo_operacion="RESTA",
                parametros=json.dumps({"numero1": numero1, "numero2": numero2}),
                resultado=resultado,
                fecha_ejecucion=datetime.now().isoformat(),
                usuario="SOAP_CLIENT"
            )
            CalculadoraService._historial.append(operacion)
            CalculadoraService._contador_id += 1
            
            return ResultadoCalculo(
                operacion="RESTA",
                numero1=numero1,
                numero2=numero2,
                resultado=resultado,
                timestamp=datetime.now().isoformat(),
                exitoso=True,
                mensaje="Operación exitosa"
            )
        except Exception as e:
            return ResultadoCalculo(
                operacion="RESTA",
                numero1=numero1,
                numero2=numero2,
                resultado=0,
                timestamp=datetime.now().isoformat(),
                exitoso=False,
                mensaje=f"Error: {str(e)}"
            )
    
    @rpc(Double, Double, _returns=ResultadoCalculo)
    def multiplicar(ctx, numero1, numero2):
        try:
            resultado = numero1 * numero2
            operacion = HistorialOperacion(
                id_operacion=CalculadoraService._contador_id,
                tipo_operacion="MULTIPLICACIÓN",
                parametros=json.dumps({"numero1": numero1, "numero2": numero2}),
                resultado = resultado,
                fecha_ejecucion=datetime.now().isoformat(),
                usuario="SOAP_CLIENT"
            )
            CalculadoraService._historial.append(operacion)
            CalculadoraService._contador_id += 1
            
            return ResultadoCalculo(
                operacion="MULTIPLICACIÓN",
                numero1=numero1,
                numero2=numero2,
                resultado=resultado,
                timestamp=datetime.now().isoformat(),
                exitoso=True,
                mensaje="Operación exitosa"
            )
        except Exception as e:
            return ResultadoCalculo(
                operacion="MULTIPLICACIÓN",
                numero1=numero1,
                numero2=numero2,
                resultado=0,
                timestamp=datetime.now().isoformat(),
                exxitoso=False,
                mensaje=f"Error: {str(e)}"
            )
            
    @rpc(Double, Double, _returns=ResultadoCalculo)
    def dividir(ctx, numero1, numero2):
        try:
            resultado = numero1 / numero2
            operacion = HistorialOperacion(
                id_operacion=CalculadoraService._contador_id,
                tipo_operacion="DIVISIÓN",
                parametros=json.dumps({"numero1": numero1, "numero2": numero2}),
                resultado = resultado,
                fecha_ejecucion=datetime.now().isoformat(),
                usuario="SOAP_CLIENT"
            )
            CalculadoraService._historial.append(operacion)
            CalculadoraService._contador_id += 1
            
            return ResultadoCalculo(
                operacion="MULTIPLICACIÓN",
                numero1=numero1,
                numero2=numero2,
                resultado=resultado,
                timestamp=datetime.now().isoformat(),
                exitoso=True,
                mensaje="Operación exitosa"
            )
        except Exception as e:
            return ResultadoCalculo(
                operacion="DIVISIÓN",
                numero1=numero1,
                numero2=numero2,
                resultado=0,
                timestamp=datetime.now().isoformat(),
                exxitoso=False,
                mensaje=f"Error: {str(e)}"
            )
        
            
    @rpc(_returns=Array(HistorialOperacion))
    def obtener_historial(ctx):
        return CalculadoraService._historial