import pandas as pd
import numpy as np
from flask import Flask, request, app, json, Response
from flask_cors import CORS
from datetime import datetime
import sys

app = Flask(__name__)
app.secret_key = 'f3167129525f2a20696b7de80ff37401c963b55871119ed7ddec510809d5fa5530fa40bdf5041484a52a3932a4cad6e542e3c5199ef4cca9aa7c7e52f69c3e76'
CORS(app)

def saveOferentesInscritos():
    dataOferentesInscritos = pd.read_excel("AGENCIA DE EMPLEO.xlsx", sheet_name="OFERENTES INSCRITOS", usecols=["Tipo Documento", "Número Documento", "Canal de Registro", "Edad", "Género", "Nivel de Estudio", "Título Homologado", "Ciudad de Residencia", "Fecha Registro", "Programa de Gobierno", "Condiciones Especiales", "Situación Laboral", "Fecha Actualización", "% Hoja Vida", "Pertenece A"]).replace(np.nan, "No Registra")
    dataOferentesInscritos["Fecha Registro"] = pd.to_datetime(dataOferentesInscritos["Fecha Registro"], dayfirst=True, format='mixed').dt.strftime('%d/%m/%Y')
    dataOferentesInscritos["Fecha Actualización"] = pd.to_datetime(dataOferentesInscritos["Fecha Actualización"], dayfirst=True, format='mixed').dt.strftime('%d/%m/%Y')
    dataOferentesInscritos["Programa de Gobierno"] = (dataOferentesInscritos["Programa de Gobierno"]!="No Registra").replace(False, "No pertenece").replace(True, "Si pertenece")
    dataOferentesInscritos["Condiciones Especiales"] = (dataOferentesInscritos["Condiciones Especiales"]!="No Registra").replace(False, "No tiene").replace(True, "Si tiene")
    dataOferentesInscritos["Situación Laboral"] = dataOferentesInscritos["Situación Laboral"].replace("NO REGISTRA", "No Registra")
    dataOferentesInscritos.loc[~dataOferentesInscritos["Ciudad de Residencia"].isin(["BUCARAMANGA","FLORIDABLANCA", "GIRÓN", "PIEDECUESTA"]), ["Ciudad de Residencia"]] = "No pertenece al área metropolitana"

    #falta titulo homologado porque de eso hay que hacer un analisis a parte
    canalRegistro = {"canalRegistro": dict(zip(dataOferentesInscritos["Canal de Registro"].value_counts().keys(), dataOferentesInscritos["Canal de Registro"].value_counts()))}
    edad =  {"edad": dict(zip(dataOferentesInscritos["Edad"].value_counts().keys(), dataOferentesInscritos["Edad"].value_counts()))}
    genero =  {"genero": dict(zip(dataOferentesInscritos["Género"].value_counts().keys(), dataOferentesInscritos["Género"].value_counts()))}
    nivelEstudio =  {"nivelEstudio": dict(zip(dataOferentesInscritos["Nivel de Estudio"].value_counts().keys(), dataOferentesInscritos["Nivel de Estudio"].value_counts()))}
    ciudadResidencia =  {"ciudadResidencia": dict(zip(dataOferentesInscritos["Ciudad de Residencia"].value_counts().keys(), dataOferentesInscritos["Ciudad de Residencia"].value_counts()))}
    fechaRegistro =  {"fechaRegistro": dict(zip(dataOferentesInscritos["Fecha Registro"].value_counts().keys(), dataOferentesInscritos["Fecha Registro"].value_counts()))}
    programaGobierno =  {"programaGobierno": dict(zip(dataOferentesInscritos["Programa de Gobierno"].value_counts().keys(), dataOferentesInscritos["Programa de Gobierno"].value_counts()))}
    condicionesEspeciales =  {"condicionesEspeciales": dict(zip(dataOferentesInscritos["Condiciones Especiales"].value_counts().keys(), dataOferentesInscritos["Condiciones Especiales"].value_counts()))}
    situacionLaboral =  {"situacionLaboral": dict(zip(dataOferentesInscritos["Situación Laboral"].value_counts().keys(), dataOferentesInscritos["Situación Laboral"].value_counts()))}
    fechaActualizacion =  {"fechaActualizacion": dict(zip(dataOferentesInscritos["Fecha Actualización"].value_counts().keys(), dataOferentesInscritos["Fecha Actualización"].value_counts()))}
    porcentajeHojaVida =  {"porcentajeHojaVida": dict(zip(dataOferentesInscritos["% Hoja Vida"].value_counts().keys(), dataOferentesInscritos["% Hoja Vida"].value_counts()))}
    perteneceA =  {"perteneceA": dict(zip(dataOferentesInscritos["Pertenece A"].value_counts().keys(), dataOferentesInscritos["Pertenece A"].value_counts()))}
    with open('jsons/oferentesInscritos.json', 'w+') as out_file:
        json.dump([canalRegistro, edad, genero, nivelEstudio, ciudadResidencia, fechaRegistro, programaGobierno, condicionesEspeciales, situacionLaboral, fechaActualizacion, porcentajeHojaVida, perteneceA], out_file, sort_keys = True, indent = 4, ensure_ascii = False)

def saveOferentesRemitidos():
    dataOferentesRemitidos = pd.read_excel("AGENCIA DE EMPLEO.xlsx", sheet_name="OFERENTES REMITIDOS", usecols=["Tipo Documento", "Número Documento", "Sexo", "Dirección Oferente", "Ciudad de residencia", "Fecha Remisión", "Código Vacante", "Proceso", "Empresa", "Agente Remitió", "Tipo de Remisión", "Programa de Gobierno", "es_mano_de_obra_calificada"]).replace(np.nan, "No Registra")
    dataOferentesRemitidos["Fecha Remisión"] = (pd.to_datetime(dataOferentesRemitidos["Fecha Remisión"], dayfirst=True, format='mixed').dt.strftime('%d/%m/%Y'))
    dataOferentesRemitidos["Programa de Gobierno"] = (dataOferentesRemitidos["Programa de Gobierno"]!="No Registra").replace(False, "No pertenece").replace(True, "Si pertenece")
    dataOferentesRemitidos.loc[~dataOferentesRemitidos["Ciudad de residencia"].isin(["BUCARAMANGA","FLORIDABLANCA", "GIRÓN", "PIEDECUESTA"]), ["Ciudad de residencia"]] = "No pertenece al área metropolitana"

    #falta empresas,direccion,codigo vacante, proceso porque de eso hay que hacer un analisis a parte
    genero =  {"genero": dict(zip(dataOferentesRemitidos["Sexo"].value_counts().keys(), dataOferentesRemitidos["Sexo"].value_counts()))}
    ciudadResidencia =  {"ciudadResidencia": dict(zip(dataOferentesRemitidos["Ciudad de residencia"].value_counts().keys(), dataOferentesRemitidos["Ciudad de residencia"].value_counts()))}
    fechaRemision =  {"fechaRemision": dict(zip(dataOferentesRemitidos["Fecha Remisión"].value_counts().keys(), dataOferentesRemitidos["Fecha Remisión"].value_counts()))}
    agenteRemitio =  {"agenteRemitio": dict(zip(dataOferentesRemitidos["Agente Remitió"].value_counts().keys(), dataOferentesRemitidos["Agente Remitió"].value_counts()))}
    tipoRemision =  {"tipoRemision": dict(zip(dataOferentesRemitidos["Tipo de Remisión"].value_counts().keys(), dataOferentesRemitidos["Tipo de Remisión"].value_counts()))}
    programaGobierno =  {"programaGobierno": dict(zip(dataOferentesRemitidos["Programa de Gobierno"].value_counts().keys(), dataOferentesRemitidos["Programa de Gobierno"].value_counts()))}
    manoObraCalificada =  {"manoObraCalificada": dict(zip(dataOferentesRemitidos["es_mano_de_obra_calificada"].value_counts().keys(), dataOferentesRemitidos["es_mano_de_obra_calificada"].value_counts()))}
    with open('jsons/oferentesRemitidos.json', 'w+') as out_file:
        json.dump([genero, ciudadResidencia, fechaRemision, agenteRemitio, tipoRemision, programaGobierno, manoObraCalificada], out_file, sort_keys = True, indent = 4, ensure_ascii = False)

def saveOferentesColocados():
    dataOferentesColocados = pd.read_excel("AGENCIA DE EMPLEO.xlsx", sheet_name="OFERENTES COLOCADOS", usecols=["Tipo Documento", "Número Documento", "sexo", "Edad", "Dirección Oferente", "Ciudad de residencia", "Programa de Gobierno", "Condiciones Especiales", "Código Vacante", "Fecha Colocación", "Proceso", "Empresa", "Tipo de Colocado", "Programa de Gobierno Vacante", "es_mano_de_obra_calificada", "Tipo Contrato", "Sector", "Municipio sede"]).replace(np.nan, "No Registra")
    dataOferentesColocados.loc[~dataOferentesColocados["Ciudad de residencia"].isin(["BUCARAMANGA","FLORIDABLANCA", "GIRÓN", "PIEDECUESTA"]),["Ciudad de residencia"]] = "No pertenece al área metropolitana"
    dataOferentesColocados["Fecha Colocación"] = (pd.to_datetime(dataOferentesColocados["Fecha Colocación"], dayfirst=True, format='mixed').dt.strftime('%d/%m/%Y'))
    dataOferentesColocados["Programa de Gobierno"] = (dataOferentesColocados["Programa de Gobierno"]!="No Registra").replace(False, "No pertenece").replace(True, "Si pertenece")
    dataOferentesColocados["Condiciones Especiales"] = (dataOferentesColocados["Condiciones Especiales"]!="No Registra").replace(False, "No tiene").replace(True, "Si tiene")
    dataOferentesColocados["Programa de Gobierno Vacante"] = (dataOferentesColocados["Programa de Gobierno Vacante"]!="No Registra").replace(False, "No pertenece").replace(True, "Si pertenece")
    dataOferentesColocados.loc[~dataOferentesColocados["Municipio sede"].isin(["BUCARAMANGA","FLORIDABLANCA", "GIRÓN", "PIEDECUESTA"]),["Municipio sede"]] = "No pertenece al área metropolitana"

    #falta empresas,direccion,codigo vacante, proceso porque de eso hay que hacer un analisis a parte
    genero =  {"genero": dict(zip(dataOferentesColocados["sexo"].value_counts().keys(), dataOferentesColocados["sexo"].value_counts()))}
    edad =  {"edad": dict(zip(dataOferentesColocados["Edad"].value_counts().keys(), dataOferentesColocados["Edad"].value_counts()))}
    ciudadResidencia =  {"ciudadResidencia": dict(zip(dataOferentesColocados["Ciudad de residencia"].value_counts().keys(), dataOferentesColocados["Ciudad de residencia"].value_counts()))}
    programaGobierno =  {"programaGobierno": dict(zip(dataOferentesColocados["Programa de Gobierno"].value_counts().keys(), dataOferentesColocados["Programa de Gobierno"].value_counts()))}
    condicionesEspeciales =  {"condicionesEspeciales": dict(zip(dataOferentesColocados["Condiciones Especiales"].value_counts().keys(), dataOferentesColocados["Condiciones Especiales"].value_counts()))}
    fechaColocacion =  {"fechaColocacion": dict(zip(dataOferentesColocados["Fecha Colocación"].value_counts().keys(), dataOferentesColocados["Fecha Colocación"].value_counts()))}
    tipoColocado =  {"tipoColocado": dict(zip(dataOferentesColocados["Tipo de Colocado"].value_counts().keys(), dataOferentesColocados["Tipo de Colocado"].value_counts()))}
    programaGobiernoVacante =  {"programaGobiernoVacante": dict(zip(dataOferentesColocados["Programa de Gobierno Vacante"].value_counts().keys(), dataOferentesColocados["Programa de Gobierno Vacante"].value_counts()))}    
    manoObraCalificada =  {"manoObraCalificada": dict(zip(dataOferentesColocados["es_mano_de_obra_calificada"].value_counts().keys(), dataOferentesColocados["es_mano_de_obra_calificada"].value_counts()))}
    tipoContrato =  {"tipoContrato": dict(zip(dataOferentesColocados["Tipo Contrato"].value_counts().keys(), dataOferentesColocados["Tipo Contrato"].value_counts()))}
    sector =  {"sector": dict(zip(dataOferentesColocados["Sector"].value_counts().keys(), dataOferentesColocados["Sector"].value_counts()))}
    municipioSede =  {"municipioSede": dict(zip(dataOferentesColocados["Municipio sede"].value_counts().keys(), dataOferentesColocados["Municipio sede"].value_counts()))}
    with open('jsons/oferentesColocados.json', 'w+') as out_file:
        json.dump([genero, edad, ciudadResidencia, programaGobierno, condicionesEspeciales, fechaColocacion, tipoColocado, programaGobiernoVacante, manoObraCalificada, tipoContrato, sector, municipioSede], out_file, sort_keys = True, indent = 4, ensure_ascii = False)

def empresasIncritas():
    dataEmpresasInscritas = pd.read_excel("AGENCIA DE EMPLEO.xlsx", sheet_name="EMPRESAS INSCRITAS", usecols=["Tipo Documento", "Número Documento", "Naturaleza", "Tipo Empresa", "Actividad Económica", "Sector", "Tamaño", "Dirección", "Ciudad", "Fecha registro", "Canal de Registro", "Agencia Aprobó", "Agente Aprobó"]).replace(np.nan, "No Registra")
    dataEmpresasInscritas.loc[~dataEmpresasInscritas["Ciudad"].isin(["BUCARAMANGA","FLORIDABLANCA", "GIRÓN", "PIEDECUESTA"]),["Ciudad"]] = "No pertenece al área metropolitana"
    dataEmpresasInscritas["Fecha registro"] = (pd.to_datetime(dataEmpresasInscritas["Fecha registro"], dayfirst=True, format='mixed').dt.strftime('%d/%m/%Y'))

    #falta tipo empresa,actividad economica, direccion, porque de eso hay que hacer un analisis a parte
    naturaleza =  {"naturaleza": dict(zip(dataEmpresasInscritas["Naturaleza"].value_counts().keys(), dataEmpresasInscritas["Naturaleza"].value_counts()))}
    sector =  {"sector": dict(zip(dataEmpresasInscritas["Sector"].value_counts().keys(), dataEmpresasInscritas["Sector"].value_counts()))}
    tamano =  {"tamaño": dict(zip(dataEmpresasInscritas["Tamaño"].value_counts().keys(), dataEmpresasInscritas["Tamaño"].value_counts()))}
    ciudad =  {"ciudad": dict(zip(dataEmpresasInscritas["Ciudad"].value_counts().keys(), dataEmpresasInscritas["Ciudad"].value_counts()))}
    fechaRegistro =  {"fechaRegistro": dict(zip(dataEmpresasInscritas["Fecha registro"].value_counts().keys(), dataEmpresasInscritas["Fecha registro"].value_counts()))}
    canalRegistro =  {"canalRegistro": dict(zip(dataEmpresasInscritas["Canal de Registro"].value_counts().keys(), dataEmpresasInscritas["Canal de Registro"].value_counts()))}
    agenciaAprobo =  {"agenciaAprobo": dict(zip(dataEmpresasInscritas["Agencia Aprobó"].value_counts().keys(), dataEmpresasInscritas["Agencia Aprobó"].value_counts()))}    
    agenteAprobo =  {"agenteAprobo": dict(zip(dataEmpresasInscritas["Agente Aprobó"].value_counts().keys(), dataEmpresasInscritas["Agente Aprobó"].value_counts()))}
    with open('jsons/empresasInscritas.json', 'w+') as out_file:
        json.dump([naturaleza, sector, tamano, ciudad, fechaRegistro, canalRegistro, agenciaAprobo, agenteAprobo], out_file, sort_keys = True, indent = 4, ensure_ascii = False)

def vacantesPublicadas():
    dataVacantesPublicadas = pd.read_excel("AGENCIA DE EMPLEO.xlsx", sheet_name="VACANTES PUBLICADAS", usecols=["Código Proceso", "Nombre Vacante", "Cargo", "Empresa", "TipoDocumentoEmpresa", "NumeroDocumentoEmpresa", "Fecha Registro", "Fecha Vencimiento", "Estado Actual", "Programa de Gobierno", "Ubicación", "Discapacidad", "Puestos de Trabajo", "Tipo de contrato", "Fecha Publicación", "Requiere Mano De Obra Calificada"]).replace(np.nan, "No Registra")
    dataVacantesPublicadas.loc[dataVacantesPublicadas["Ubicación"].str.contains("BUCARAMANGA"),["Ubicación"]] = "BUCARAMANGA"
    dataVacantesPublicadas.loc[dataVacantesPublicadas["Ubicación"].str.contains("FLORIDABLANCA"),["Ubicación"]] = "FLORIDABLANCA"
    dataVacantesPublicadas.loc[dataVacantesPublicadas["Ubicación"].str.contains("GIRÓN"),["Ubicación"]] = "GIRÓN"
    dataVacantesPublicadas.loc[dataVacantesPublicadas["Ubicación"].str.contains("PIEDECUESTA"),["Ubicación"]] = "PIEDECUESTA"
    dataVacantesPublicadas.loc[~dataVacantesPublicadas["Ubicación"].str.contains("BUCARAMANGA|FLORIDABLANCA|GIRÓN|PIEDECUESTA", regex=True),["Ubicación"]] = "No pertenece al área metropolitana"
    dataVacantesPublicadas["Fecha Vencimiento"] = (pd.to_datetime(dataVacantesPublicadas["Fecha Vencimiento"], format='%d/%m/%Y').dt.strftime('%d/%m/%Y'))
    dataVacantesPublicadas["Fecha Publicación"] = (pd.to_datetime(dataVacantesPublicadas["Fecha Publicación"], format='%d/%m/%Y').dt.strftime('%d/%m/%Y'))
    dataVacantesPublicadas["Programa de Gobierno"] = (dataVacantesPublicadas["Programa de Gobierno"]!="No Registra").replace(False, "No pertenece").replace(True, "Si pertenece")
    dataVacantesPublicadas["Discapacidad"] = (dataVacantesPublicadas["Discapacidad"]!="No Registra").replace(False, "No presenta").replace(True, "Si presenta")

    #falta codigo proceso,nombre vacante, direccion, porque de eso hay que hacer un analisis a parte
    cargo =  {"cargo": dict(zip(dataVacantesPublicadas["Cargo"].value_counts().keys(), dataVacantesPublicadas["Cargo"].value_counts()))}
    empresa =  {"empresa": dict(zip(dataVacantesPublicadas["Empresa"].value_counts().keys(), dataVacantesPublicadas["Empresa"].value_counts()))}
    fechaVencimiento =  {"fechaVencimiento": dict(zip(dataVacantesPublicadas["Fecha Vencimiento"].value_counts().keys(), dataVacantesPublicadas["Fecha Vencimiento"].value_counts()))}
    estadoActual =  {"estadoActual": dict(zip(dataVacantesPublicadas["Estado Actual"].value_counts().keys(), dataVacantesPublicadas["Estado Actual"].value_counts()))}
    programaGobierno =  {"programaGobierno": dict(zip(dataVacantesPublicadas["Programa de Gobierno"].value_counts().keys(), dataVacantesPublicadas["Programa de Gobierno"].value_counts()))}
    ciudad =  {"ciudad": dict(zip(dataVacantesPublicadas["Ubicación"].value_counts().keys(), dataVacantesPublicadas["Ubicación"].value_counts()))}    
    discapacidad =  {"discapacidad": dict(zip(dataVacantesPublicadas["Discapacidad"].value_counts().keys(), dataVacantesPublicadas["Discapacidad"].value_counts()))}
    puestosTrabajo =  {"puestosTrabajo": dict(zip(dataVacantesPublicadas["Puestos de Trabajo"].value_counts().keys(), dataVacantesPublicadas["Puestos de Trabajo"].value_counts()))}
    tipoContrato =  {"tipoContrato": dict(zip(dataVacantesPublicadas["Tipo de contrato"].value_counts().keys(), dataVacantesPublicadas["Tipo de contrato"].value_counts()))}
    fechaPublicacion =  {"fechaPublicacion": dict(zip(dataVacantesPublicadas["Fecha Publicación"].value_counts().keys(), dataVacantesPublicadas["Fecha Publicación"].value_counts()))}
    manoObraCalificada =  {"manoObraCalificada": dict(zip(dataVacantesPublicadas["Requiere Mano De Obra Calificada"].value_counts().keys(), dataVacantesPublicadas["Requiere Mano De Obra Calificada"].value_counts()))}
    with open('jsons/vacantesPublicadas.json', 'w+') as out_file:
        json.dump([cargo, empresa, estadoActual, programaGobierno, ciudad, discapacidad, puestosTrabajo, tipoContrato, fechaPublicacion, manoObraCalificada], out_file, sort_keys = True, indent = 4, ensure_ascii = False)

#saveOferentesInscritos()
#saveOferentesRemitidos()
#saveOferentesColocados()
#empresasIncritas()
#vacantesPublicadas()

@app.route('/oferentes-inscritos-stats', methods=['GET'])
def OferentesInscritosStats():
    with open("jsons/oferentesInscritos.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )

@app.route('/oferentes-remitidos-stats', methods=['GET'])
def OferentesRemitidosStats():
    with open("jsons/oferentesRemitidos.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )

@app.route('/oferentes-colocados-stats', methods=['GET'])
def OferentesColocadosStats():
    with open("jsons/oferentesColocados.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )

@app.route('/empresas-inscritas-stats', methods=['GET'])
def EmpresasInscritasStats():
    with open("jsons/empresasInscritas.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )

@app.route('/vacantes-publicadas-stats', methods=['GET'])
def VacantesPublicadasStats():
    with open("jsons/vacantesPublicadas.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )

if __name__ == '__main__':
    app.run()

