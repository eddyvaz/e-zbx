#!/usr/bin/python3
#######################################################
# Bot interativo do Telegram p/ Zabbix                #
#                                                     #
#-Desenvolvido por: Eddy S. G. Vaz                    #
#                                                     #
#Criado em: 17/11/2017                                #
#Ultima implementacao: 29/11/2017                     #
#                                                     #
#***Usados, parcial ou integralmente, scripts de:     #
# https://github.com/q1x/zabbix-gnomes                #
#######################################################

import telepot
import time
import os


def handle(msg):
   content_type, chat_type, chat_id = telepot.glance(msg)

   if (content_type == 'text'):
      command = msg['text']
      #print ('Got command: %s' % command)

#######################################################inicio comandos
   ##menu com opcoes de comandos
   if '/help' in command:
      bot.sendMessage(chat_id, "\n-COMANDOS ZABBIX SERVER:\n\n /zg - lista grupos de hosts\n /zhg+G - hosts por grupo, substituir G pelo nome do grupo\n /zi - últimos 20 incidentes gerais\n /zhi+H - incidente(s) ativo(s) por host, substituir H pelo nome do host\n")
     
   ##lista de grupos de hosts
   if '/zg' in command:
      bot.sendMessage(chat_id, os.popen('python ./scripts/zgroupfinder.py').read())
      
   ##lista de hosts por grupo
   if '/zhg' in command.split('+')[0]:
      zhg = os.popen('python ./scripts/zghostfinder.py ' + command.split('+')[1]).read()
      bot.sendMessage(chat_id, '-Hosts: \n' + zhg)

   ##últimos 20 incidentes
   if '/zi' in command:
      bot.sendMessage(chat_id, os.popen('python ./scripts/zeventfinder.py -L 20 --all-hosts').read())

   ##incidente(s) ativo(s) por host
   if '/zhi' in command.split('+')[0]:
      zhi = os.popen('python ./scripts/./zhtrigfinder.py -A ' + command.split('+')[1]).read()
      bot.sendMessage(chat_id, '-Incidente(s) ativo(s): \n' + zhi)


################################################################fim comandos
## bot API key
bot = telepot.Bot('TOKEN_TELEGRAM')
bot.message_loop(handle)

## Aguardar novas msgs
while 1:
   time.sleep(20)
   
