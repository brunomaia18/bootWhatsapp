import pandas as pd
import pywhatkit as pk

df = pd.read_excel("nome do arquivo em .xlsx")

for i, mensagem in enumerate(df["Mensagem"]):
    
    numero = df.loc[i,"Numero"]
    pk.sendwhatmsg_instantly(numero,mensagem)
    
    sleep(2)
