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
    #dataOferentesInscritos["Fecha Registro"] = pd.to_datetime(dataOferentesInscritos["Fecha Registro"], dayfirst=True, format='mixed').dt.strftime('%d/%m/%Y')
    dataOferentesInscritos["Fecha Registro"] = pd.to_datetime(dataOferentesInscritos["Fecha Registro"], dayfirst=True, format='mixed')
    dataOferentesInscritos["Fecha Actualización"] = pd.to_datetime(dataOferentesInscritos["Fecha Actualización"], dayfirst=True, format='mixed')
    dataOferentesInscritos["Programa de Gobierno"] = (dataOferentesInscritos["Programa de Gobierno"]!="No Registra").replace(False, "No pertenece").replace(True, "Si pertenece")
    dataOferentesInscritos["Condiciones Especiales"] = (dataOferentesInscritos["Condiciones Especiales"]!="No Registra").replace(False, "No tiene").replace(True, "Si tiene")
    dataOferentesInscritos["Situación Laboral"] = dataOferentesInscritos["Situación Laboral"].replace("NO REGISTRA", "No Registra")
    dataOferentesInscritos.loc[~dataOferentesInscritos["Ciudad de Residencia"].isin(["BUCARAMANGA","FLORIDABLANCA", "GIRÓN", "PIEDECUESTA"]), ["Ciudad de Residencia"]] = "No pertenece al área metropolitana"
    dataOferentesInscritos = dataOferentesInscritos.sort_values(by="Fecha Registro")
    #falta titulo homologado porque de eso hay que hacer un analisis a parte
    canalRegistro = [["","Canal de Registro"], *list(zip(dataOferentesInscritos["Canal de Registro"].value_counts().keys(), dataOferentesInscritos["Canal de Registro"].value_counts()))]
    edad =  [["","Edad"], *list(zip(dataOferentesInscritos["Edad"].value_counts().keys(), dataOferentesInscritos["Edad"].value_counts()))]
    genero =  [["","Genero"], *list(zip(dataOferentesInscritos["Género"].value_counts().keys(), dataOferentesInscritos["Género"].value_counts()))]
    nivelEstudio = [["","Nivel de Estudio"], *list(zip(dataOferentesInscritos["Nivel de Estudio"].value_counts().keys(), dataOferentesInscritos["Nivel de Estudio"].value_counts()))]
    ciudadResidencia = [["","Ciudad de Residencia"], *list(zip(dataOferentesInscritos["Ciudad de Residencia"].value_counts().keys(), dataOferentesInscritos["Ciudad de Residencia"].value_counts()))]
    fechaRegistro = [["","Fecha de Registro"], *list(zip(dataOferentesInscritos["Fecha Registro"].value_counts().sort_index().keys().to_series().dt.date.astype(str), dataOferentesInscritos["Fecha Registro"].value_counts().sort_index()))]
    programaGobierno = [["","Programa de Gobierno"], *list(zip(dataOferentesInscritos["Programa de Gobierno"].value_counts().keys(), dataOferentesInscritos["Programa de Gobierno"].value_counts()))]
    condicionesEspeciales =  [["","Condiciones Especiales"], *list(zip(dataOferentesInscritos["Condiciones Especiales"].value_counts().keys(), dataOferentesInscritos["Condiciones Especiales"].value_counts()))]
    situacionLaboral =  [["","Situacion Laboral"], *list(zip(dataOferentesInscritos["Situación Laboral"].value_counts().keys(), dataOferentesInscritos["Situación Laboral"].value_counts()))]
    fechaActualizacion =  [["","Fecha de Actualizacion"], *list(zip(dataOferentesInscritos["Fecha Actualización"].value_counts().sort_index().keys().to_series().dt.date.astype(str), dataOferentesInscritos["Fecha Actualización"].value_counts().sort_index()))]
    porcentajeHojaVida =  [["","Porcentaje Hoja de Vida"], *list(zip(dataOferentesInscritos["% Hoja Vida"].value_counts().keys(), dataOferentesInscritos["% Hoja Vida"].value_counts()))]
    perteneceA =  [["","Ubicacion"], *list(zip(dataOferentesInscritos["Pertenece A"].value_counts().keys(), dataOferentesInscritos["Pertenece A"].value_counts()))]

    with open('jsons/oferentesInscritos/canalRegistro.json', 'w+') as out_file:
        json.dump([canalRegistro], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesInscritos/edad.json', 'w+') as out_file:
        json.dump([edad], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesInscritos/genero.json', 'w+') as out_file:
        json.dump([genero], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesInscritos/nivelEstudio.json', 'w+', encoding="utf-8") as out_file:
        json.dump([nivelEstudio], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesInscritos/ciudadResidencia.json', 'w+', encoding="utf-8") as out_file:
        json.dump([ciudadResidencia], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesInscritos/fechaRegistro.json', 'w+') as out_file:
        json.dump([fechaRegistro], out_file, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesInscritos/programaGobierno.json', 'w+') as out_file:
        json.dump([programaGobierno], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesInscritos/condicionesEspeciales.json', 'w+') as out_file:
        json.dump([condicionesEspeciales], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesInscritos/situacionLaboral.json', 'w+') as out_file:
        json.dump([situacionLaboral], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesInscritos/fechaActualizacion.json', 'w+') as out_file:
        json.dump([fechaActualizacion], out_file, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesInscritos/porcentajeHojaVida.json', 'w+') as out_file:
        json.dump([porcentajeHojaVida], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesInscritos/perteneceA.json', 'w+') as out_file:
        json.dump([perteneceA], out_file, sort_keys = True, indent = 4, ensure_ascii = False)

    """
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
    """

def saveOferentesRemitidos():
    dataOferentesRemitidos = pd.read_excel("AGENCIA DE EMPLEO.xlsx", sheet_name="OFERENTES REMITIDOS", usecols=["Tipo Documento", "Número Documento", "Sexo", "Dirección Oferente", "Ciudad de residencia", "Fecha Remisión", "Código Vacante", "Proceso", "Empresa", "Agente Remitió", "Tipo de Remisión", "Programa de Gobierno", "es_mano_de_obra_calificada"]).replace(np.nan, "No Registra")
    dataOferentesRemitidos["Fecha Remisión"] = (pd.to_datetime(dataOferentesRemitidos["Fecha Remisión"], dayfirst=True, format='mixed').dt.strftime('%d/%m/%Y'))
    dataOferentesRemitidos["Programa de Gobierno"] = (dataOferentesRemitidos["Programa de Gobierno"]!="No Registra").replace(False, "No pertenece").replace(True, "Si pertenece")
    dataOferentesRemitidos.loc[~dataOferentesRemitidos["Ciudad de residencia"].isin(["BUCARAMANGA","FLORIDABLANCA", "GIRÓN", "PIEDECUESTA"]), ["Ciudad de residencia"]] = "No pertenece al área metropolitana"
    dataOferentesRemitidos.sort_values(by="Fecha Remisión")

    #falta empresas,direccion,codigo vacante, proceso porque de eso hay que hacer un analisis a parte
    genero =  [["","Genero"], *list(zip(dataOferentesRemitidos["Sexo"].value_counts().keys(), dataOferentesRemitidos["Sexo"].value_counts()))]
    ciudadResidencia =  [["","Ciudad de Residencia"], *list(zip(dataOferentesRemitidos["Ciudad de residencia"].value_counts().keys(), dataOferentesRemitidos["Ciudad de residencia"].value_counts()))]
    fechaRemision =  [["","Fecha de Remision"], *list(zip(dataOferentesRemitidos["Fecha Remisión"].value_counts().keys(), dataOferentesRemitidos["Fecha Remisión"].value_counts()))]
    agenteRemitio =  [["","Agente que Remitio"], *list(zip(dataOferentesRemitidos["Agente Remitió"].value_counts().keys(), dataOferentesRemitidos["Agente Remitió"].value_counts()))]
    tipoRemision =  [["","Tipo de Remision"], *list(zip(dataOferentesRemitidos["Tipo de Remisión"].value_counts().keys(), dataOferentesRemitidos["Tipo de Remisión"].value_counts()))]
    programaGobierno =  [["","Programa de Gobierno"], *list(zip(dataOferentesRemitidos["Programa de Gobierno"].value_counts().keys(), dataOferentesRemitidos["Programa de Gobierno"].value_counts()))]
    manoObraCalificada =  [["","Mano de Obra Calificada"], *list(zip(dataOferentesRemitidos["es_mano_de_obra_calificada"].value_counts().keys(), dataOferentesRemitidos["es_mano_de_obra_calificada"].value_counts()))]
    with open('jsons/oferentesRemitidos/genero.json', 'w+') as out_file:
        json.dump([genero], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesRemitidos/ciudadResidencia.json', 'w+') as out_file:
        json.dump([ciudadResidencia], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesRemitidos/fechaRemision.json', 'w+') as out_file:
        json.dump([fechaRemision], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesRemitidos/agenteRemitio.json', 'w+') as out_file:
        json.dump([agenteRemitio], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesRemitidos/tipoRemision.json', 'w+') as out_file:
        json.dump([tipoRemision], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesRemitidos/programaGobierno.json', 'w+') as out_file:
        json.dump([programaGobierno], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesRemitidos/manoObraCalificada.json', 'w+') as out_file:
        json.dump([manoObraCalificada], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    """
    genero =  {"genero": dict(zip(dataOferentesRemitidos["Sexo"].value_counts().keys(), dataOferentesRemitidos["Sexo"].value_counts()))}
    ciudadResidencia =  {"ciudadResidencia": dict(zip(dataOferentesRemitidos["Ciudad de residencia"].value_counts().keys(), dataOferentesRemitidos["Ciudad de residencia"].value_counts()))}
    fechaRemision =  {"fechaRemision": dict(zip(dataOferentesRemitidos["Fecha Remisión"].value_counts().keys(), dataOferentesRemitidos["Fecha Remisión"].value_counts()))}
    agenteRemitio =  {"agenteRemitio": dict(zip(dataOferentesRemitidos["Agente Remitió"].value_counts().keys(), dataOferentesRemitidos["Agente Remitió"].value_counts()))}
    tipoRemision =  {"tipoRemision": dict(zip(dataOferentesRemitidos["Tipo de Remisión"].value_counts().keys(), dataOferentesRemitidos["Tipo de Remisión"].value_counts()))}
    programaGobierno =  {"programaGobierno": dict(zip(dataOferentesRemitidos["Programa de Gobierno"].value_counts().keys(), dataOferentesRemitidos["Programa de Gobierno"].value_counts()))}
    manoObraCalificada =  {"manoObraCalificada": dict(zip(dataOferentesRemitidos["es_mano_de_obra_calificada"].value_counts().keys(), dataOferentesRemitidos["es_mano_de_obra_calificada"].value_counts()))}
    with open('jsons/oferentesRemitidos.json', 'w+') as out_file:
        json.dump([genero, ciudadResidencia, fechaRemision, agenteRemitio, tipoRemision, programaGobierno, manoObraCalificada], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    """

def saveOferentesColocados():
    dataOferentesColocados = pd.read_excel("AGENCIA DE EMPLEO.xlsx", sheet_name="OFERENTES COLOCADOS", usecols=["Tipo Documento", "Número Documento", "sexo", "Edad", "Dirección Oferente", "Ciudad de residencia", "Programa de Gobierno", "Condiciones Especiales", "Código Vacante", "Fecha Colocación", "Proceso", "Empresa", "Tipo de Colocado", "Programa de Gobierno Vacante", "es_mano_de_obra_calificada", "Tipo Contrato", "Sector", "Municipio sede"]).replace(np.nan, "No Registra")
    dataOferentesColocados.loc[~dataOferentesColocados["Ciudad de residencia"].isin(["BUCARAMANGA","FLORIDABLANCA", "GIRÓN", "PIEDECUESTA"]),["Ciudad de residencia"]] = "No pertenece al área metropolitana"
    dataOferentesColocados["Fecha Colocación"] = (pd.to_datetime(dataOferentesColocados["Fecha Colocación"], dayfirst=True, format='mixed').dt.strftime('%d/%m/%Y'))
    dataOferentesColocados["Programa de Gobierno"] = (dataOferentesColocados["Programa de Gobierno"]!="No Registra").replace(False, "No pertenece").replace(True, "Si pertenece")
    dataOferentesColocados["Condiciones Especiales"] = (dataOferentesColocados["Condiciones Especiales"]!="No Registra").replace(False, "No tiene").replace(True, "Si tiene")
    dataOferentesColocados["Programa de Gobierno Vacante"] = (dataOferentesColocados["Programa de Gobierno Vacante"]!="No Registra").replace(False, "No pertenece").replace(True, "Si pertenece")
    dataOferentesColocados.loc[~dataOferentesColocados["Municipio sede"].isin(["BUCARAMANGA","FLORIDABLANCA", "GIRÓN", "PIEDECUESTA"]),["Municipio sede"]] = "No pertenece al área metropolitana"
    dataOferentesColocados.sort_values(by="Fecha Colocación")

    #falta empresas,direccion,codigo vacante, proceso porque de eso hay que hacer un analisis a parte
    genero =  [["","Genero"], *list(zip(dataOferentesColocados["sexo"].value_counts().keys(), dataOferentesColocados["sexo"].value_counts()))]
    edad =  [["","Edad"], *list(zip(dataOferentesColocados["Edad"].value_counts().keys(), dataOferentesColocados["Edad"].value_counts()))]
    ciudadResidencia =  [["","Ciudad de Residencia"], *list(zip(dataOferentesColocados["Ciudad de residencia"].value_counts().keys(), dataOferentesColocados["Ciudad de residencia"].value_counts()))]
    programaGobierno =  [["","Programa de Gobierno"], *list(zip(dataOferentesColocados["Programa de Gobierno"].value_counts().keys(), dataOferentesColocados["Programa de Gobierno"].value_counts()))]
    condicionesEspeciales =  [["","Condiciones Especiales"], *list(zip(dataOferentesColocados["Condiciones Especiales"].value_counts().keys(), dataOferentesColocados["Condiciones Especiales"].value_counts()))]
    fechaColocacion =  [["","Fecha de Colocacion"], *list(zip(dataOferentesColocados["Fecha Colocación"].value_counts().keys(), dataOferentesColocados["Fecha Colocación"].value_counts()))]
    tipoColocado =  [["","Tipo de Colocado"], *list(zip(dataOferentesColocados["Tipo de Colocado"].value_counts().keys(), dataOferentesColocados["Tipo de Colocado"].value_counts()))]
    programaGobiernoVacante =  [["","Programa de Gobierno de la Vacante"], *list(zip(dataOferentesColocados["Programa de Gobierno Vacante"].value_counts().keys(), dataOferentesColocados["Programa de Gobierno Vacante"].value_counts()))]
    manoObraCalificada =  [["","Mano de Obra Calificada"], *list(zip(dataOferentesColocados["es_mano_de_obra_calificada"].value_counts().keys(), dataOferentesColocados["es_mano_de_obra_calificada"].value_counts()))]
    tipoContrato =  [["","Tipo de Contrato"], *list(zip(dataOferentesColocados["Tipo Contrato"].value_counts().keys(), dataOferentesColocados["Tipo Contrato"].value_counts()))]
    sector =  [["","Sector"], *list(zip(dataOferentesColocados["Sector"].value_counts().keys(), dataOferentesColocados["Sector"].value_counts()))]
    municipioSede =  [["","Municipio Sede"], *list(zip(dataOferentesColocados["Municipio sede"].value_counts().keys(), dataOferentesColocados["Municipio sede"].value_counts()))]
    with open('jsons/oferentesColocados/genero.json', 'w+') as out_file:
        json.dump([genero], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesColocados/edad.json', 'w+') as out_file:
        json.dump([edad], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesColocados/ciudadResidencia.json', 'w+') as out_file:
        json.dump([ciudadResidencia], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesColocados/programaGobierno.json', 'w+') as out_file:
        json.dump([programaGobierno], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesColocados/condicionesEspeciales.json', 'w+') as out_file:
        json.dump([condicionesEspeciales], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesColocados/fechaColocacion.json', 'w+') as out_file:
        json.dump([fechaColocacion], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesColocados/tipoColocado.json', 'w+') as out_file:
        json.dump([tipoColocado], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesColocados/programaGobiernoVacante.json', 'w+') as out_file:
        json.dump([programaGobiernoVacante], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesColocados/manoObraCalificada.json', 'w+') as out_file:
        json.dump([manoObraCalificada], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesColocados/tipoContrato.json', 'w+') as out_file:
        json.dump([tipoContrato], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesColocados/sector.json', 'w+') as out_file:
        json.dump([sector], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/oferentesColocados/municipioSede.json', 'w+') as out_file:
        json.dump([municipioSede], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    """
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
    """

def empresasIncritas():
    dataEmpresasInscritas = pd.read_excel("AGENCIA DE EMPLEO.xlsx", sheet_name="EMPRESAS INSCRITAS", usecols=["Tipo Documento", "Número Documento", "Naturaleza", "Tipo Empresa", "Actividad Económica", "Sector", "Tamaño", "Dirección", "Ciudad", "Fecha registro", "Canal de Registro", "Agencia Aprobó", "Agente Aprobó"]).replace(np.nan, "No Registra")
    dataEmpresasInscritas.loc[~dataEmpresasInscritas["Ciudad"].isin(["BUCARAMANGA","FLORIDABLANCA", "GIRÓN", "PIEDECUESTA"]),["Ciudad"]] = "No pertenece al área metropolitana"
    dataEmpresasInscritas["Fecha registro"] = (pd.to_datetime(dataEmpresasInscritas["Fecha registro"], dayfirst=True, format='mixed').dt.strftime('%d/%m/%Y'))
    dataEmpresasInscritas.sort_values(by="Fecha registro")

    #falta tipo empresa,actividad economica, direccion, porque de eso hay que hacer un analisis a parte
    naturaleza =  [["","Naturaleza"], *list(zip(dataEmpresasInscritas["Naturaleza"].value_counts().keys(), dataEmpresasInscritas["Naturaleza"].value_counts()))]
    sector =  [["","Sector"], *list(zip(dataEmpresasInscritas["Sector"].value_counts().keys(), dataEmpresasInscritas["Sector"].value_counts()))]
    tamano =  [["","Tamaño"], *list(zip(dataEmpresasInscritas["Tamaño"].value_counts().keys(), dataEmpresasInscritas["Tamaño"].value_counts()))]
    ciudad =  [["","Ciudad"], *list(zip(dataEmpresasInscritas["Ciudad"].value_counts().keys(), dataEmpresasInscritas["Ciudad"].value_counts()))]
    fechaRegistro =  [["","Fecha de Registro"], *list(zip(dataEmpresasInscritas["Fecha registro"].value_counts().keys(), dataEmpresasInscritas["Fecha registro"].value_counts()))]
    canalRegistro =  [["","Canal de Registro"], *list(zip(dataEmpresasInscritas["Canal de Registro"].value_counts().keys(), dataEmpresasInscritas["Canal de Registro"].value_counts()))]
    agenciaAprobo =  [["","Agencia que Aprobo"], *list(zip(dataEmpresasInscritas["Agencia Aprobó"].value_counts().keys(), dataEmpresasInscritas["Agencia Aprobó"].value_counts()))] 
    agenteAprobo =  [["","agenteAprobo"], *list(zip(dataEmpresasInscritas["Agente Aprobó"].value_counts().keys(), dataEmpresasInscritas["Agente Aprobó"].value_counts()))]
    with open('jsons/empresasInscritas/naturaleza.json', 'w+') as out_file:
        json.dump([naturaleza], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/empresasInscritas/sector.json', 'w+') as out_file:
        json.dump([sector], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/empresasInscritas/tamano.json', 'w+') as out_file:
        json.dump([tamano], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/empresasInscritas/ciudad.json', 'w+') as out_file:
        json.dump([ciudad], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/empresasInscritas/fechaRegistro.json', 'w+') as out_file:
        json.dump([fechaRegistro], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/empresasInscritas/canalRegistro.json', 'w+') as out_file:
        json.dump([canalRegistro], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/empresasInscritas/agenciaAprobo.json', 'w+') as out_file:
        json.dump([agenciaAprobo], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/empresasInscritas/agenteAprobo.json', 'w+') as out_file:
        json.dump([agenteAprobo], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    """
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
    """

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
    dataVacantesPublicadas.sort_values(by="Fecha Vencimiento")

    #falta codigo proceso,nombre vacante, direccion, porque de eso hay que hacer un analisis a parte
    cargo =  [["","Cargo"], *list(zip(dataVacantesPublicadas["Cargo"].value_counts().keys(), dataVacantesPublicadas["Cargo"].value_counts()))]
    empresa =  [["","Empresa"], *list(zip(dataVacantesPublicadas["Empresa"].value_counts().keys(), dataVacantesPublicadas["Empresa"].value_counts()))]
    fechaVencimiento =  [["","Fecha de Vencimiento"], *list(zip(dataVacantesPublicadas["Fecha Vencimiento"].value_counts().keys(), dataVacantesPublicadas["Fecha Vencimiento"].value_counts()))]
    estadoActual =  [["","Estado Actual"], *list(zip(dataVacantesPublicadas["Estado Actual"].value_counts().keys(), dataVacantesPublicadas["Estado Actual"].value_counts()))]
    programaGobierno =  [["","Programa de Gobierno"], *list(zip(dataVacantesPublicadas["Programa de Gobierno"].value_counts().keys(), dataVacantesPublicadas["Programa de Gobierno"].value_counts()))]
    ciudad =  [["","Ciudad"], *list(zip(dataVacantesPublicadas["Ubicación"].value_counts().keys(), dataVacantesPublicadas["Ubicación"].value_counts()))]
    discapacidad =  [["","Discapacidad"], *list(zip(dataVacantesPublicadas["Discapacidad"].value_counts().keys(), dataVacantesPublicadas["Discapacidad"].value_counts()))]
    puestosTrabajo =  [["","Puestos de Trabajo"], *list(zip(dataVacantesPublicadas["Puestos de Trabajo"].value_counts().keys(), dataVacantesPublicadas["Puestos de Trabajo"].value_counts()))]
    tipoContrato =  [["","Tipo de Contrato"], *list(zip(dataVacantesPublicadas["Tipo de contrato"].value_counts().keys(), dataVacantesPublicadas["Tipo de contrato"].value_counts()))]
    fechaPublicacion =  [["","Fecha de Publicacion"], *list(zip(dataVacantesPublicadas["Fecha Publicación"].value_counts().keys(), dataVacantesPublicadas["Fecha Publicación"].value_counts()))]
    manoObraCalificada =  [["","manoObraCalificada"], *list(zip(dataVacantesPublicadas["Requiere Mano De Obra Calificada"].value_counts().keys(), dataVacantesPublicadas["Requiere Mano De Obra Calificada"].value_counts()))]
    with open('jsons/vacantesPublicadas/cargo.json', 'w+') as out_file:
        json.dump([cargo], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/vacantesPublicadas/empresa.json', 'w+') as out_file:
        json.dump([empresa], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/vacantesPublicadas/estadoActual.json', 'w+') as out_file:
        json.dump([estadoActual], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/vacantesPublicadas/programaGobierno.json', 'w+') as out_file:
        json.dump([programaGobierno], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/vacantesPublicadas/ciudad.json', 'w+') as out_file:
        json.dump([ciudad], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/vacantesPublicadas/discapacidad.json', 'w+') as out_file:
        json.dump([discapacidad], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/vacantesPublicadas/puestosTrabajo.json', 'w+') as out_file:
        json.dump([puestosTrabajo], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/vacantesPublicadas/tipoContrato.json', 'w+') as out_file:
        json.dump([tipoContrato], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/vacantesPublicadas/fechaPublicacion.json', 'w+') as out_file:
        json.dump([fechaPublicacion], out_file, sort_keys = True, indent = 4, ensure_ascii = False)
    with open('jsons/vacantesPublicadas/manoObraCalificada.json', 'w+') as out_file:
        json.dump([manoObraCalificada], out_file, sort_keys = True, indent = 4, ensure_ascii = False)

    """
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
    """

saveOferentesInscritos()
#saveOferentesRemitidos()
#saveOferentesColocados()
#empresasIncritas()
#vacantesPublicadas()

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
def oferentesInscritosfechaActualizacion():
    with open("jsons/oferentesInscritos/fechaActualizacion.json","r") as file:
        json_string = file.read()
    return Response(json_string,content_type="application/json; charset=utf-8" )
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
@app.route('/empresasInscritas/agenciaAprobo', methods=['GET'])
def empresasInscritasagenciaAprobo():
    with open("jsons/empresasInscritas/agenciaAprobo.json","r") as file:
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

