import pandas as pd
import numpy as np
from flask import Flask, request, app, json, Response
from flask_cors import CORS
from datetime import datetime
import sys

app = Flask(__name__)
app.secret_key = 'f3167129525f2a20696b7de80ff37401c963b55871119ed7ddec510809d5fa5530fa40bdf5041484a52a3932a4cad6e542e3c5199ef4cca9aa7c7e52f69c3e76'
CORS(app)

@app.route('/', methods=['GET'])
def Inicio():
    return "inicio"

### oferentes inscritos
@app.route('/oferentesInscritos/canalRegistro', methods=['GET'])
def oferentesInscritoscanalRegistro():
    with open("jsons/oferentesInscritos/canalRegistro.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesInscritos/edad', methods=['GET'])
def oferentesInscritosedad():
    with open("jsons/oferentesInscritos/edad.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesInscritos/genero', methods=['GET'])
def oferentesInscritosgenero():
    with open("jsons/oferentesInscritos/genero.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesInscritos/nivelEstudio', methods=['GET'])
def oferentesInscritosnivelEstudio():
    with open("jsons/oferentesInscritos/nivelEstudio.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesInscritos/ciudadResidencia', methods=['GET'])
def oferentesInscritosciudadResidencia():
    with open("jsons/oferentesInscritos/ciudadResidencia.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesInscritos/fechaRegistro', methods=['GET'])
def oferentesInscritosfechaRegistro():
    with open("jsons/oferentesInscritos/fechaRegistro.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesInscritos/programaGobierno', methods=['GET'])
def oferentesInscritosprogramaGobierno():
    with open("jsons/oferentesInscritos/programaGobierno.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesInscritos/condicionesEspeciales', methods=['GET'])
def oferentesInscritoscondicionesEspeciales():
    with open("jsons/oferentesInscritos/condicionesEspeciales.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesInscritos/situacionLaboral', methods=['GET'])
def oferentesInscritossituacionLaboral():
    with open("jsons/oferentesInscritos/situacionLaboral.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesInscritos/fechaActualizacion', methods=['GET'])

@app.route('/oferentesInscritos/porcentajeHojaVida', methods=['GET'])
def oferentesInscritosporcentajeHojaVida():
    with open("jsons/oferentesInscritos/porcentajeHojaVida.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesInscritos/perteneceA', methods=['GET'])
def oferentesInscritosperteneceA():
    with open("jsons/oferentesInscritos/perteneceA.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )


### oferentes remitidos
@app.route('/oferentesRemitidos/genero', methods=['GET'])
def oferentesRemitidosgenero():
    with open("jsons/oferentesRemitidos/genero.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesRemitidos/ciudadResidencia', methods=['GET'])
def oferentesRemitidosciudadResidencia():
    with open("jsons/oferentesRemitidos/ciudadResidencia.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesRemitidos/fechaRemision', methods=['GET'])
def oferentesRemitidosfechaRemision():
    with open("jsons/oferentesRemitidos/fechaRemision.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesRemitidos/agenteRemitio', methods=['GET'])
def oferentesRemitidosagenteRemitio():
    with open("jsons/oferentesRemitidos/agenteRemitio.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesRemitidos/tipoRemision', methods=['GET'])
def oferentesRemitidostipoRemision():
    with open("jsons/oferentesRemitidos/tipoRemision.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesRemitidos/programaGobierno', methods=['GET'])
def oferentesRemitidosprogramaGobierno():
    with open("jsons/oferentesRemitidos/programaGobierno.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesRemitidos/manoObraCalificada', methods=['GET'])
def oferentesRemitidosmanoObraCalificada():
    with open("jsons/oferentesRemitidos/manoObraCalificada.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )


### oferentes colocados
@app.route('/oferentesColocados/genero', methods=['GET'])
def oferentesColocadosgenero():
    with open("jsons/oferentesColocados/genero.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesColocados/edad', methods=['GET'])
def oferentesColocadosedad():
    with open("jsons/oferentesColocados/edad.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesColocados/ciudadResidencia', methods=['GET'])
def oferentesColocadosciudadResidencia():
    with open("jsons/oferentesColocados/ciudadResidencia.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesColocados/programaGobierno', methods=['GET'])
def oferentesColocadosprogramaGobierno():
    with open("jsons/oferentesColocados/programaGobierno.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesColocados/condicionesEspeciales', methods=['GET'])
def oferentesColocadoscondicionesEspeciales():
    with open("jsons/oferentesColocados/condicionesEspeciales.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesColocados/fechaColocacion', methods=['GET'])
def oferentesColocadosfechaColocacion():
    with open("jsons/oferentesColocados/fechaColocacion.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesColocados/tipoColocado', methods=['GET'])
def oferentesColocadostipoColocado():
    with open("jsons/oferentesColocados/tipoColocado.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesColocados/programaGobiernoVacante', methods=['GET'])
def oferentesColocadosprogramaGobiernoVacante():
    with open("jsons/oferentesColocados/programaGobiernoVacante.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesColocados/manoObraCalificada', methods=['GET'])
def oferentesColocadosmanoObraCalificada():
    with open("jsons/oferentesColocados/manoObraCalificada.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesColocados/tipoContrato', methods=['GET'])
def oferentesColocadostipoContrato():
    with open("jsons/oferentesColocados/tipoContrato.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesColocados/sector', methods=['GET'])
def oferentesColocadossector():
    with open("jsons/oferentesColocados/sector.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/oferentesColocados/municipioSede', methods=['GET'])
def oferentesColocadosmunicipioSede():
    with open("jsons/oferentesColocados/municipioSede.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )


### empresas inscritas
@app.route('/empresasInscritas/naturaleza', methods=['GET'])
def empresasInscritasnaturaleza():
    with open("jsons/empresasInscritas/naturaleza.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/empresasInscritas/sector', methods=['GET'])
def empresasInscritassector():
    with open("jsons/empresasInscritas/sector.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/empresasInscritas/tamano', methods=['GET'])
def empresasInscritastamano():
    with open("jsons/empresasInscritas/tamano.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/empresasInscritas/ciudad', methods=['GET'])
def empresasInscritasciudad():
    with open("jsons/empresasInscritas/ciudad.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/empresasInscritas/fechaRegistro', methods=['GET'])
def empresasInscritasfechaRegistro():
    with open("jsons/empresasInscritas/fechaRegistro.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/empresasInscritas/canalRegistro', methods=['GET'])
def empresasInscritascanalRegistro():
    with open("jsons/empresasInscritas/canalRegistro.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/empresasInscritas/agenteAprobo', methods=['GET'])
def empresasInscritasagenteAprobo():
    with open("jsons/empresasInscritas/agenteAprobo.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )


### vacantes publicadas
@app.route('/vacantesPublicadas/cargo', methods=['GET'])
def vacantesPublicadascargo():
    with open("jsons/vacantesPublicadas/cargo.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/vacantesPublicadas/empresa', methods=['GET'])
def vacantesPublicadasempresa():
    with open("jsons/vacantesPublicadas/empresa.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/vacantesPublicadas/estadoActual', methods=['GET'])
def vacantesPublicadasestadoActual():
    with open("jsons/vacantesPublicadas/estadoActual.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/vacantesPublicadas/programaGobierno', methods=['GET'])
def vacantesPublicadasprogramaGobierno():
    with open("jsons/vacantesPublicadas/programaGobierno.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/vacantesPublicadas/ciudad', methods=['GET'])
def vacantesPublicadasciudad():
    with open("jsons/vacantesPublicadas/ciudad.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/vacantesPublicadas/discapacidad', methods=['GET'])
def vacantesPublicadasdiscapacidad():
    with open("jsons/vacantesPublicadas/discapacidad.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/vacantesPublicadas/puestosTrabajo', methods=['GET'])
def vacantesPublicadaspuestosTrabajo():
    with open("jsons/vacantesPublicadas/puestosTrabajo.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/vacantesPublicadas/tipoContrato', methods=['GET'])
def vacantesPublicadastipoContrato():
    with open("jsons/vacantesPublicadas/tipoContrato.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/vacantesPublicadas/fechaPublicacion', methods=['GET'])
def vacantesPublicadasfechaPublicacion():
    with open("jsons/vacantesPublicadas/fechaPublicacion.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
@app.route('/vacantesPublicadas/manoObraCalificada', methods=['GET'])
def vacantesPublicadasmanoObraCalificada():
    with open("jsons/vacantesPublicadas/manoObraCalificada.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )

if __name__ == '__main__':
    app.run()

