from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from services.calculadora_service import CalculadoraService

app = FastAPI(
    title="Calculadora SOAP",
    description="Servicio SOAP de calculadora",
    version="1.0.0"
)

calculadora_app = Application(
    [CalculadoraService],
    tns='http://www.servicio.com/soa/calculadora',
    name='CalculadoraService',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

app.mount("/calculadora", WSGIMiddleware(WsgiApplication(calculadora_app)))

@app.get("/")
async def root():
    return {
        "message": "Calculadora SOAP Service",
        "wsdl": "http://localhost:8000/calculadora?wsdl"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)