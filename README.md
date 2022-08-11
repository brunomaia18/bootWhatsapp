# bootWhatsapp
Estou Iniciando no python então resolvir fazer esse Boot de whatsapp usando a biblioteca <strong>pandas e PyWhatKit</strong>



Irei passar algumas Instruções, o boot ainda nao foi criado a interface para ser mais interativo, mas com o tempo irei lançar atualizações dele:

º O bote pega um arquivo .xlsx ler o que tem la, e envia mensagem para o numero que esta escrito na planinha do excel, facilitando com que o usuario faça cadastra de pessoas
e consiga entrar em contato com elas futuramente de forma automatica, ṕodendo ate msm programar a hora que iremos falar com ela ("irei tentar fazer com que vc determine o dia
e a hora que a mensagem vai ser enviada")


º Dentro do codigo teremos que fazer umas alteraçoes  vamos entrar na funçao:
def sendwhatmsg_instantly(
    phone_no: str,
    message: str,
    wait_time: int = 8,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
    time.sleep(4)
    pg.click(core.WIDTH / 2, core.HEIGHT / 2)
    time.sleep(wait_time - 4)
    pg.press("enter")
    log.log_message(_time=time.localtime(), receiver=phone_no, message=message) 
    ------------------------------- Quando chegamos nessa parte da funçao iremos acrescentar mais algumas coisas como:
    sleep(3) #isso é para da tempo da mensagem ser enviada
    pg.hotkeys('ctrl','w') #isso e para fechamos a aba do whatsapp web para abrir outra
    pg.press('enter') #vamos confirmar que queremos que a aba seja fechada 
    

altere o codigo acima caso você queira que seu boot feche as abas que ele for abrindo, se nao tiver problema pra você  pode deixar o codigo do jeito que está



  ºFuturas atualizações:
-Irei fazer com que o sistema fique interativo com o uso de uma interface
-tera um sistema de login para que o bote possa ser vendido
-Envio de mensagem com Dia e com a hora determinada pelo usuario

