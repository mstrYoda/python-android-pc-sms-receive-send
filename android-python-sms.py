import android , socket, threading ,json

droid = android.Android()

host = '192.168.0.x'
port = 4595

#client (bilgisayara bağlanacak) socketimiz
sock = socket.socket()
sock.connect((host,port))

#server (bilgisayardan sms alacak) socketimiz
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('',2595))

def cevapBekle():
    server.listen(5);
    while True:
        client,address = server.accept()
        gelen = client.recv(1024)
        if gelen:
            msj = json_dumps(gelen.decode('utf-8'))
            print('numara : ' + msj['numara'] + ' msj : ' + msj['msj'])
            droid.smsSend(msj['numara'],msj['msj']);
            client.close()

threading.Thread(target=cevapBekle)

gelen_id = droid.smsGetMessageIds(True,'inbox') #gelen kutusundaki okunmamış sms lerin id lerini alıyoruz. Eğer False deseydik okunmuş smslerin id lerini alırdık

okunanlar = [] #bir kere bilgisayara gönderdiğimiz sms i tekrar göndermemek için okunan sms lerin listesini bir dizide tutuyoruz

while len(gelen_id) > 0:
    for id in gelen_id:
        if id not in okunanlar:
            msj = droid.smsGetMessageById(id,['address','body']) #okunmamış sms in gönderen bilgisini ve msj içeriğini alıyoruz
            sock.sendall(str(msj[1]).encode()) #sms i bilgisayara gönderiyoruz
            okunanlar.append(id) #sms i okunanlar listesine alıyoruz
