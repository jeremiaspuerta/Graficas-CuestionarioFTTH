#Dependecnias gspread, oauth2client y pandas
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

#Autenticación para gspread

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("patchToJsonKeyfile", scope)
client = gspread.authorize(creds)

#############################

#Abrir la hoja 2 de sheets
sheet = client.open("Respuestas de Formulario Inspector FTTH").get_worksheet(2) 

#Pasar sheet a data frame
df = pd.DataFrame(sheet.get_all_records())

#Cambio de nombre de las columnas
df.columns = ['Fecha','Tiempo','Empresa','Cuadrilla','Cliente','Respeta orden de conectores','Usa pasagoma','Precinto enumerado','Coloca retenciones', 'Correcta altura de pasacalles', 'Esquiva transformador', 'Deja fibra en techo','Deja equipos amurados', 'Calidad de cableador interno','Potencia Optica', 'Acceso remoto', 'Coloca DNS', 'Eplica APP Westnet']


