Bot interativo Telegram para Zabbix.

Criado em: 17/11/2017

Desenvolvido por: Eddy Vaz - eddy.vaz@gmail.com

*Usados, parcial ou integralmente, scripts de: https://github.com/q1x/zabbix-gnomes



-Funcionalidades:

/help -> lista as seguintes funcionalidades:

/zg - apresenta lista de grupos de hosts

/zhg+GRUPO - apresenta lista de hosts por grupo, substituir GRUPO pelo nome do grupo

/zi - apresenta últimos 20 incidentes gerais

/zhi+HOST - apresenta incidente(s) por host, substituir HOST pelo nome do host


-Dependências:

-Servidor Zabbix e bot Telegram configurados;

-Editar zbx.conf com informações do servidor Zabbix;
 
-Python 2.7 e módulos pyzabbix e pillow; 

-Python 3 e módulo telepot.


-Execução:

./e-zbx.py &

